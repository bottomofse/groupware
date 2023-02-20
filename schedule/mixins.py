import datetime
import calendar
from collections import deque

class BaseCalendarMixin:

    first_weekday = 0
    week_names = ['日','月','火','水','木','金','土',]
    
    def setup_calendar(self):
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):

        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)

        return week_names

class MonthCalendarMixin(BaseCalendarMixin):
    #前の月
    def get_previous_month(self, date):
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)
    #次の月
    def get_next_month(self, date):
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        return self._calendar.monthdatescalendar(date.year, date.month)

    def get_current_month(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        self.setup_calendar()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data

class WeekCalendarMixin(BaseCalendarMixin):

    def get_week_days(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        for week in self._calendar.monthdatescalendar(date.year, date.month):
            if date in week:
                return week
        
    def get_week_calendar(self):
        self.setup_calendar()
        days = self.get_week_days()
        first = days[0]
        last = days[-1]
        calendar_data = {
            'now': datetime.date.today(),
            'week_days': days,
            'week_previous': first - datetime.timedelta(days=7),
            'week_next': first + datetime.timedelta(days=7),
            'week_names': self.get_week_names(),
            'week_first': first,
            'week_last': last,
        }
        return calendar_data

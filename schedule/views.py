from django.views.generic import TemplateView
from . import mixins

class MonthCalendar(mixins.MonthCalendarMixin, TemplateView):

    template_name = 'schedule/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
    
class WeekCalendar(mixins.WeekCalendarMixin, TemplateView):

    template_name = 'schedule/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context
from django.contrib import admin
from .models import GroupwareFunction

class GroupwareFunctionAdmin(admin.ModelAdmin):
    pass

admin.site.register(GroupwareFunction, GroupwareFunctionAdmin)

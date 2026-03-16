from django.contrib import admin

# Register your models here.
#user password: mashaSUPER11

from models import IssueType, Resolution, Issue, Comment

admin.site.register(IssueType)
admin.site.register(Resolution)
admin.site.register(Issue)
admin.site.register(Comment)
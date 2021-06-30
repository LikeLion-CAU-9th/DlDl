from django.contrib import admin
from apply.models import Apply, Project, ProjectComment

# Register your models here.

admin.site.register(Apply)
admin.site.register(Project)
admin.site.register(ProjectComment)
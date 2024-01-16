from django.contrib import admin

# Register your models here.

from .models import University, Institute, SubjectTopic, Thesis, Keyword, ThesisType, Language

admin.site.register(University)
admin.site.register(Institute)
admin.site.register(SubjectTopic)
admin.site.register(Thesis)
admin.site.register(Keyword)
admin.site.register(ThesisType)
admin.site.register(Language)
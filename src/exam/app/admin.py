from django.contrib import admin
from app.models import Exam, Question, Option

class OptionInfield(admin.TabularInline):
    model = Option
    extra = 2

class ExamApp(admin.ModelAdmin):
    fieldsets = [ 
	(None, {'fields':['title']}),
	('Information', {'fields':['id', 'times_taken'], 'classes':['collapse']}),
    ]
    readonly_fields=('id','times_taken')
    list_filter = ['id']
    search_fields = ['title']

class QApp(admin.ModelAdmin):
    fieldsets = [ 
	('Question link', {'fields':['exam']}),
	(None, {'fields':['text','correct_answer']}),
    ]
    inlines = [OptionInfield]

admin.site.register(Exam, ExamApp)
admin.site.register(Question, QApp)

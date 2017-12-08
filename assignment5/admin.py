from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Student,Parent,Teacher,StudentParent,Marks,Exam,Course,Grade,Event_registration,Event,Invoice,Login_role

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
    }
	
class ExamAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
    }
	
class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
    }
	
class InvoiceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
    }

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(StudentParent)
admin.site.register(Teacher)
admin.site.register(Login_role)
admin.site.register(Course,CourseAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Marks)
admin.site.register(Grade)
admin.site.register(Event,EventAdmin)
admin.site.register(Event_registration)
admin.site.register(Invoice,InvoiceAdmin)


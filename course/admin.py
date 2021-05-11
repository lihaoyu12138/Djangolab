
from django.contrib import admin

from .models import ClassTime, Course,Student,Membership


    
class ClassTimeInline(admin.TabularInline):
    model = ClassTime
    extra=5

    
class CourseAdmin(admin.ModelAdmin):
    inlines = [ClassTimeInline]
    list_display = ('name', 'Start_teacher', 'introduction','tel','mailbox','class_time','date','end')
    list_filter = ['name']
    search_fields = ['name']
    
admin.site.register(Course,CourseAdmin)        

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'studentid', 'tel','mailbox','perm')
  
class MembershipAdmin( admin.ModelAdmin):
    list__display = ( 'student', 'classtime','date_joined')

admin.site.register(Student,StudentAdmin) 
admin.site.register(Membership,MembershipAdmin) 

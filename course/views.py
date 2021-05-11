
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Course,ClassTime
from django.contrib import messages
 
def getTea(request):
    try:
        tea = Teacher.objects.get(uid = request.session['schoolid'])
    except Teacher.DoesNotExist:
        raise Http404("没有数据")
    except KeyError:
        raise Http404("非标准用户或未登录")
    return tea
    
def getStu(request):
    try:
        stu = Student.objects.get(uid = request.session['studentid'])
    except Student.DoesNotExist:
        raise Http404("没有数据")
    except KeyError:
        raise Http404("非标准用户或未登录")
    return stu
    
def toast(request):
    messages.success(request,"哈哈哈哈")
        
class IndexView(generic.ListView):
    template_name = 'course/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        return Course.objects.order_by('Start_teacher')[:100]


class DetailView(generic.DetailView):
    model = Course
    template_name = 'course/detail.html'


class ClassView(generic.ListView):
    model = ClassTime
    template_name = 'course/class.html'
    context_object_name = 'latest_class_list'
    
    def get_queryset(self):
        return ClassTime.objects.order_by('teacher')[:100]
        
class ClassdetailView(generic.DetailView):
    model = ClassTime
    template_name = 'course/classdetail.html'        
        

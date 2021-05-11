import datetime
from django.db import models
from home.models import Teacher
from ckeditor.fields import RichTextField

class Course(models.Model):
    class Meta:
        verbose_name="课程"
        verbose_name_plural="课程"

    name = models.CharField(max_length=200)
    Start_teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    introduction= RichTextField()
    tel = models.CharField(max_length=20)
    mailbox=models.CharField(max_length=200)
    class_time= models.CharField(max_length=200)
    date = models.DateTimeField('Start Date')
    end = models.DateTimeField('End Date', blank=True, null=True)  
    def get_agenda(self):
        return self.agenda.all()
    def isOK(self, day, start, end):
        return True
    def __str__(self):
        return self.name
  
class Student(models.Model):
    class Meta:
        verbose_name="学生"
        verbose_name_plural="学生"
    name = models.CharField(max_length=200, verbose_name="姓名")
    studentid = models.CharField(max_length=10, verbose_name="学生证号")
    tel = models.CharField(max_length=20)
    mailbox=models.CharField(max_length=200)
    perm = models.IntegerField(default=0, verbose_name="权限") # web permissions
        
        
class ClassTime(models.Model):
   course= models.ForeignKey(Course, on_delete=models.CASCADE)
   class_time=models.CharField(max_length=200)
   teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
   students= models.ManyToManyField(Student, through='Membership')
   teacher_tel = models.CharField(max_length=20)
   teacher_mailbox=models.CharField(max_length=200)
       
   def __str__(self):
        return self.class_time
        
class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classtime = models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    date_joined = models.DateField()        # 进组时间
   
'''class CourseAgenda(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='agenda')
    title = models.CharField(max_length=200)
    teacherid = models.CharField(max_length=12)
    teachername = models.CharField(max_length=40)
    repeat = models.IntegerField(default=0)
    date = models.DateField(default='2018-01-01')
    week = models.IntegerField(default=-1)
    start_time = models.TimeField(default='00:00')
    end_time = models.TimeField(default='00:00')
    confirm = models.IntegerField(default=0)
       
    def collide_time(self, other):
        if ((self.start_time < other.end_time) and (self.start_time > other.start_time)):
            return True
        if ((self.end_time > other.start_time) and (self.end_time < other.end_time)):
            return True
        return False

    def collide(self):
        today = datetime.date.today()
        all_agenda = RoomAgenda.objects.filter(room=self.room,date__gte=today)
        if self.repeat == 1:
            for a in all_agenda.filter(week=self.week,repeat=1):
                if self.collide_time(a):
                    return True
            for a in all_agenda.filter(date__lte=self.date,week=self.week,repeat=0):
                if self.collide_time(a):
                    return True
        else:
            for a in all_agenda.filter(date=self.date,repeat=0):
                if self.collide_time(a):
                    return True
            for a in all_agenda.filter(date__gte=self.date,week=self.week,repeat=1):
                if self.collide_time(a):
                    return True
        return False'''
        
         
class techer_History(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_time=models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    Lesson_No = models.IntegerField(default=0,verbose_name="第几次课")
    date = models.DateTimeField('上课日期')
    note = models.CharField(max_length=200,verbose_name="该次实验反映问题与教师记录")    
    
class studentHistory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_time=models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    techer=models.ForeignKey(Teacher, on_delete = models.CASCADE)
    Lesson_No = models.IntegerField(default=0,verbose_name="第几次课")
    student_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    Experiment_completion=models.CharField(max_length=200,verbose_name="学生i的实验完成情况")
    date = models.DateTimeField('上课日期')
    note = models.CharField(max_length=200,verbose_name="该次实验反映问题与改进建议")
    
    
class Experiment(models.Model):
    techer=models.ForeignKey(Teacher, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_time=models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    experiment_No = models.IntegerField(default=0,verbose_name="第几次实验")
    info = models.CharField(max_length=500, blank=True, verbose_name="该次实验描述")
    
    class Meta:
        verbose_name="一次实验课"
        verbose_name_plural="一次实验课"
    
class Experimentpart(models.Model):
    experiment=models.ForeignKey(Experiment, on_delete = models.CASCADE)
    content = models.CharField(max_length=600)
    votes = models.IntegerField(default=0)
    '''此处添加一个学生能提供反馈的ckeditor文本框，或者再加两个选项变成投票形式'''
    def __str__(self):
        return self.content
    
    

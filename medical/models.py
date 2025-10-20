from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    student_id = models.CharField(max_length=20, verbose_name='学号', unique=True)
    
    def __str__(self):
        return f'{self.name} - {self.student_id}'
    
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
from django.shortcuts import render
from .models import Student

# 查看所有学生信息
def student_list(request):
    students = Student.objects.all()
    return render(request, 'medical/student_list.html', {'students': students})

# 添加学生信息
def add_student(request):
    # 这里可以实现表单提交逻辑
    return render(request, 'medical/add_student.html')
from django.shortcuts import render
from student_info.models import StudentBaseInfo
import json
from django.shortcuts import render, HttpResponse
from student_info import models
# Create your views here.

from django.core.files.base import ContentFile
# import requests

# Create your views here.
class Student(object):
    def __init__(self,stu_name,stu_no) -> None:
        super().__init__()
        self.stu_name=stu_name
        self.stu_no=stu_no

    def sign_in(request):
        if request.method == "POST":
            data=json.load(request.body)




    def updateinfo(request):
        if request.method == 'POST':
            # img = request.FILES.get('photo')
            # user = request.FILES.get('photo').name

            new_img = models.mypicture(
                photo=request.FILES.get('photo'),  # 拿到图片
                user=request.FILES.get('photo').name # 拿到图片的名字
            )
            new_img.save()  # 保存图片
            return HttpResponse('上传成功！')  

        return render(request, 'index.html')

    def login(self,request):   #登陆
        return render(request,"music.html")     #返回HTML模板      
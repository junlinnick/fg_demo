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




    # def updateinfo(request):
    #     if request.method == 'POST':
    #         # img = request.FILES.get('photo')
    #         # user = request.FILES.get('photo').name

    #         new_img = models.mypicture(
    #             photo=request.FILES.get('photo'),  # 拿到图片
    #             user=request.FILES.get('photo').name # 拿到图片的名字
    #         )
    #         new_img.save()  # 保存图片
    #         return HttpResponse('上传成功！')  

    #     return render(request, 'index.html')

    def data(request):
        datas = StudentBaseInfo.get_all()

        context = {
            'datas': datas,
        }
        return render(request, 'data.html', context=context)


    def index(request):
        return render(request, 'index.html')


    def upload_file(request):

        if request.method == "POST":    # 请求方法为POST时，进行处理
            myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(os.path.join('facePhoto', myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作

            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()

            pictureLocation = os.path.join('facePhoto', myFile.name)
            data = StudentBaseInfo()
            data.picture = pictureLocation
            stu_name = request.POST['stu_name']
            stu_no = request.POST['stu_no']
            data.names = stu_name
            data.save()

            red.set(stu_name, stu_no,pictureLocation)

            return HttpResponseRedirect('/index/')

        elif request.method == 'GET':
            return render(request, 'index.html')
from django.shortcuts import render
from student_info.models import StudentBaseInfo
import json
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
            

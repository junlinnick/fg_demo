from enum import unique
from django.db import models
from  jsonfield import JSONField
# Create your models here.

class StudentBaseInfo(models.Model):
    '''
    学生基本信息表
    '''
    id = models.AutoField(primary_key=True, editable=False)
    stu_name=models.CharField(max_length=50, verbose_name="学生名称")
    stu_no=models.CharField(max_length=50, verbose_name="学生编号", unique = True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table='student_base_info'
        app_label='student_info'

class StudentCheckInfo(models.Model):
    '''
    学生行为信息表
    '''
    class ActionTypes(object):
        DEFAULT,CHECKIN, CHECKOUT  =1, 2, 3
        OPTIONS = (DEFAULT,"未出现"),(CHECKIN, "签到"), ( CHECKOUT , "离开")
    class Mode(object):
        ABSENT, LATE, EARLYLEAVING, NORMAL  =1, 2, 3, 4
        OPTIONS = (ABSENT,"旷课"),(LATE, "迟到"), ( EARLYLEAVING , "早退"), ( NORMAL , "正常")

    id = models.AutoField(primary_key=True, editable=False)
    stu_no=models.ForeignKey('StudentBaseInfo',to_field = 'stu_no', on_delete=models.CASCADE, verbose_name = "学生编号")
    status=models.IntegerField(default = ActionTypes.DEFAULT, choices = ActionTypes.OPTIONS, verbose_name="学生行为种类")
    mode=models.IntegerField(default = Mode.ABSENT, choices = Mode.OPTIONS, verbose_name="学生出席状态")
    is_deleted=models.BooleanField(default = False, null = True ,verbose_name= "删除标记")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间" )
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="更新时间" )
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table='student_check_info'
        app_label='student_info'




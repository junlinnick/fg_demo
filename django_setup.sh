tips:
https://www.byhy.net/tut/webdev/django/04/
https://www.bilibili.com/read/cv7444716/
https://www.jianshu.com/p/b81abbf46e6c
https://www.cnblogs.com/wjw1014/p/8664474.html

# 执行命令创建项目目录，并且进入到项目目录
cd /data/checkin

# 然后执行命令 创建manage.py 和 项目配置目录 名为 backend
django-admin startproject backend 

python manage.py migrate


python manage.py startapp student_info 

python manage.py makemigrations student_info
python manage.py migrate
from django.contrib import admin
from django.urls import path
from  student_info.views import Student
from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#                   path('admin/', admin.site.urls),
#                   path('updateinfo/', Student.updateinfo),
#                 path("login/",Student.login),
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', Student.index),
    url(r'^data/$', Student.data),
    url(r'^uploadFile/', Student.upload_file),
    url(r'^camera/', facelogin),
    url(r'^$', home),
    url(r'^facePhoto/(?P<path>.*)$', serve, {'document_root': 'facePhoto'}),
    url(r'^chouqian/facePhoto/(?P<path>.*)$', serve, {'document_root': 'facePhoto'}),
    url(r'^chouqian/', chouqian),
    path(r'register/', register),
    path(r'login/', login),
    path(r'logout/', tologin),
]

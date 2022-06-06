from django.contrib import admin
from django.urls import path
from  student_info.views import Student
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('updateinfo/', Student.updateinfo),
                path("login/",Student.login),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
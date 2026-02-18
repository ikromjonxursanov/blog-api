
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapi/v1/', include('blogapi.urls')),
    path('', include("posts.urls"))
]

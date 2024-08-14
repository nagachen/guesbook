from django.urls import path
from django.views.generic import RedirectView
 #. 表示当前目录：在 Python 中，点号 . 用于表示当前目录。
 # 因此，.views 表示当前应用目录下的 views.py 文件。
from .views import * 
from django.conf.urls import include

urlpatterns = [
    #as_view() 是 Django 类视图中的一个类方法，用于将类视图实例化并返回一个可调用的视图函数。
    # 这是 Django 中将类视图转换为函数视图的标准方式，便于与 URL 路由结合使用。
    #RedirectView：这是一个通用视图类，用于处理 URL 重定向。它会自动生成一个 HTTP 重定向响应。
    #url='message/'：这个参数指定了重定向的目标 URL。当用户访问根路径 / 时，他们会被重定向到 /message/。
    
    path('',MessageListView.as_view()),
    path('<int:pk>/',MessageDetail.as_view()),
    path('create/',MessageCreate.as_view()),
    path('<int:pk>/delete/',MessageDelete.as_view()),###
 
]
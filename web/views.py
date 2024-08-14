from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin ###
from .forms import MessageForm
# Create your views here.
#留言列表
class MessageListView(ListView):
    model = Message
    ordering =['-id'] #以id欄位值由大至小反向排列

#留言檢視
class MessageDetail(DetailView):
    model = Message

#新增留言
class MessageCreate(CreateView):
    form_class = MessageForm
    success_url = '/message/'
    #指定欲使用的頁面範本
    template_name = 'form.html'

#刪除留言 ###
class MessageDelete(LoginRequiredMixin,DeleteView):
    model = Message
    success_url = '/message'
    template_name='confirm_delete.html'    

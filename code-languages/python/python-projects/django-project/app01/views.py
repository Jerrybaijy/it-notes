from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def home(request):
    # 1.去request中可以获取请求的数据
    # 2.做一些业务处理
    # 3.给浏览器返回内容
    # return HttpResponse("成功")

    # django寻找html模板的顺序
    # 1.settings -> TEMPLATES
    return render(request,'home.html')
from django.shortcuts import render, HttpResponse
import os
from .forms import *


# Create your views here.
def upload_file(request):
    if request.method == 'GET':
        return render(request, 'app5/upload.html')
    if request.method == 'POST':
        myFile = request.FILES.get("myfile", None)
        if myFile:
            path = 'media/uploads/'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path + myFile.name), 'wb+')
            for chunk in myFile.chunks():
                dest.write(chunk)
            dest.close()
            return HttpResponse("上传完成！")
    else:
        return HttpResponse("没有上传文件！")


def userinfo_form(request):
    if request.method == "GET":
        myform = UserInfoForm()
        return render(request, 'app5/userinfo.html', {'form_obj': myform})

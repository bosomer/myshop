from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app2.models import UserBaseInfo


def test_redirect(request):
    return redirect("https://www.baidu.com/")


def test_redirect_views(request, id):
    return redirect('app2_userinfo', id)


def test_redirect_model(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)


def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号：" + str(user.id) + "姓名：" + user.username)


def test_render(request):
    return render(request, 'app2/test_render.html', {'info': 'hello django'}, content_type='text/html')


def test_response(request):
    response = HttpResponse()
    response.write("hello django")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return response


def test_post(request):
    print(request.method)  # 获取HTTP的请求方式
    print(request.POST.get("username"))  # 获取POST请求的”username“的值
    return render(request, "app2/test_post.html")


def test_get(request):
    print(request.get_host())  # 域名 + 端口
    print(request.get_raw_uri())  # 全部路径，包含参数
    print(request.path)  # 获取访问文件路径，不含参数
    print(request.get_full_path())  # 获取访问文件路径，包含参数
    print(request.method)  # 获取请求中使用的HTTP方式
    print(request.GET)  # 获取GET请求的参数
    print(request.META["HTTP_USER_AGENT"])  # 用户浏览器的user-agent字符串
    print(request.META["REMOTE_ADDR"])  # 客户端IO地址
    print(request.GET.get("username"))  # 获取get参数
    return HttpResponse("")


def url_reverse(request):
    # 使用reverse()方法反向解析
    print("在views()函数中使用reverse()方法解析的结果：" + reverse("app2_url_reverse"))
    return render(request, "app2/url_reverse.html")


def article_list(request, year):
    return HttpResponse("app2中的article_list方法，参数year，指定4位，值为" + str(year))


def article_page(request, page, key):
    return HttpResponse("app2中的article_page方法，参数page，任意数字，值为" + str(page)
                        + "参数key，字母数字下划线，值为" + key)


def index(request):
    return HttpResponse("app2中的index方法")


def show_uuid(request, id):
    return HttpResponse("app2中的show_uuid方法，参数为id,值为" + str(id))


def show_slug(request, q):
    return HttpResponse("app2中的show_slug方法，参数为id,值为" + str(q))

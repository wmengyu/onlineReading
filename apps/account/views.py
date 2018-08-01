from django.shortcuts import render, redirect

# Create your views here.
from apps.book.models import User


def login(request):
    if request.method == 'GET':
        return render(request, '../templates/include/home/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name and password:
            users = User.objects.filter(name=name)
            if users:
                user = users.first()
                if user.password == password:
                    #表示登录成功
                    userinfo = {
                        'uid': user.u_id,
                        'name': user.name,
                    }
                    request.session['userinfo'] = userinfo
                    return redirect('/book/index')
                else:
                    return render(request, '../templates/include/home/login.html', {'msg': '用户密码错误'})
            else:
                return render(request, '../templates/include/home/login.html', {'msg': '用户不存在,请注册'})
        else:
            return render(request, '../templates/include/home/login.html', {'msg': '用户名不能为空'})
    else:
        #其他错误的请求方式
        return render(request, '../templates/include/home/login.html', {'msg': '错误的请求方式'})

def logout(request):
    del request.session['userinfo']
    return redirect('/book/index')


def register(request):
    if request.method == 'GET':
         return render(request, '../templates/include/home/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password1')
        if name and password:
            users = User.objects.filter(name=name)
            if users:
                return render(request, '../templates/include/home/register.html', {'msg': '用户名已存在'})
            else:
                user = User.objects.create(name=name, password=password)
                user.save()
                return redirect('/book/index', {'msg':'返回首页登录'})
        else:
            return render(request, '../templates/include/home/register.html', {'msg': '注册信息不能为空'})

    else:
        return render(request, '../templates/include/home/register.html', {'msg':'错误的请求方式'})

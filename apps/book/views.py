from django.shortcuts import render, redirect

# Create your views here.
from apps.book.models import Upway, Nav, Sub, Produce, Review, Detail, Banner


def index(request):
    ways = Upway.objects.all()
    navigations = Nav.objects.all()
    #查询一级分类菜单数据
    sub_list = Sub.objects.all()
    #动态语言可以动态添加属性
    for sub in sub_list:
        #获取二级菜单的数据
        submenus = sub.submenu_set.all()
        sub.subs = submenus
    banners = Banner.objects.all()
    novels = Produce.objects.filter(img__startswith='xiaoshuo')
    return render(request, 'home.html', {'ways':ways, 'navigations':navigations,'sub_list':sub_list, 'banners':banners,
                                         'novels':novels})

#关键字搜索
def search(request):
    key = request.POST.get('keyword')
    books = Produce.objects.filter(title__icontains=key)
    return render(request, 'include/book/search.html',{'books':books})



#获取详细信息 查询数据库中的评论信息
def detail(request, pro_id):
    ways = Upway.objects.all()
    #通过主表查询子表信息
    pros= Produce.objects.filter(pro_id=pro_id)
    for pro in pros:
        pro.imgs = pro.detail_set.all()
        pro.count = pro.review_set.count()
    reviews = Review.objects.filter(pro_id=pro_id)


    if request.method == 'POST':
        # uid = request.POST.get(request.session._session['userinfo']['uid'])
        uid = request.session['userinfo']['uid']
        # name = request.POST.get('userinfo[name]')
        # pro_id = request.POST.get('pro_id')
        review_words = request.POST.get('review_words')
        review = Review.objects.create(user_id=uid, content=review_words, pro_id=pro_id)
        review.save()
    else:
        pass
    coments = Review.objects.all()
    for c in coments:
        print(c.content)
    # return redirect('/book/review/', {'coments':coments})
    return render(request, 'include/book/detail.html', {'ways':ways,'reviews':reviews, 'pros':pros, 'coments':coments})


# def review(request, pro_id):
#     if request.method == 'POST':
#         # uid = request.POST.get(request.session._session['userinfo']['uid'])
#         uid = request.session['userinfo']['uid']
#         # name = request.POST.get('userinfo[name]')
#         # pro_id = request.POST.get('pro_id')
#         review_words = request.POST.get('review_words')
#         review = Review.objects.create(user_id=uid, content=review_words, pro_id=pro_id)
#         review.save()
#     else:
#         pass
#     coments = Review.objects.all()
#     for c in coments:
#         print(c.content)
#     # return redirect('/book/review/', {'coments':coments})
#     return render(request, 'include/book/detail.html', {'coments':coments})


def add_cart(request, pro_id):

    return render(request, 'include/book/cart.html')
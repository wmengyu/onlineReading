from django.conf.urls import url

from apps.book import views

urlpatterns = [
    url('index/', views.index, name='index'),
    url('detail/(\d+)', views.detail, name='detail'),
    url('search/', views.search, name='search'),
    url('add_cart/(\d+)', views.add_cart, name='add_cart'),
    # url('review/(\d+)', views.review, name='review'),
]
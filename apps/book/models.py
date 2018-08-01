from django.db import models

# Create your models here.
#用户表
class User(models.Model):
    u_id = models.AutoField('ID',primary_key=True)
    name = models.CharField('用户', max_length=255, blank=True, null=True, unique=True)
    password = models.CharField('密码', max_length=255, blank=True, null=True, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

#轮播
class Banner(models.Model):
    id = models.AutoField('ID',primary_key=True)
    img = models.CharField('轮播图', max_length=255, blank=True, null=True)
    def __str__(self):
        return self.img
    class Meta:
        db_table = 'banner'
        verbose_name = '图片'


#导航表
class Nav(models.Model):
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'nav'
        verbose_name = '导航菜单'
        verbose_name_plural = '导航菜单管理'

#分类表
class Sub(models.Model):
    sub_id = models.AutoField('分类ID',primary_key=True)
    name = models.CharField('名称', max_length=255, db_index=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'sub'
        verbose_name = '分类菜单'
        verbose_name_plural = '分类菜单管理'

#观看方式
class Upway(models.Model):
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=255)
    class Meta:
        db_table = 'upway'


#父菜单
class SubMenu(models.Model):
    sub_menu_id = models.AutoField('ID', primary_key=True)
    name = models.CharField('名称', max_length=255, blank=True, null=True)
    sub = models.ForeignKey(Sub, db_column='sub_id', db_index=True,verbose_name='父菜单')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_menu'
        verbose_name = '一级菜单'
        verbose_name_plural = '一级菜单管理'

#二级菜单
class SubMenu2(models.Model):
    sub_menu2_id = models.AutoField('ID', primary_key=True)
    name = models.CharField('名称', max_length=255)
    sub = models.ForeignKey(Sub, db_column='sub_id', db_index=True,verbose_name='父菜单')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_menu2'
        verbose_name = '二级菜单'
        verbose_name_plural = '二级菜单管理'

#部分书表  主表
class Produce(models.Model):
    pro_id = models.AutoField('ID', primary_key=True)
    img = models.CharField('插图', max_length=255)
    title = models.CharField('标题', max_length=255)
    author = models.CharField('作者', max_length=255)
    product = models.CharField('简介', max_length=255)
    def __str__(self):
        return self.author

    class Meta:
        db_table = 'produce'
        verbose_name = '主编推荐'

#评论表(关联用户和书籍)
class Review(models.Model):
    review_id = models.AutoField('ID', primary_key=True)
    content = models.CharField('评论内容', max_length=255)
    create_date = models.DateTimeField('评论时间', auto_now=True)
    user = models.ForeignKey(User, db_column='u_id', db_index=True)
    pro = models.ForeignKey(Produce, db_column='pro_id', db_index=True)
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'review'
        verbose_name = '评论'

#详情表  与 Produce 呈一对一的关系  从表
class Detail(models.Model):
    d_id = models.AutoField('ID', primary_key=True)
    place = models.CharField('出自何地', max_length=255)
    type = models.CharField('类型', max_length=255)
    full_content = models.CharField('简介', max_length=255)
    pro = models.ForeignKey(Produce, db_column='pro_id', db_index=True)
    def __str__(self):
        return self.full_content

    class Meta:
        db_table = 'detail'
        verbose_name = '详情'


#订单表
class Order(models.Model):
    oder_id = models.AutoField('ID', primary_key=True)
    order_code = models.IntegerField()
    address = models.CharField('地址', max_length=255)
    receiver = models.CharField('接收人', max_length=255)
    mobile = models.IntegerField()
    user_message = models.CharField('买家信息', max_length=255)
    pay_time = models.DateTimeField(auto_now=True)
    uer = models.ForeignKey(User, db_column='u_id', db_index=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'order'
        verbose_name = '订单'


#购物车表(一个用户一个购物车->多条商品记录,一个购物车对应多条订单)
class Cart(models.Model):
    car_id = models.AutoField('ID', primary_key=True)
    number = models.IntegerField()
    pro = models.ForeignKey(Produce, db_column='pro_id', db_index=True)
    uer = models.ForeignKey(User, db_column='u_id', db_index=True)
    oder = models.ForeignKey(Order, db_column='oder_id', db_index=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'

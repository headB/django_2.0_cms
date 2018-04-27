1. 大概的流程
    1. 接收数据
        1. OK!现在去看看关于django的get和post先.毕竟好像和php的不一样.!
        2. OK!现在看了,应该可以了.好.继续.
    2. 加密
        1. 
    3. 创建对象(有什么用?)
    4. 完成后转向

2. 然后这个django是MTV模型,所以说,按步骤走了
    1. 首先写好model的一些派生类,或者先写view也可以,这里我先写好model.
        1. 前提是,记得先在settings.py里面**先注册刚刚创建的app**,例如我这里是login_admin
        2. 然后是在settings.py记得**设置数据库**什么的.!
        3. 然后记得在settings.py里面设置**加载模板的路径**.注意,推荐使用os.path.join这样的模式来拼接路径.!
    2. 然后再刚刚新建的app下面**新建urls.py.**
        1. 在这个urls.py里面,首先添加这些代码
        ```python
        from django.conf.urls import url
        from django.urls import path
        from  login_admin import views

        urlpatterns = [
            path('x',views.xx)

        ]
        ```
    3. 然后就是**修改项目里面的urls.py文件**
        1. 在里面的urlpattern里面添加
            path('xx',include('xx.urls'))
    
    4. 然后**修改app中的views.py内容了**
        1. 这里是定义视图里面的函数了,不用定义派生类.
        2. 一般性代码需要导入render,HttpResponse,Redirect
        3. 还有导入一下需要操作用到的model派生类.或者暴力一点可以直接from xx.models import *

    5. 然后是写一些关于models.py里面的一些派生类,这些每一个对应的派生类都是对应一个数据表的.!
        1. 记得就是写一个派生类的时候,记得都是继承(models.Model)

    6. 模板的话,其实可以写可以不写.
            
3. 现在的新问题是,path如何写正则呢?
    1. 但是先看看这个例子
        1. 代码
            ```python
            urlpatterns = [  
            path('articles/2003/', views.special_case_2003),  
            path('articles/<int:year>/', views.year_archive),  
            path('articles/<int:year>/<int:month>/', views.month_archive),  
            path('articles/<int:year>/<int:month>/<slug>/', views.article_detail),  
            ]  
            ```
    2. 不难看出,这个是利用分隔符去接收了一部分的数据,比如用一个<>从url中捕获值.**大概作者,觉得这种方式去匹配更加方便而且容易用把**
    3. 捕获值中可以包含一个转化器类型（converter type），比如使用 <int:name> 捕获一个整数变量。若果没有转化器，将匹配任何字符串，当然也包括了 / 字符。
    4. 无需添加前导斜杠。

4. 昨晚稍微尝试一下了templates,大概知道了可以直接在所在的app里面创建templates是直接可以使用的,
    但是一般操作都是在根目录底下,直接固定在这个templates文件里面,然后按app形式命名结构,就可以了.!好,现在继续去尝试一下做一个登陆的样式先.

5. 然后现在需要结合一下static和templates.
6. OK!templates还是统一管理的好吧,都可以,反正设置项也是很简单.
    1. **意思大概有两个使用templates的方式.**
        1. 直接在对应的app目录下面直接创建templates
        2. 可以到settings.py指定一个统一使用的templates
            1. 'DIRS': [os.path.join(BASE_DIR,'templates')],
7. 现在看看关于static的测试先.
    1. 
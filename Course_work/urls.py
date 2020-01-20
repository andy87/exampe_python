"""Course_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .controllers import controllerAccount, controllerViews, controllerAirtort, controllerOrder, controllerUser
from django.contrib import admin

urlpatterns = [

    # views
    url(r'^$', controllerViews.home, name='home_url'),
    url(r'^login/', controllerViews.login, name='login'),
    url(r'^logout/', controllerViews.logout, name='logout'),
    url(r'error/^$', controllerViews.error404),


    url(r'^admin/', admin.site.urls, name='admin'),

    # account
    url(r'^account/', controllerAccount.account, name='account'),

    # user
    url(r'^user_list/', controllerUser.user_list),
    url(r'^moderator_list/', controllerUser.moderator_list),
    url(r'^add_user/', controllerUser.add_user, name='add_user'),
    url(r'^add_mod/', controllerUser.add_mod, name='add_mod'),
    url(r'^list_del_user/', controllerUser.list_del_user, name='list_del_user'),
    url(r'del_user/(?P<user_id>\d+)', controllerUser.del_user1, name='del_user1'),

    # order
    url(r'order/add/', controllerOrder.add_order, name='order_add'),

    # airtort
    url(r'airport/(?P<air_id>\d+)', controllerAirtort.air_detail, name='air_detail_url'),
]

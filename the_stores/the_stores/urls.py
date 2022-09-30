from django.conf.urls import include,url
from django.contrib import admin
from racks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]

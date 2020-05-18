from django.urls import path,re_path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:id>',views.article_detail, name='article_detail'),
        path('year/<int:year>/', views.year_archive),
        path('<int:year>/<int:month>/', views.month_archive),
        path('<int:year>/<int:month>/<int:id>/', views.article_detail),
        path('add/',views.home, name='home'),
        re_path(r'^sum/.*',views.add, name='add'),
        path('form/',views.ajax),
        path('ajax/',views.jax),
        ]

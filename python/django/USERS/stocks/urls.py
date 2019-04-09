from django.urls import path
from . import views
from .views import *

urlpatterns = [

    # path('', views.index, name='index'),

    path('',StockListView.as_view(), name='stock_list'),
    path('<slug:stock_name>',StockDetailView.as_view(),name='stock_detail'),
    #path('/chart/api/data/<slug:stock_name>',StockDetailView.as_view(),name='stock_detail'),
    #path('api/data',views.get_data, name='api-data'),
    path('api/chart/data',ChartData.as_view()),

    

    




    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    # path('all_users', views.all_users, name='all_users'),
    # path('user_details/<str:username>', views.user_details, name='user_details'),
    # path('edit/<str:username>', views.edit, name='edit'),

]

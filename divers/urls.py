from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.SiteList.as_view(), name='site_list'),
    path('sites/<int:pk>', views.SiteDetail.as_view(), name='site_detail'),
    path('log/', views.LogList.as_view(), name='log_list'),
    path('log/<int:pk>', views.LogDetail.as_view(), name='log_detail')
]
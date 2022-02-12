from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.SiteList.as_view(), name='site_list'),
    path('sites/<int:pk>', views.SiteDetail.as_view(), name='site_detail'),
    path('visitor/', views.VisitorList.as_view(), name='visitor_list'),
    path('visitor/<int:pk>', views.VisitorDetail.as_view(), name='visitor_detail')
]
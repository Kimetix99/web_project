from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band/create', views.CreateBandView.as_view(), 
        name='band_create'),
    path('band/<int:pk>', views.BandDetail.as_view(),
        name='band_detail'),
    path('establishment/', views.ListEstablishment.as_view(),
        name='establishment_list')
]

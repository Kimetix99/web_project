from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band/', views.ListBand.as_view(), name='band_list'),
    path('band/create', views.CreateBandView.as_view(), 
        name='band_create'),
    path('band/<int:pk>', views.BandDetail.as_view(),
        name='band_detail'),
    path('establishment/create', views.CreateEstablishmentView.as_view(),
        name='establishment_create'),
    path('establishment/', views.ListEstablishment.as_view(),
        name='establishment_list'),
    path('event/', views.ListEvent.as_view(),
        name='event_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band/', views.ListBand.as_view(), name='band_list'),
    path('band/create', views.CreateBandView.as_view(), 
        name='band_create'),
    path('band/<int:pk>', views.BandDetail.as_view(),
        name='band_detail'),
    path('establishment/', views.ListEstablishment.as_view(),
        name='establishment_list'),
    path('establishment/<int:pk>', views.EstablishmentDetail.as_view(),
        name='establishment_detail'),
    path('event/', views.ListEvent.as_view(),
        name='event_list'),
    path('event/delete/<int:pk>', views.DeleteEvent.as_view(),
        name='event_delete'),
    path('event/<int:pk>', views.EventDetail.as_view(),
        name='event_detail'),
    path('band/delete/<int:pk>', views.DeleteBand.as_view(),
        name='band_delete'),
]

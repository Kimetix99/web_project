from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band/', views.ListBand.as_view(), name='band_list'),
    path('band/create', views.CreateBandView.as_view(), 
        name='band_create'),
    path('band/edit/<int:pk>', views.EditBandView.as_view(),
         name='band_edit'),
    path('band/<int:pk>', views.BandDetail.as_view(),
        name='band_detail'),
    path('establishment/', views.ListEstablishment.as_view(),
        name='establishment_list'),
    path('establishment/edit/<int:pk>', views.EditEstablishmentView.as_view(),
        name='establishment_edit'),
    path('establishment/<int:pk>', views.EstablishmentDetail.as_view(),
        name='establishment_detail'),
    path('event/', views.ListEvent.as_view(),
        name='event_list'),
    path('event/<int:pk>', views.EventDetail.as_view(),
        name='event_detail'),
    path('event/edit/<int:pk>', views.EditEventView.as_view())
]

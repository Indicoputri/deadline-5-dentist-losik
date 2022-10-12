from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('doktergigi', views.doktergigi, name = 'doktergigi'),
    path ('updatedatadoktergigi/<str:id>', views.updatedatadoktergigi, name = 'updatedatadoktergigi'),     
    path('pasien', views.pasien, name = 'pasien'),
    path('createdatapasien',views.createdatapasien,name='createdatapasien'),
    path('updatedatapasien/<str:id>', views.updatedatapasien, name = 'updatedatapasien'),
    path('deletedatapasien/<str:id>',views.deletedatapasien,name='deletedatapasien'),
    path('pelayanan', views.pelayanan, name = 'pelayanan'),
    path('createdatapelayanan',views.createdatapelayanan,name='createdatapelayanan'),
    path('updatedatapelayanan/<str:id>', views.updatedatapelayanan,name = 'updatedatapelayanan'),
    path('deletedatapelayanan/<str:id>',views.deletedatapelayanan,name='deletedatapelayanan'),
    path('pendaftaran',views.pendaftaran,name='pendaftaran'),
    path('createdatapendaftaran',views.createdatapendaftaran,name='createdatapendaftaran'),
    path('updatedatapendaftaran/<str:id>', views.updatedatapendaftaran,name = 'updatedatapendaftaran'),
    path('detailpelayanan',views.detailpelayanan,name='detailpelayanan'),
    path('createdatadetailpelayanan',views.createdatadetailpelayanan,name='createdatadetailpelayanan'),
    path('updatedatadetailpelayanan/<str:id>', views.updatedatadetailpelayanan,name = 'updatedatadetailpelayanan')
]
from django.urls import path
from .views import index,viewDisco,viewInstrum,discoAdd,discoDelete,discoEdit,instrumAdd

urlpatterns = [
    path('index', index, name="index"),
    path('viewdisco', viewDisco, name="viewdisco"),
    path('viewinstrum', viewInstrum, name="viewinstrum"),
    path('discoadd',discoAdd, name="discoadd"),
    path('discoedit/<str:pk>', discoEdit, name='discoedit'),
    path('discodelete/<str:pk>', discoDelete, name='discodelete'),
    path('instrumadd',instrumAdd,name='instrumadd'),
]
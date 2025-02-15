from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('delete/<int:item_id>/',views.delete_item,name="delete"),
    path('logout/',views.logout_view,name='logout')
]
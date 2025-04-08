from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.MenuItemView.as_view(), name='table-list'),
    path('menu/<int:pk>/', views.MenuItemSingleView.as_view()),
    path('booking/', views.BookingList.as_view(), name='booking-list'),
    path('booking/<int:pk>', views.BookingSingleView.as_view())
]


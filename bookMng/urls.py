from django.urls import path
from . import views
from .views import remove_book

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('remove_book/<int:book_id>/', remove_book, name='remove_book'),
    path('messages', views.messages, name='messages'),
    path('search', views.search, name='search'),
    # Updated line for viewing the cart
    path('add_to_cart/<int:book_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.index, name='library_app-index'),
    path('books/<int:book_id>/', views.show, name='library_app-show'),
]

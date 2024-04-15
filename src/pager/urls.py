from django.urls import path
from . import views  # Убедитесь, что этот импорт соответствует вашему расположению views.py

urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]

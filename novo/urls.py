from django.urls import path
from .  import views

urlpatterns = [
    
    path('', views.contato_list, name="contato-list"),
    path('criar/', views.create, name="contato-create"),
    path('<int:pk>/update/', views.update, name="contato-update"),
    path('<int:pk>/delete/', views.delete, name="contato-delete")
]
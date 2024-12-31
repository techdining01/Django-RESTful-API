from django.urls import path
from . import views


urlpatterns = [
path('todos/', views.TodosListCreate.as_view()),
path('todos/<int:pk>/', views.TodosRetrieveUpdateDestroy.as_view()),
path('todos/<int:pk>/complete/', views.TodoToggleComplete.as_view()),
path('signup/', views.signup),
]


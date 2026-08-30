from django.urls import path

from .views import index, TodoItemDetailView
from .views import CreateTodoItemView, ViewTodoItems, TodoItemDeleteView
app_name = "todo"

urlpatterns = [
    path("", index, name="index"),
    path("create/", CreateTodoItemView.as_view(), name="create"),
    path("list/", ViewTodoItems.as_view(), name="list"),
    path("<int:pk>/", TodoItemDetailView.as_view(), name="detail" ),
    path("<int:pk>/delete/", TodoItemDeleteView.as_view(), name="delete"),
]


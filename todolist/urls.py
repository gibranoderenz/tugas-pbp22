from django.urls import path
from todolist import views

app_name = "todolist"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("create-task/", views.create_task, name="create_task"),
    path("toggle-task/<int:id>", views.toggle_task, name="toggle_task"),
    path("delete-task/<int:id>", views.delete_task, name="delete_task"),
    path("json/", views.get_json_todolist, name="json"),
    path("add/", views.create_task_ajax, name="create_task_ajax"),
    path("delete/<int:id>", views.delete_task_ajax, name="delete_task_ajax"),
]

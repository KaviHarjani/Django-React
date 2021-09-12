from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("", apioverview, name="api-overview"),
    path("task-list/", taskList, name="task-list"),
    path("task-create/", taskCreate, name="task-create"),
    path("task-update/<int:pk>/", taskUpdate, name="task-update"),
    path("task-delete/<int:pk>/", taskDelete, name="task-delete"),
    path("task-detail/<int:pk>/", taskDetail, name="task-detail"),
]

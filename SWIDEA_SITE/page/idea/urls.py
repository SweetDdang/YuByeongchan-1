from django.urls import path
from . import views

app_name = "idea"

urlpatterns = [
    path('', view=views.idea_list, name='idea_list'),
    path('<int:pk>/', view=views.idea_detail, name='idea_detail'),
    path('create/', view=views.idea_create, name='idea_create'),
    path('<int:pk>/update/', view=views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', view=views.idea_delete, name='idea_delete'),
    path('dev/', view=views.dev_list, name='dev_list'),
    path('dev_create/', view=views.dev_create, name='dev_create'),
    path('<int:pk>/dev_detail/', view=views.dev_detail, name='dev_detail'),
    path('<int:pk>/dev_update/', view=views.dev_update, name='dev_update'),
    path('<int:pk>/dev_delete/', view=views.dev_delete, name='dev_delete'),
]


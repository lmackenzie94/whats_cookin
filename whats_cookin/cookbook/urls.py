# have to manually create this file

from django.urls import path

from . import views

# allows Django to differentiate the URL names between multiple apps in a given project
app_name = 'cookbookNamespace'
# this maps the view to a URL
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /cookbook/5/
    path('recipes/add', views.add, name='add'),

    path('recipes/<int:recipe_id>/', views.detail, name='detail'),
]

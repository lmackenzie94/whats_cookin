# have to manually create this file

from django.urls import path

from . import views

# this maps the view to a URL
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /cookbook/5/
    path('<int:recipe_id>', views.detail, name='detail')
]

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.template import loader


def index(request):
    # latest_recipes = Recipe.objects.order_by('-pub_date')[:5]
    # context = {
    #     'latest_recipes': latest_recipes
    # }
    # return render(request, 'cookbook/index.html', context)
    latest_recipe = Recipe.objects.all()[:5]
    template = loader.get_template('cookbook/index.html')
    context = {
        'latest_recipe': latest_recipe,
    }
    return HttpResponse(template.render(context, request))


# these two routes take an argument
def detail(request, recipe_id):
    # try:
    #     recipe = Recipe.objects.get(pk=recipe_id)
    # except Recipe.DoesNotExist:
    #     raise Http404("Oops, looks like that recipe does not exist.")
    # return render(request, 'cookbook/detail.html', {'recipe': recipe})

    # SHORTCUT
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'cookbook/detail.html', {'recipe': recipe})


def results(request, recipe_id):
    response = "You're looking at the results of recipe %s."
    return HttpResponse(response % recipe_id)

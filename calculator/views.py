from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request, recipe1):
    d = request.GET.get("servings", "")

    if d:
        name_recipe = recipe1
        dish = {}
        dish.clear()
        for ing, amount in DATA[name_recipe].items():
            dish[ing] = amount * int(d)
            DATA[name_recipe].update(dish)
        # name_recipe = recipe1
        print(dish)
        context = {
            "recipe": DATA[name_recipe]
        }
    else:
        name_recipe = recipe1
        context = {
            "recipe": DATA[name_recipe]
        }

    return render(request, template_name="calculator/index.html", context=context)

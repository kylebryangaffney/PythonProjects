from django.shortcuts import render

def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    names = ["Token", "Grinch", "Crow", "JR", "Hesher", "Crane"]
    ctx = {
        "products": products,
        "names": names,
    }

    
    return render(request, "home.html", ctx)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.models import Page
import json
# Import the Category model
from rango.models import Category

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):
    if request.POST:
        user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
        user.save()

        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        print("login")
        redirect("about")

    return render(request, 'rango/register.html', {})


def login_view(request):
    message = ""

    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                print("Redirect to a success page.")
                redirect("about")
            else:
                # Return a 'disabled account' error message
                message = "Inactive User"
        else:
            # Return an 'invalid login' error message.
            message = "Invalid Login"

    return render(request, 'rango/login.html', {"message": message})


def data_categories(request):
    output = []
    for c in Category.objects.all():
        output.append({"id": c.id, "name": c.name})
    return HttpResponse(json.dumps(output, indent=4), content_type='application/json')


def data_pages(request):
    output = []
    for p in Page.objects.all():
        output.append({"id": p.id, "title": p.title, "url": p.url, "category_id": p.category.id})
    return HttpResponse(json.dumps(output, indent=4), content_type='application/json')


def data_all(request):
    output = []
    page_list = Page.objects.all()

    for p in page_list:
        output.append({
            "id": p.id, "title": p.title, "url": p.url,
            "category": {
                "id": p.category.id, "name": p.category.name
            }
        })
    return HttpResponse(json.dumps(output, indent=4), content_type='application/json')


def main(request):
    return render(request, 'main.html', {})



def create_page_and_category_example(request):
    # Page(title='new dj page', category=Category.objects.get(name='Django')).save()
    c = Category.objects.get(name='Django')
    p = Page()
    p.title = 'new dj page'
    p.category = c
    p.save()

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def category(request, category_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
    

    
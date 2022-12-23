from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A View that renders the bags content """
    
    return render(request, 'bag/bag.html')
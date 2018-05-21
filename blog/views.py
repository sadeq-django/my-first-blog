from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def browse_page(request):
    return render(request, 'blog/browse_page.html', {})
    
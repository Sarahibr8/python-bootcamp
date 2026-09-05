from django.shortcuts import render

def post_list(request):
    return render(request, 'post_list.html')

def post_detail(request, post_id):
    return render(request, 'post_detail.html', {'post_id': post_id})

def category(request, category_name):
    return render(request, 'category.html', {'category_name': category_name})
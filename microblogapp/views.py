from django.shortcuts import render

def post_list(request):
    return render(request, 'microblogapp/post_list.html', {})

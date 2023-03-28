from django.shortcuts import render

def render_cv(request):
    return render(request, 'cv.html')


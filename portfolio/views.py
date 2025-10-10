from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')


def portfolio(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'portfolio/portfolio.html', {'projects': projects})


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tags = project.tags.split(',')
    return render(request, 'portfolio/detail.html', {'project': project, 'tags':tags})


def cover_letter(request):
    return render(request, 'portfolio/cover_letter.html')


def resume(request):
    return render(request, 'portfolio/resume.html')


def contact(request):
    return render(request, 'portfolio/contact.html')


def error_404_view(request, exception):
    return render(request, 'portfolio/404.html')


# def error_500_view(request, exception):
#     return render(request, 'portfolio/500.html')
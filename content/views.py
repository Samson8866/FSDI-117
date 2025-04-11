from django.shortcuts import get_object_or_404, render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.

def projects_list_view(request):

    projects = Project.object.all().order_by('-year')

    return render(request, "content/projects_list.html", {"projects": projects})



def project_new_view(request):
    form = ProjectForm()

    return render(request,"content/project_new.html", {"form": form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects_list')
    
    return render(request, 'content/project_delete_conformation.html', {'project': project})

def project_new_view(request):

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect("projects_list")
        else:
            form = ProjectForm()

        return render(request, "content/project_new.html"), {"form":form}
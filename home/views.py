from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from home.models import Task

# Create your views here.
def home(request):
    try:
        if request.method == "POST":
            if "title" in request.POST:
                title = request.POST.get("title")
                desc = request.POST.get("desc")
                
                # Check for empty title or description
                if not title or not desc:
                    messages.error(request, "Empty fields!")
                else:
                    ins = Task(taskTitle=title, taskDesc=desc)
                    ins.save()
                    messages.success(request, "Task added successfully!")

            elif "task_id" in request.POST:
                task_id = request.POST.get("task_id")
                task = get_object_or_404(Task, id=task_id)
                task.completed = not task.completed
                task.save()
                messages.info(request, "Task status updated!")

            elif "delete_task_id" in request.POST:
                delete_task_id = request.POST.get("delete_task_id")
                task = get_object_or_404(Task, id=delete_task_id)
                task.delete()
                messages.warning(request, "Task deleted successfully!")

            return redirect('/')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('/')

    search_query = request.GET.get('search', '')
    if search_query:
        allTasks = Task.objects.filter(taskTitle__icontains=search_query)
    else:
        allTasks = Task.objects.all()

    context = {'tasks': allTasks}
    return render(request, 'index.html', context)

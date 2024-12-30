from django.shortcuts import redirect, render, get_object_or_404
from home.models import Task

# Create your views here.
def home(request):

    if request.method == "POST":
        
        if "title" in request.POST:
            title = request.POST.get("title")
            desc = request.POST.get("desc")
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            context = {'success': True}
            
        elif "task_id" in request.POST:  
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            task.completed = not task.completed
            task.save()
            
            
        elif "delete_task_id" in request.POST:  
            delete_task_id = request.POST.get("delete_task_id")
            task = get_object_or_404(Task, id=delete_task_id)
            task.delete()
            context = {'success': True, 'message': 'Task deleted successfully!'}
            
        return redirect('/')

    search_query = request.GET.get('search', '')
    if search_query:
        allTasks = Task.objects.filter(taskTitle__icontains=search_query)
    else:
        allTasks = Task.objects.all()

    context = {'success': False, 'tasks': allTasks}
    return render(request, 'index.html', context)

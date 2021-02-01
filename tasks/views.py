from django.shortcuts import render,redirect

from .forms import TaskForm

from .models import Task

from django.contrib.auth.decorators import login_required

# Create your views here.

# def home(request):
# 	form = TaskForm()

	

# 	if request.method == 'POST':
# 		entry = TaskForm(request.POST)
# 		if entry.is_valid():
# 			entry.save()
# 		return 	redirect ('/')

# 	tasks = Task.objects.all()

# 	context = {
# 		'tasks' : tasks,
# 		'form' : form,
# 	}

# 	return render(request,'tasks/home.html',context)


def home(request,id=0):
	if request.method == 'GET':

		if id == 0:
			form = TaskForm()
		else:
			entry = Task.objects.get(pk=id)
			form = TaskForm(instance=entry)

	else:
		if id == 0:
			form = TaskForm(request.POST)

		else:
			entry = Task.objects.get(pk=id)
			form = TaskForm(request.POST,instance=entry)

		if form.is_valid():
			form.save()

		return redirect('/home')

	tasks = Task.objects.all()

	context = {
		'form' : form,
		'tasks' : tasks,
	}

	return render(request,'tasks/home.html',context)

def deleteEntry(request,id):

	task = Task.objects.get(pk=id)


	if request.method == 'POST':
		task.delete()

		return redirect('/home')

	return render(request,'tasks/delete.html',{'task':task})

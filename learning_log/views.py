from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
	"""The home page for Learning Log."""
	return render(request, 'learning_log/index.html')
	
def topics(request):
	"""Show all topics"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_log/topics.html', context)
	
def topic(request, topic_id):
	#Show a single topic and all its entries
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_log/topic.html', context)
	
def new_topic(request):
	"""Add a new topic."""
	if request.method !='POST':
		#No data submitted; create a blank form.
		form = TopicForm()
	else:
		#POST date submitted; process data.
		form = TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_log:topics')
	#Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'learning_log/new_topic.html', context)
	
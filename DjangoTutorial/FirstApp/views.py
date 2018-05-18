from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
	now = datetime.now()

	return render(
		request,
		"FirstApp/index.html", #Relative path from the 'templates' folder to the template file.
		{
			'title' : "First App!",
			'content' : "Hello Django! on " + now.strftime("%A, %d, %B, %Y, at %X"),
			'message' : "Welcome to your first Django App"
		}
	)

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from list.models import Task_models
def create(request):
    try:
        if request.method == 'POST':
            title request.data['title']
            description =  request.data.get('description','no description')
            completiondate = datetime.strptime(request.data['completion date'],'%d/%m/%y %H:%M')
            priority = request.date['priority']
            Task_models.object.create(title=title, description = description, completiondate = completiondate ,priority = priority)
    except Exception:
        pass
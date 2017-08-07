from django.shortcuts import render,get_object_or_404
from .models import Question

def index(request):
	x=Question.objects.order_by('-date')
	context={'questions':x}
	return render(request,'polls/index.html',context)
def detail(request,qid):
	x=get_object_or_404(Question,pk=int(qid))
	context={'q':x}
	return render(request,'polls/detail.html',context)
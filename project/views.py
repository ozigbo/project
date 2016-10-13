from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404, render
from django.views     import generic


from .models import Question,Choice

# Create your views here.

#def index(request):
    #return HttpResponse("Hello, world. You're at the project index.")
#def index(request):
#    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output =', '.join([q.question_text for q in latest_question_list])
#      return HttpResponse(output)
#    context ={'latest_question_list':lastest_question_list}
#    return render (request,'project/index.html',context)

#leave the rest of the views (detail,results,vote) unchanged

class IndexView(generic.ListView):
      template_name ='project/index.html'
      context_object_name = 'lastest_question_list'
      
      def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by ('-pub_date')[:5]

class  DetailView(generic.DetailView):
       model=Question
       template_name= 'project/detail.html'
       
class  ResultsView(generic.DetailView):
       model=Question
       template_name='project/results.html'
 
def detail(request ,question_id):
        question =get_object_or_404(Question, pk=question_id)
        #try:
        # question=Question.objects.get(pk=question_id)
        #except Question.DoesNotExist:
         #  raise Http404("Question does not exist")
        return render( request,'project/detail.html',{'question': question})
    #return HttpResponse("You' re looking at question %s." % question_id)
    
def results(request,question_id):
         #response ="You're looking at the results of question %s."
         question =get_object_or_404(Question,pk=question_id)
         return render(request,'project/results.html',{'question':question})
     
def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
       selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(keyError,Choice.DoesNotExist):
       # Redisplay the question voting form.
       return render(request, 'project/detail.html',
              {'question': question,
               'error_message':"You didn't select a choice.",
              })
    else:
         selected_choice.votes +=1
         selected_choice.save()
         #Always return an httpResonseRedirect after successfully dealing
         #with POST data. This prevents data from being posted twice if a
         #user hits the back button.
         return HttpResponseRedirect(reverse('project:results',args=(question.id,)))
    #return HttpResponse("You're voting on question %s." %  question_id)

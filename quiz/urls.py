from django.urls import path
from quiz.views import Quiz , RandomQuestion , QuizQuestion

app_name= 'quiz'
urlpatterns = [
    
    path('' , Quiz.as_view() , name = 'quiz'),
    #path('question/random/' , RandomQuestion.as_view() , name = 'random_question')
    path('r/<str:topic>/' , RandomQuestion.as_view() , name = 'random_question') , 

    path('q/<str:topic>/' , QuizQuestion.as_view() , name = 'quiz_questions')
  

]

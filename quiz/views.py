from rest_framework import generics , status
from quiz.models import Quizzes, Question
from quiz.serializers import QuizSerializer , RandomQuestionSerializer , QuestionSerializer
from rest_framework.views import APIView    
from rest_framework.response import Response
# Create your views here.


class Quiz (generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):

    def get (self,request , format = None ,**kwargs) :
        try : 
            question = Question.objects.filter(quiz__title = kwargs['topic']).order_by('?')[:1]
            serializer = RandomQuestionSerializer(question , many = True)  # Many Answers associated with one question !!
          
          
            if  not serializer.data:
                 errorMessage =  "No Quizzes Associated with this Topic" +  kwargs['topic']
                 return Response({'Message' :  errorMessage } ,status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data , status = status.HTTP_200_OK)

        except :      
            return Response(  {"Message" : "Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)
        



class QuizQuestion(APIView):
    def get (self  , request , format = None , ** kwargs):
        question = Question.objects.filter(quiz__title = kwargs['topic'])
        serializer = QuestionSerializer(question , many= True)
        
        
        return Response(serializer.data , status = status.HTTP_200_OK)



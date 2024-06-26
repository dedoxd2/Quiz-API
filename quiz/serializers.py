from rest_framework import serializers
from quiz.models import Quizzes , Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Quizzes
        fields = [ 'title' , 'category']




class AnswerSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Answer
        # fields  = '__all__'
        fields = ['id' , 'answer_text' , 'is_right' , ] 


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True , read_only = True)
    class Meta : 
        model = Question
      #  fields = '__all__'
        fields = ['title' , 'answer']



class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True , read_only = True)
    quiz = QuizSerializer( read_only = True)
    class Meta : 
        model = Question
      #  fields = '__all__'
        fields = ['quiz','title' , 'answer' ]

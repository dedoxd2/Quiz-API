from django.contrib import admin
from quiz.models import Category , Quizzes , Question , Answer
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , ]


@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text' , 'is_right' , ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title' , 'quiz']
    list_display = ['date_updated' , 'title' , 'quiz']

    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text' , "is_right" , "question"]

# TabularInline
# StackedInline

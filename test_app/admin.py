from django.contrib import admin
from .models import Question, Test, MyUser


class CustomQuestion(admin.ModelAdmin):
    fieldsets = (
        ('main', {
            'fields': ('question_text',),
        }),
        ('Answer 1:', {
            'fields': (('used_1', 'ans_1','right_1', 'points_1'),),
        }),
        ('Answer 2:', {
            'fields': (('used_2', 'ans_2','right_2', 'points_2'),),
        }),
        ('Answer 3:', {
            'fields': (('used_3', 'ans_3','right_3', 'points_3'),),
        }),
        ('Answer 4:', {
            'fields': (('used_4', 'ans_4','right_4', 'points_4'),),
        }),
        ('Answer 5:', {
            'fields': (('used_5', 'ans_5','right_5', 'points_5'),),
        }),
    )


admin.site.register(MyUser)
admin.site.register(Test)
admin.site.register(Question, CustomQuestion)

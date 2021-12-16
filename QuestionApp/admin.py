from django.contrib import admin

from .models import Choice, Question, Vote, Comment

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

class ReadOnlyMixin:
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
class VoteAdmin(ReadOnlyMixin, admin.ModelAdmin):
    list_display = ('voter_name', 'vote_date', 'choice')
admin.site.register(Vote, VoteAdmin)

class CommentAdmin(ReadOnlyMixin, admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)
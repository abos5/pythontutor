"""admin ctrls
"""
from django.contrib import admin
from polls.models import Question, Choice
from tutor.models import Person, Group, Membership
from tutor.models import Monkey, Male2
from webblog.models import Blog, Entry, Author
admin.AdminSite.site_header = "Abos Work Arround"
admin.AdminSite.site_title = "Abos Work Arround"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class GroupInline(admin.TabularInline):
    model = Group
    extra = 2


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('pub date', {
            'fields': ['pub_date'],
            'classes': ['collapse'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', ]
    search_fields = ['question_text']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None, {'fields': ['members']}),
    ]
    inlines = [MembershipInline]


@admin.register(Male2)
class Male2Admin(admin.ModelAdmin):
    pass


@admin.register(Monkey)
class MonkeyAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass

# Register your models here.

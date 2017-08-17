from django.contrib import admin
from main.models import Category, Content, ContentImage, Program
from django import forms
from django.forms import SelectMultiple, CheckboxSelectMultiple


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']


class PropertyImageInline(admin.TabularInline):
    fields = ('image_tag', 'image', 'sort')
    readonly_fields = ('image_tag',)
    model = ContentImage
    extra = 0

from django.forms import ModelForm, Textarea


class ContentForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}))

    class Meta:
        model = Content
        # fields = ('img', 'title', 'desc')
        # widgets = {
        #     'desc': Textarea(attrs={'cols': 80, 'class': 'ssssssss'}),
        # }
from django.forms import TextInput, Textarea
from django.db import models


class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 80})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    list_display = ['title', 'image_tag', 'video_tag']
    inlines = [PropertyImageInline, ]
    fields = ('title', 'desc', 'img', 'image_tag',
              'video', 'category', 'general_slider', 'news_line', 'publish_date', 'hit_count')
    readonly_fields = ('image_tag',)
    form = ContentForm

    def get_queryset(self, request):
        qs = super(ContentAdmin, self).get_queryset(request)
        return qs

    class Media:
        js = (
            '/static/main/js/tinymce/js/tinymce/tinymce.js',
            '/static/main/js/textareas.js',
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Content, ContentAdmin)
# Register your models here.


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

UserAdmin.list_display = ('email', 'first_name', 'last_name',
                          'is_active', 'date_joined', 'is_staff')

UserAdmin.fieldsets = (
    (None, {'fields': ('username', 'password')}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    ('Permissions', {'fields': ('is_staff', 'groups')}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
)

# admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

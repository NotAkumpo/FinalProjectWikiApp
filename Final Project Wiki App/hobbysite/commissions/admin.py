from django.contrib import admin

from .models import Commission, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInLine,]

    search_fields = ['title',]
    list_display = ['title', 'peopleRequired',]
    list_filter = ['title', 'peopleRequired',] 


class CommentAdmin(admin.ModelAdmin):
    model = Comment

    search_fields = ['commission',]
    list_display = ['commission',]
    list_filter = ['commission',] 


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
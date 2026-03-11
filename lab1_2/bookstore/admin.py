from django.contrib import admin
from .models import Book, Author, Genre

class BookAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('title',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
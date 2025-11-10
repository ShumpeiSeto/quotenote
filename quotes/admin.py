from django.contrib import admin
from .models import Quote, Book, Tag, Connection

# Register your models here.
admin.site.register(Quote)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Connection)

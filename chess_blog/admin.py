from django.contrib import admin
from .models import CustomUser, ChessCategory, ChessPost, ChessComment

admin.site.register(ChessCategory)
admin.site.register(CustomUser)
admin.site.register(ChessPost)
admin.site.register(ChessComment)
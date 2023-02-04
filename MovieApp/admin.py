from django.contrib import admin
from MovieApp.models import Movies
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['releasedate','moviename','actor','actress','ratings']
admin.site.register(Movies,MoviesAdmin)
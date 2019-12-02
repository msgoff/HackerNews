from django.contrib import admin
from django.urls import path
from main.views import StoriesView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',StoriesView.as_view()),
]

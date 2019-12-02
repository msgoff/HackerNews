from django.views.generic import ListView
from django.shortcuts import render
from main.models import Stories


class StoriesView(ListView):
    model = Stories
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

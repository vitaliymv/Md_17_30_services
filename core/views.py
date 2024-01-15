from django.shortcuts import render
from django.views.generic import TemplateView

from core.services import generate_data


# Create your views here.
class RecordsView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = generate_data()
        return context

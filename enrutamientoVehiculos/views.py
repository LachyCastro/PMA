from django.shortcuts import render, redirect
from enrutamientoVehiculos.models import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from django.contrib import messages
from enrutamientoVehiculos.ir_logic.load import charge_corpus
from enrutamientoVehiculos.ir_logic.vectorial_model import vectorial_model
# Create your views here.


def index(request):
    return render(request, 'index.html')


class DocumentList(ListView):
    model = Publication

    def get(self, request: HttpRequest) -> HttpResponse:

        doc = Publication.objects.all()

        return render(request, 'documents.html', {'object_list': doc})


class IRDocumentList(ListView):

    def get(self, request: HttpRequest) -> HttpResponse:

        resource = []
        if "charge" in request.GET:
            charge_corpus()
            messages.add_message(request, 25, "charge corpus done!")
            return redirect("documents_rec")
        elif "search" in request.GET:
            try:
                query = request.GET["query"]
                resource = vectorial_model(query)
            except Exception:
                messages.add_message(request, 40, "Error in search")
                return redirect("documents_rec")

        return render(request, 'documents_rec.html', {'object_list': resource})

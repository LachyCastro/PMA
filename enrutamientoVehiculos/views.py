from django.shortcuts import render
from enrutamientoVehiculos.models import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from enrutamientoVehiculos.ir_logic import vectorial_model
# Create your views here.
def index(request):
    return render(request, 'index.html')

class DocumentList(ListView):
    model = Publication
    def get(self, request : HttpRequest) -> HttpResponse:
        doc = Publication.objects.all()

        return render(request,'documents.html', {'object_list': doc})

class IRDocumentList(ListView):

    def get(self, request: HttpRequest) -> HttpResponse:
        # para saber luego q modelo aplicar
        # type_query = request.GET["choices-single-defaul"]
        # query = request.GET["search"]  # Consulta desde la web
        #resource = []
        #if (type_query == "Vectorial"):
        #resource = vectorial_model("")
        return render(request, 'documents_rec.html', {'document_list': []})
        
        
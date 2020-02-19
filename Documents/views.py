from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Document
# Create your views here.


def index(req):
    latest_documents = Document.objects.order_by('-pub_date')[:5]
    data = {'latest_documents': latest_documents}
    return render(req, 'Documents/index.html', data)


def detail(req, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(req, 'Documents/detail.html', {'document': document})


def post(req, document_id):
    return render(req, 'Documents/post.html')
from django.db.models import F, FloatField
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Book
from django.db.models.functions import Coalesce
from .forms import BookForm



# index sehinde yazilanlar
def index_view(request):
    context={
        "text":"Salam necesen?",
        "new":Book.objects.all()
        # "text":Book.objects.all()
    }
    return render(request, "index.html", context)


# list sehifesinde yazilanlar
def list_view(request):
    context={
        "books":Book.objects.all()
    }
    return render(request, "list.html", context)


# detail sehifesinde yazilanlar
def detail_view(request, id):
    bookdetail= Book.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount")
    ).get(id=id)

    context={
        "bookdetail": bookdetail
    }
    return render(request, "detail.html", context)


# create sehifesinde yazilanlar
def create_view(request):
    form=BookForm()

    if request.method=="POST":
        form = BookForm(request.POST) #modelin ozundeki validationlari getirir
        if form.is_valid():
            form.save() #datani validationdan kecenleri melumati create edib databasaya elave edecek
        # print(request.POST)
        return redirect('list')

    context={
        "form":form
    }
    return render(request,"create.html", context)



def update_view(request,id):
    book = get_object_or_404(Book, id=id)
    form = BookForm()
    context={}
    return render(request, 'update.html', context)
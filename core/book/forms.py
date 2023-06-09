from django import forms
from .models import Book

# class BookForm(forms.Form):
#     name= forms.CharField()
#     description= forms.CharField()
#     price=forms.FloatField()




class BookForm(forms.ModelForm):

    # category=forms.CharField()
    class Meta:
        model =Book
        fields = ['name','description','price']
        exclude=["description"]   #bunu silir formdan
        fields ='__all__'   #butun fieldleri getiri

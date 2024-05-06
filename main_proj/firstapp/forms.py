from django import forms
from table.models import *

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"id":"title"}))
    # image = forms.image(widget=forms.FileInput(attrs={"id":"pim"}))
    descrption = forms.CharField(widget=forms.Textarea(attrs={"id":"desc"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"id":"price"}))
    day=forms.DecimalField(widget=forms.NumberInput(attrs={"id":"day"}))
    # sdate = forms.DateField(widget=forms.DateInput(attrs={"id":"desc"}))
    # edata = forms.DateField(widget=forms.DateInput(attrs={"id":"desc"}))

    class Meta:
        model = Product
        fields = ['title','descrption','price']

class ImageForm(forms.ModelForm):

    class Meta:
        model = ProductImages
        fields = ['images']

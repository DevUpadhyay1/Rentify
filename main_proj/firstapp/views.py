from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from table.models import *
from firstapp.forms import *
from django.views import View

# Create your views here.
def Index(request):
    return render(request,'Index.html')

def rent(request):
    return render(request,'rent.html')

def categories(request):
    return render(request,'categories.html')

def Index(request):
    image_paths = [
        'images/banglow.png',
        'images/CarRental.png',
        'images/Furniturerental.png',
        # Add other image paths as needed
    ]
    return render(request, 'Index.html', {'image_paths': image_paths})

@login_required
def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories":categories
    }

    return render(request, 'categories.html',context)

class UserProfileView(View):
    template_name = 'Profile.html'

    def get(self,request,*args, **kwargs):
        
        id = kwargs.get('id')
        user =  get_object_or_404(CustomeUser,id=id)
    
        try:
            address = Address.objects.get(user=user)
        except Address.DoesNotExist:
            address = None

        products =Product.objects.all()

        context = {
           'user':user,
            'address':address,
           'products':products
        }
        return render(request,self.template_name,context)

# def rent_product(request):
    
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Index')  # Redirect to a page showing all products
#     else:
#         form = ProductForm()
#     return render(request, 'rent_product.html', {'form': form})

def rent_product(request):
    ImageFormSet = inlineformset_factory(Product, ProductImages, form=ImageForm, extra=2)  # Allow up to 3 images per product
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        if product_form.is_valid() and formset.is_valid():
            product = product_form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.product = product
                instance.save()
            return redirect('Index')
    else:
        product_form = ProductForm()
        formset = ImageFormSet()
    return render(request, 'rent_product.html', {'product_form': product_form, 'formset': formset})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'Index.html', {'products': products})

def images_list(request):
    images = ProductImages.objects.all()
    return render(request, 'Indext.html', {'images': images})

def update_profile(request):
    context = {}
    return render(request,'update_profile.html',context)
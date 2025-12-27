from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.

def ElectroIndex(request):
    DTslides = CarouselSlide.objects.all()
    DTbanner = BannerOffer.objects.first()
    DTpromoBox = PromoBox.objects.all()
    DTCategory = Category.objects.all()
    DTProduct = Product.objects.all()
    DTleft_banner = Banner.objects.filter(position='left').first()
    DTright_banner = Banner.objects.filter(position='right').first()

    context = {
        "slides": DTslides,
        "banner": DTbanner,
        'promoBox': DTpromoBox,
        'categories': DTCategory,
        'products': DTProduct,
        'left_banner': DTleft_banner,
        'right_banner': DTright_banner,
    }
    return render(request, "Electro/index.html", context)


def ElectroShop(request):
    query = request.GET.get('q')

    DTleft_banner = Banner.objects.filter(position='left').first()
    DTright_banner = Banner.objects.filter(position='right').first()
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(productName__icontains=query) |
            Q(description__icontains=query)
        )

    categories = Category.objects.all()

    return render(request, 'Electro/shop.html', {
        'products': products,
        'categories': categories,
        'left_banner': DTleft_banner,
        'right_banner': DTright_banner,
    })

def ShopByCategory(request, CatID):
    DTleft_banner = Banner.objects.filter(position='left').first()
    DTright_banner = Banner.objects.filter(position='right').first()
    DTCategory = Category.objects.all()
    DTProduct = Product.objects.filter(categoryID=CatID)

    context = {
        'products': DTProduct,
        'left_banner': DTleft_banner,
        'right_banner': DTright_banner,
        'categories': DTCategory,
    }
    return render(request, 'Electro/shop-by-category.html', context)



def ElectroContact(request):
    return render(request, 'Electro/contact.html')

def ElectroCart(request):
    return render(request, 'Electro/cart.html')

def ElectroCheckout(request):
    return render(request, 'Electro/checkout.html')

def ElectroShopDetail(request, pk):
    DTProduct = Product.objects.get(id=pk)
    DTProductDetail = ProductDetail.objects.get(productID=pk)

    context = {
        'products': DTProduct,
        'productDetail': DTProductDetail
    }
    return render(request, 'Electro/shop-details.html', context)



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
        cart[str(product_id)]['total'] = cart[str(product_id)]['quantity'] * cart[str(product_id)]['price']
    else:
        product = Product.objects.get(id=product_id)
        cart[str(product_id)] = {
            'productName': product.description,
            'price': float(product.new_price),
            'quantity': 1,
            'total': float(product.new_price) * 1,
            'image': product.image.url if product.image else ''
        }

    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'Electro/cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    return render(request, 'Electro/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })


def billing_add(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['total'] for item in cart.values())

    if request.method == "POST":
        data = request.POST
        qr_image = request.FILES.get('qr_code_image')

        billing = BillingDetail(
            first_name=data['first_name'],
            last_name=data['last_name'],
            country=data['country'],
            address=data['address'],
            town=data['town'],
            postcode=data['postcode'],
            phone=data['phone'],
            email=data['email'],
            qr_code_image=qr_image,
            total=data['total']
        )
        billing.save()
        return redirect('billing_list')
    
    return render(request, 'Electro/checkout.html', {
        'cart': cart,
        'total_price': total_price,
    })


def billing_list(request):
    billings = BillingDetail.objects.all()
    return render(request, 'Electro/BillingList.html', {'billings': billings})



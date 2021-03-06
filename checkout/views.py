
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from recipes.models import Product
from recipes.contexts import purchased_contents
from checkout.models import Purchases
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


## ---------------checkout----- 

# Function for checkout. Proceses payments after payment form is valid.
# redirect user to user profile after payments.
# Looping through cart items and add recipes to purchases after pay.
# after that user will see seucces messag 

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
                
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                
                purchased_items = request.session.get('cart', {})
                total = 0
                for id, quantity in purchased_items.items():
                    user = User.objects.get(username=request.user)
                    product = get_object_or_404(Product, pk=id)
                    total += quantity * product.price
                    purchases = Purchases(
                        user=user,
                        product=product,
                        quantity=quantity
                    )
                    purchases.save()
                    
                request.session['cart'] = {}
                
                return redirect(reverse('user_profile' ))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})



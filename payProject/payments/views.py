from django.shortcuts import render
from .models import Item
from django.http import JsonResponse
import stripe

def index(request):
    context = {
        'item_name': 'hello',
    }
    return render(request, "payments/index.html", context)


def detail(request, item_id):
    buy_item = Item.objects.filter(id=item_id)
    context = {
        'item_name': buy_item[0].name, 'item_description': buy_item[0].description, 'item_price': buy_item[0].price,
    }
    return render(request, "payments/index.html", context)

def buy (request, buy_id):
        stripe.api_key = "sk_test_51Li1VfGR7gyicWID2Yl5idJbt4o9Eo2LyJuXItZDYyJe8Nagld9UG6CWsz8MoJsVx4K3d8djze5pAkCRNITLTmj100WT3QDLio"
        buy_item = Item.objects.filter(id=buy_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'PLN',
                    'product_data': {
                        'name': buy_item[0].name,
                    },
                    'unit_amount': int(buy_item[0].price*100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        context = {
            "id_sesion": session.id,
        }
        return JsonResponse(context)

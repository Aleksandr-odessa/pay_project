import stripe
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

def buy(request):
    # y = json.loads()
    stripe.api_key = "sk_test_51Li1VfGR7gyicWID2Yl5idJbt4o9Eo2LyJuXItZDYyJe8Nagld9UG6CWsz8MoJsVx4K3d8djze5pAkCRNITLTmj100WT3QDLio"
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'PLN',
            'product_data': {
                'name': 'njdfh1',
            },
            'unit_amount': 20000,
        },
        'quantity': 1,
    }],
    mode='payment',
    success_url='https://example.com/success',
    cancel_url='https://example.com/cancel',
    )
    context = {
    "id_sesion": session.id
    }
    return JsonResponse(context)
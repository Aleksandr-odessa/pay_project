from .models import Item
import stripe

def request_item(req_cat, item_id):
    buy_item = Item.objects.filter(id=item_id)
    if req_cat == "detail":
        context = {
    'item_name': buy_item[0].name, 'item_description': buy_item[0].description, 'item_price': buy_item[0].price,
    }
    else:
        stripe.api_key = "sk_test_51Li1VfGR7gyicWID2Yl5idJbt4o9Eo2LyJuXItZDYyJe8Nagld9UG6CWsz8MoJsVx4K3d8djze5pAkCRNITLTmj100WT3QDLio"
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'PLN',
                    'product_data': {
                        'name': buy_item[0].name,
                    },
                    'unit_amount': int(buy_item[0].price * 100),
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
    return (context)
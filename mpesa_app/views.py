from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


def index(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        amount = int(request.POST['amount'])
        account_reference = request.POST['account_reference']
        transaction_desc = request.POST['transaction_desc']
        callback_url = 'https://darajambili.herokuapp.com/express-payment'
        cl = MpesaClient()
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, 'index.html')

# def index(request):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '0742545818'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://darajambili.herokuapp.com/express-payment'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")
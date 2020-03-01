from django.shortcuts import render
from random import randint
from .models import ResultPoolService, Subscribtion
from _sha3 import sha3_512
# from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from _datetime import datetime
import requests
import coreapi
from django.http.response import HttpResponse

def getNow():
    return datetime.now()

class ResultPoolServiceView(APIView):
    def post(self, request):
        try:
            resultpoolservice = request.data.get('ResultPoolService')
            method = resultpoolservice['method']
            method = method.lower()
            
        except:
            return Response(f"No method")
        
        if method == "getticket":
            ticket = sha3_512((str(datetime.now()) + str(randint(1000, 3000))).encode('utf-8')).hexdigest()
            a = ResultPoolService(r_ticket=ticket)
            a.save()
            return Response(f'Place for result has created.check ticket: {ticket}')
            
        elif method == "put":
            try:
                r_ticket = resultpoolservice["r_ticket"]
                result = resultpoolservice["result"]
            except:
                return Response(f"You need r_ticket and result")
            ResultPoolService.objects.filter(r_ticket=r_ticket).update(text=result, flag=1)
            return Response(f"{r_ticket} is ready")
        
        elif method == "get":
            try:
                r_ticket = resultpoolservice["r_ticket"]
            except:
                return Response(f"You need r_ticket")
            obj = ResultPoolService.objects.filter(r_ticket=r_ticket).get()
            result = obj.text
            return Response(f"{result} is your answer")
        
        elif method == "delete":
            try:
                r_ticket = resultpoolservice["r_ticket"]
            except:
                return Response(f"You need r_ticket")
            ResultPoolService.objects.filter(r_ticket=r_ticket).delete()
            return Response(f"{r_ticket} has successfully deleted")
        
        elif method == "subscribe":
            try:
                r_ticket = resultpoolservice["r_ticket"]
                endpoint = resultpoolservice["endpoint"]
            except:
                return Response(f"You need r_ticket and endpoint")
            a = Subscribtion(r_ticket = r_ticket, endpoint = endpoint)
            a.save()
            return Response(f"{r_ticket} has successfully subscribed")
        
        elif method == "unsubscribe":
            try:
                r_ticket = resultpoolservice["r_ticket"]
            except:
                return Response(f"You need r_ticket")
            Subscribtion.objects.filter(r_ticket=r_ticket).delete()
            return Response(f"{r_ticket} has successfully unsubscribed")
        
        
# def home(request):
#     response = requests.get('http://www.json-generator.com/api/json/get/bQInOcOZgy')
#     data = response.json()
#     return render(request, 'pool_2/index.html', {
#         'id': data['id'],
#         'text': data['text']
#     })
#     
def home(request):
    client = coreapi.Client()
    schema = client.get('http://127.0.0.1:8000/pool/poolservices/')
#     pools = client.action(schema, ['post'], params={"PoolService":{"method":"get"}})
    return render(request, 'pool_2/index.html', {
        'id': 2,
#         'text': pools
    })
        
            
            
            
            
        


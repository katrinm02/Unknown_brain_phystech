from types import FunctionType
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from _sha3 import sha3_512

from .models import PoolServices, PoolPending
from .serializers import PoolServicesSerializer
from _datetime import datetime
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.metadata import BaseMetadata

@action(methods=['GET'], detail=False)
def schema(self, request):
    meta = self.metadata_class()
    data = meta.determine_metadata(request, self)
    return Response(data)

# class MinimalMetadata(BaseMetadata):
#     """
#     Don't include field and other information for `OPTIONS` requests.
#     Just return the name and description.
#     """
#     def determine_metadata(self, request, view):
#         return {
#             'name': view.get_view_name(),
#             'description': view.get_view_description()
#         }

def getNow():
    return datetime.now()

def serialize(self, q):
    serializer = PoolServicesSerializer(q)
    content = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = PoolServicesSerializer(data=data)
    return serializer

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]



class PoolServiceView(APIView): 
    
    def get(self, request):
        return Response('post')
        
    def post(self, request):
        try:
            poolservice = request.data.get('PoolService')
            method = poolservice['method']
            method = method.lower()
        except:
            return Response(f"No method")
        
        if method == "get":
            services = PoolServices.objects.all()
            serializer = PoolServicesSerializer(services, many=True)
            return Response({"PoolServices": serializer.data})
        
        elif method == "register":
            try:
                endpoint = poolservice['endpoint']
                pool = poolservice['pool']
            except:
                return Response(f"You need endpoint and pool")
            if PoolServices.objects.filter(endpoint=endpoint):
                if PoolServices.objects.filter(endpoint=endpoint, pool=pool):
                    obj = PoolServices.objects.filter(endpoint=endpoint, pool=pool)[0]
                    ticket = obj.getTicket()
                    q = self.update(ticket, 'SA')
                else:
                    return Response({"Error"})   
            else:
                ticket = sha3_512((endpoint + str(pool)).encode('utf-8')).hexdigest()
                q = PoolServices(ticket=ticket, endpoint=endpoint, pool=pool, timestamp=getNow())
                serializer = self.serialize(q)
                q.save()
                if serializer.is_valid(raise_exception=True):
                    poolservice_saved = serializer.save()
                    ticket = poolservice_saved.ticket
            return Response(f"PoolService created succesfully. Ticket: {ticket}")

        elif method == "update":
            #ticket; state, timestamp
            try:
                ticket = poolservice['ticket']
                pool = poolservice['pool']
            except:
                return Response(f"You need ticket and pool")
            saved_pool = get_object_or_404(PoolServices.objects.all(), pk=ticket)
            serializer = PoolServicesSerializer(instance=saved_pool, data={"pool": pool, "timestamp":getNow()}, partial=True)
            if serializer.is_valid(raise_exception=True):
                pool_saved = serializer.save()
            return Response(f"success: PoolService {pool_saved.endpoint} updated successfully")
        
        elif method == "unregister":
            try:
                ticket = poolservice['ticket']
            except:
                return Response(f"You need ticket")
            PoolServices.objects.filter(pk=ticket).delete()
            return Response(f"success: PoolService {ticket} deleted successfully")
     
        elif method == "getwork":
            try:
                pool = poolservice['pool']
            except:
                return Response(f"You need pool")
            if PoolServices.objects.filter(pool=pool, state='SA').count() < 1:
                return Response(f"No available pool service")
            else:
                obj = PoolServices.objects.filter(pool=pool, state='SA').first()
                print(obj)
                ticket = obj.getTicket()
                self.update(ticket, 'SP')
                a = PoolPending(ticket=obj, timer=getNow())
                a.save()
                return Response(f"Pool servie {obj.endpoint} is busy now")
                        
    def update(self, ticket, state):
        obj = PoolServices.objects.filter(ticket=ticket).update(state=state, timestamp=getNow())
        return obj 
             
            

    
    
    

            
        
        
        
        
        
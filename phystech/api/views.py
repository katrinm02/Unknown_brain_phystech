from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from .models import TimeTable
from .serializers import TimeTableSerializer

from _datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def serialize(self, q):
    serializer = TimeTable(q)
    content = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = TimeTable(data=data)
    return serializer

def getNow():
    return datetime.now()

class PoolTimeTable(APIView):
    def post(self, request):
        try:
            timetable = request.data.get('PoolTimeTable')
            method = timetable['method']
            method = method.lower()
        except:
            return Response(f"No method")
        
        if method == "gettimetable":
            try: 
                day = timetable['day']
            except:
                raise ValueError("You need day")
            table = TimeTable.objects.all().filter(day)
            serializer = TimeTableSerializer(table, many=True)
            return Response({"Timetable": serializer.data})
        
        elif method == "editclass":
            pass
        
        elif method == "putclass":
            pass
        
        elif method == "delete":
            try:
                id = timetable['id']
            except:
                raise ValueError("You need id")
            TimeTable.objects.filter(pk=id).delete()
            return Response(f"Timetable {id} has successfully deleted")
            
                
            
            
            
import json
from rest_framework import viewsets
from .serializers import PersonSerializer, ParticipationSerializer, SttSerializer, SummarySerializer
from .models import Person, Participation, Stt, Summary
from django.http import HttpResponse, JsonResponse


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


def ParticipationViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    queryset = Participation.objects.filter(username=data["username"])
    serializer = ParticipationSerializer(queryset, many=True)
    if queryset.count() == 0:
        return HttpResponse(status=400)
    return JsonResponse(serializer.data, safe=False)


def SttViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    buffer = ""
    queryset = Stt.objects.get(class_id=data["class_id"])
    with open("stt/" + queryset.stt_file, encoding='utf-8') as txtfile:
        buffer = txtfile.read()
    return JsonResponse({'contents': buffer}, safe=False)


def SummaryViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    buffer = ""
    queryset = Summary.objects.get(class_id=data["class_id"])
    with open("summary/" + queryset.summary_file, encoding='utf-8') as txtfile:
        buffer = txtfile.read()
    return JsonResponse({'contents': buffer}, safe=False)

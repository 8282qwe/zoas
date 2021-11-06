import json
from .STT_convert import *
from .Summar_convert import *
from rest_framework import viewsets
from .serializers import PersonSerializer, ParticipationSerializer, SttSerializer, SummarySerializer
from .models import Person, Participation, Stt, Summary
from django.http import HttpResponse, JsonResponse


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


def joinViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)

    if Participation.objects.filter(username=data["username"], class_id=data["class_id"]).count() == 1:
        return HttpResponse(status=400)

    Participation.objects.create(username=data["username"], class_id=data["class_id"]).save()
    return HttpResponse(status=200)


def ParticipationViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    queryset = Participation.objects.filter(username=data["username"])
    serializer = ParticipationSerializer(queryset, many=True)
    # 효준이(영상파일 <-> stt)체킹 후 영상 업로드 진행
    for dictionary in queryset.values_list():
        if (Stt.objects.filter(class_id=dictionary[2]).count() == 0):
            upload_blob(dictionary[2])
            google_transcribe(dictionary[2])
            # 창우(stt<->summary)체킹 후 작업 실행
            # 없다! {"username" : value1, "class_id": value2}
            # summary(class_id) 실행 후 summary에 값(.txt)로 저장
            summary_convert(dictionary[2])
            sttbuffer = dictionary[2] + ".txt"
            summarybuffer = dictionary[2] + ".txt"
            Stt.objects.create(class_id=dictionary[2], stt_file=sttbuffer).save()
            Summary.objects.create(class_id=dictionary[2], summary_file=summarybuffer).save()
    if queryset.count() == 0:
        return HttpResponse(status=400)
    return JsonResponse(serializer.data, safe=False)


def SttViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    buffer = ""
    buffer2 = ""
    buffer3 = ""
    buffer4 = ""
    queryset = Stt.objects.get(class_id=data["class_id"])

    with open("stt/" + queryset.stt_file, encoding='utf-8') as txtfile:
        buffer = txtfile.read()
    with open("summary/" + queryset.stt_file, encoding='utf-8') as txtfile:
        buffer2 = txtfile.read()
    with open("keyword/" + queryset.stt_file, encoding='utf-8') as txtfile:
        buffer3 = txtfile.read()
    with open("timestamp/" + queryset.stt_file, encoding='utf-8') as txtfile:
        buffer4 = txtfile.read()
    return JsonResponse({'stt_contents': buffer,
                         'summary_contents': buffer2,
                         'keywords': buffer3,
                         "timestamps": buffer4
                         }, safe=False)


def SummaryViewSet(request):
    s = request.body.decode('utf-8')
    data = json.loads(s)
    buffer = ""
    queryset = Summary.objects.get(class_id=data["class_id"])
    with open("summary/" + queryset.summary_file, encoding='utf-8') as txtfile:
        buffer = txtfile.read()
    return JsonResponse({'contents': buffer}, safe=False)

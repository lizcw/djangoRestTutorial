from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Study
from .serializers import StudySerializer


def index(request):
    template = 'main/index.html'
    studies = Study.objects.all()
    context = {'name': "ME", 'studies': studies}
    return render(request, template, context)

@api_view(['GET', 'POST'])
def study_list(request, format=None):
    """
    List all studys, or create a new study.
    """
    if request.method == 'GET':
        studys = Study.objects.all()
        serializer = StudySerializer(studys, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def study_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code study.
    """
    try:
        study = Study.objects.get(pk=pk)
    except Study.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudySerializer(study)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudySerializer(study, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        study.delete()
        return HttpResponse(status=204)


class StudyList(APIView):
    def get(self, request, format=None):
        studys = Study.objects.all()
        serializer = StudySerializer(studys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Study.objects.all().order_by('-created')
    serializer_class = StudySerializer
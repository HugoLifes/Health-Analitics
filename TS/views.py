from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from rest_framework import parsers
from django.http import response

from TS.models import Activity, Heartrate, Sleep
from TS.serializers import ActivitySerializer, HeartSerializer, SleepSerializer
from django.http import HttpResponse #added
from django.core.files.storage import default_storage

# Create your views here.

def main(request):
    return render(request, 'analitics/main.html')
def user_info(request):
    return render(request, 'analitics/user_info.html')

@csrf_exempt
def activityApi(request, id=0):
    if request.method== 'GET':
        activity = Activity.objects.all()
        activity_serializer = ActivitySerializer(activity, many=True)
        return response.JsonResponse(activity_serializer.data,safe=False)
    elif request.method== 'POST':
        activity_data = parsers.JSONParser().parse(request)
        activity_serializer= ActivitySerializer(data=activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return response.JsonResponse('Added Successfully', safe= False)
        return response.JsonResponse('Failed to add')
    elif request.method == 'PUT':
        activity_data= parsers.JSONParser().parse(request)
        print(activity_data['ActivityId'])
        activity =  Activity.objects.get(ActivityId=activity_data['ActivityId'])
        activity_serializer = ActivitySerializer(activity,data=activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return response.JsonResponse("Update Successfully", safe=False)
        return response.JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        activity = Activity.objects.get(ActivityId=id)
        activity.delete()
        return response.JsonResponse("Deleted Successfully", safe= False)


@csrf_exempt
def heartApi(request, id=0):
    if request.method== 'GET':
        heart = Heartrate.objects.all()
        heart_serializer = HeartSerializer(heart, many=True)
        return response.JsonResponse(heart_serializer.data,safe=False)
    elif request.method== 'POST':
        heart_data = parsers.JSONParser().parse(request)
        heart_serializer= HeartSerializer(data=heart_data)
        if heart_serializer.is_valid():
            heart_serializer.save()
            return response.JsonResponse('Added Successfully', safe= False)
        return response.JsonResponse('Failed to add')
    elif request.method == 'PUT':
        heart_data= parsers.JSONParser().parse(request)
        print(heart_data['HeartId'])
        heart = Heartrate.objects.get(HeartId=heart_data['HeartId'])
        heart_serializer = ActivitySerializer(heart,data=heart_data)
        if heart_serializer.is_valid():
            heart_serializer.save()
            return response.JsonResponse("Update Successfully", safe=False)
        return response.JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        heart = Heartrate.objects.get(HeartId=id)
        heart.delete()
        return response.JsonResponse("Deleted Successfully", safe= False)

@csrf_exempt
def sleepApi(request, id=0):
    if request.method== 'GET':
        sleep = Sleep.objects.all()
        sleep_serializer = SleepSerializer(sleep, many=True)
        return response.JsonResponse(sleep_serializer.data,safe=False)
    elif request.method== 'POST':
        sleep_data = parsers.JSONParser().parse(request)
        sleep_serializer= SleepSerializer(data=sleep_data)
        if sleep_serializer.is_valid():
            sleep_serializer.save()
            return response.JsonResponse('Added Successfully', safe= False)
        return response.JsonResponse('Failed to add')
    elif request.method == 'PUT':
        sleep_data= parsers.JSONParser().parse(request)
        print(sleep_data['SleepId'])
        sleep = Sleep.objects.get(SleepId=sleep_data['SleepId'])
        sleep_serializer = ActivitySerializer(sleep,data=sleep_data)
        if sleep_serializer.is_valid():
            sleep_serializer.save()
            return response.JsonResponse("Update Successfully", safe=False)
        return response.JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        sleep = Sleep.objects.get(SleepId=id)
        sleep.delete()
        return response.JsonResponse("Deleted Successfully", safe= False)


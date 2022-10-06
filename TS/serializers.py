from rest_framework import serializers
from TS.models import Activity, Heartrate, Sleep


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("ActivityId","ActivityDate", "Steps", "Distance", "Run", "Calories")

class HeartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartrate
        fields= ("HeartId","HeartDate", "Time", "HeartRate")

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ("SleepId", "SleepDate", "DeepSleepTime", "ShallowSleepTime", "WakeTime", "Start", "End")
from rest_framework import serializers
from .models import InterventionType
from nurses_note.serializers import NursesNoteDetailsSerializer


class InterventionTypeSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = InterventionType
        fields = "__all__"
        read_only_fields = ["id"]

'''
class InterventionTypeDetailsSerializer ( serializers.ModelSerializer ):
    #nurses_note = NursesNoteDetailsSerializer ()

    class Meta:
        model = InterventionType
        fields = "__all__"
        read_only_fields = ["id"]
'''

from rest_framework import serializers
from glossary.models import GlossaryTerm 

class GlossaryItemSerializer(serializers.ModelSerializer): 
    """
    Serializer for glossary items.
    """
    class Meta:
        model = GlossaryTerm  
        fields = "__all__" 

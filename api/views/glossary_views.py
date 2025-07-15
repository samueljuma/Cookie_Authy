from rest_framework import viewsets, status
from glossary.models import GlossaryTerm
from api.serializers.glossary_serializers import GlossaryItemSerializer
from rest_framework.permissions import IsAuthenticated

class GlossaryViewSet(viewsets.ModelViewSet): 
    queryset = GlossaryTerm.objects.all()
    serializer_class = GlossaryItemSerializer
    permission_classes = [IsAuthenticated] 
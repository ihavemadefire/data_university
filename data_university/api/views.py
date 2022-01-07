from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Session
from .serializers import SessionSerializer


@api_view(['GET'])
def session_list(request):
    """
    List all sessions
    """
    sessions = Session.objects.all()
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def session_detail(request, slug):
    """
    Retrieve a session.
    """
    try:
        session = Session.objects.get(slug=slug)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SessionSerializer(session)
    return Response(serializer.data)

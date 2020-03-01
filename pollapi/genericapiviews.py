from rest_framework import generics

from .models import *
from .serializers import *

class PollsList(generics.ListCreateAPIView):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer


class PollsDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = PollsDetail.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

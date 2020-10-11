# TODO: Setup Auth0 User Management Helper Functions Here

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.views import Response
from rest_framework.decorators import action
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["POST"])
    def email_invitation(self, request, pk=None):
        try:
            with transaction.atomic():
                # TODO: Add Email Sending Method Here
                return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"err": str(e)}, status=status.HTTP_400_BAD_REQUEST)

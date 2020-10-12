# TODO: Setup Auth0 User Management Helper Functions Here

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.views import Response
from rest_framework.decorators import action
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.utils import create_password_recovery


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"])
    def email_invitation(self, request, pk=None):
        try:
            with transaction.atomic():
                wat_id = request.data["wat_id"]
                email = f"{wat_id}@uwaterloo.ca"

                password_recovery_link = create_password_recovery(wat_id, email)

                # TODO: Add sendinblue email sending

                return Response(
                    {"password_recovery_link": password_recovery_link},
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response({"err": str(e)}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Auth.is_owner_read_write import IsOwnerOrDeny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrDeny]

    def get(self, request):
        CustomUser = get_user_model()
        user = CustomUser.objects.all()
        return Response(user)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import CustomRegistrationSerializer, LogoutSerializer


class CustomRegistrationView(APIView):

    def post(self, request):
        ser = CustomRegistrationSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({
            'detail': 'User has been created successfully.'
        }, status=status.HTTP_201_CREATED)


class CustomLogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        ser = LogoutSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        try:
            token = RefreshToken(ser.validated_data['refresh']) 
            token.blacklist()
            return Response({
                'detail': 'Successfully logged out.'
            }, status=status.HTTP_204_NO_CONTENT)

        except TokenError:
            return Response({
                'detail': 'Invalid or expired token.'
            }, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from api.serializers.auth_serializers import LoginSerializer
from datetime import datetime
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.exceptions import ValidationError

class LoginView(APIView): 
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response = Response(
            data = {
                'succces': True,
                'message': 'Login successful',
                'user': data['username'],
            },
            status=status.HTTP_200_OK
            )

        response.set_cookie(
            key='Authentication',
            value=data['access'],
            httponly=True, 
            secure=True, 
            samesite='None', 
            expires=data['access_expires_at']
        )
        response.set_cookie(
            key='Refresh',
            value=data['refresh'],
            httponly=True, 
            secure=True, 
            samesite='None', 
            expires=data['refresh_expires_at']
        )

        return response
    

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("Refresh")  # Extract from cookies

        if not refresh_token:
            raise ValidationError("Refresh token is missing")

        serializer = TokenRefreshSerializer(data={"refresh": refresh_token})
        serializer.is_valid(raise_exception=True)

        response = Response(
            {
                'success': True,
                'message': 'Token refreshed successfully',
            },
            status=status.HTTP_200_OK,
        )

        # Update Authentication cookie with new access token
        response.set_cookie(
            key="Authentication",
            value=serializer.validated_data["access"],
            httponly=True,
            secure=True,
            samesite="Lax",
        )

        return response

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timezone

class LoginSerializer(serializers.Serializer): 
    """
    Serializer for user login.
    """
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        """
        Validate the username and password.
        """
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            raise serializers.ValidationError("Invalid username or password.")
        
        # Generate tokens 
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        access_expiry = datetime.fromtimestamp(access['exp'], timezone.utc).isoformat()
        refresh_expiry = datetime.fromtimestamp(refresh['exp'], timezone.utc).isoformat()
        
        return {
            'username': user.username,
            'refresh': str(refresh),
            'access': str(access),
            'access_expires_at': access_expiry,
            'refresh_expires_at': refresh_expiry
        }

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.api.serializers import RegistrationSerializer
from user_app import models

@api_view(['POST'])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        data = {
            'response': "Registration Successful!!",
            'username': account.username,
            'email': account.email,
        }
        token, created = Token.objects.get_or_create(user=account)
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
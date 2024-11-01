from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import AccessToken

class UserDetailView(APIView):
    permission_classes = [AllowAny]  # Garante que qualquer um pode acessar
    @swagger_auto_schema(
        operation_description="LoginUser",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['cpf', 'senha'],
            properties={
                'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do usuario'),
                'senha': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuario'),
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'user': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nome de usuário'),
                            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Primeiro nome do usuário'),
                            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Último nome do usuário'),
                            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do usuário'),
                        },
                    ),
                    'auth_token': openapi.Schema(type=openapi.TYPE_STRING, description='Token de autenticação JWT'),
                },
            ),
        }
    )
    def post(self, request):
        data = request.data
        user = authenticate(request=request, username=data['cpf'], password=data['senha'])

        if user is not None:
            access_token = AccessToken.for_user(user)  # Gera o token JWT para o usuário

            return Response({
                'user': {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                },
                'auth_token': str(access_token),  # Retorna o token como string
            }, status=status.HTTP_200_OK)

        return Response({'detail': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

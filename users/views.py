from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer, objectSerializer, colorSerializer
from .models import userModel, objectModel, colorModel
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class login_api(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        models = User.objects.filter(email=email).first()
        
        if models is None:
            raise AuthenticationFailed('user not found')
        else:
            if models.password != password:
                raise AuthenticationFailed('password not current')
            else:
                _, token = AuthToken.objects.create(models) 

        # serializer= AuthTokenSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']

        return Response({
                'user_info': {
                'id': models.id,
                'username': models.username,
                'email': models.email
            },
            'token': token
        })

class get_user_data(APIView):
    def get(self, request):
        user= request.user

        if user.is_authenticated:
            return Response({
                'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'status': 0
        })
        else:
            return Response({'error': 'not authenticated', 'status': 1})

class register_api(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
                'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email 
            }
        })

class getObject(APIView):
    def post(self, request):
        tableName= request.data['tableName']

        if tableName=="object":
            model= objectModel.objects.all()
        if tableName== "color":
            model= colorModel.objects.all()

        return Response(model)

class deleteObject(APIView):
    def delete(self, request):
        id = request.data['id']
        tableName= request.data['tableName']

        if tableName=="object":
            member=objectModel.objects.get(id=id)
            member.delete()
        if tableName=="color":
            member=colorModel.objects.get(id=id)
            member.delete()

class addobject(APIView):
    def post(self, request):
        serializer = objectSerializer(data=request.data)
        serializer.is_valid()
        if serializer.save() :
            return Response({
                "message": "success"
            })
        else:
            return Response({
                "message": "failed"
            })

class addcolor(APIView):
    def post(self, request):
        serializer = colorSerializer(data=request.data)
        serializer.is_valid()
        if serializer.save() :
            return Response({
                "message": "success"
            })
        else:
            return Response({
                "message": "failed"
            })
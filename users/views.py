from rest_framework.views import APIView, Request, Response, status

from .models import User
from .serializer import UserSerializer, JWTSerializer
from .permissions import PermissionsPersonalized

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(APIView):

    def post(self, request:Request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsPersonalized]


    def get(self, request: Request, user_id: int):
        user = User.objects.get(id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status.HTTP_200_OK)


class UserLogin(TokenObtainPairView):
    serializer_class = JWTSerializer        

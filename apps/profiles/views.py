from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserDetailSerializer


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Get user profile with default address"""
        try:
            user = request.user
            serializer = UserDetailSerializer(user)
            return Response({
                'status': 'success',
                'message': 'Profile retrieved successfully',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error retrieving profile: {str(e)}',
            }, status=status.HTTP_400_BAD_REQUEST)

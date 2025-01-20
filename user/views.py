from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from company.models import Company
from student.models import Student

from .models import User, UserRoles
from .serializers import UserCreateSerializer


class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            with transaction.atomic():
                # Create user with hashed password (create_user handles hashing)
                user = User.objects.create_user(
                    email=validated_data['email'],
                    password=validated_data['password'],  # Password will be automatically hashed
                    name=validated_data.get('name', ''),
                    role=validated_data.get('role', UserRoles.STUDENT)
                )
                
                # Create profile based on role
                if user.role == UserRoles.COMPANY:
                    Company.objects.create(
                        user=user,
                        company_name=validated_data.get('company_name', ''),
                        industry=validated_data.get('industry', ''),
                        location=validated_data.get('location', ''),
                        description=validated_data.get('description', ''),
                    )
                else:
                    Student.objects.create(
                        user=user,
                        full_name=validated_data.get('full_name', ''),
                        education=validated_data.get('education', ''),
                        skills=validated_data.get('skills', []),
                        experience=validated_data.get('experience', ''),
                        location=validated_data.get('location', ''),
                    )
            
            return Response({
                'message': 'User created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({
                'error': 'Please provide both email and password'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(email=email, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'name': user.name,
                    'role': user.role
                }
            }, status=status.HTTP_200_OK)
            
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        # Add logout logic here
        pass

    @action(detail=False, methods=['post'])
    def password_reset(self, request):
        # Add password reset logic here
        pass

    # Add your protected viewset logic here

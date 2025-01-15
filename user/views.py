from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsStudent, IsOrganization, RoleBasedPermission
from .models import UserRoles
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Using specific role permissions
@api_view(['GET'])
@permission_classes([IsStudent])
def student_only_view(request):
    # Only students can access this view
    return Response({"message": "Hello Student!"})

@api_view(['GET'])
@permission_classes([IsOrganization])
def organization_only_view(request):
    # Only organizations can access this view
    return Response({"message": "Hello Organization!"})

# Using the generic RoleBasedPermission
class SomeViewSet(viewsets.ModelViewSet):
    # Allow both students and organizations
    permission_classes = [RoleBasedPermission([UserRoles.STUDENT, UserRoles.ORGANIZATION])]
    
    # ... rest of your viewset code

# Or for organization-only viewset
class OrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = [RoleBasedPermission([UserRoles.ORGANIZATION])]
    
    # ... rest of your viewset code

class SomeProtectedViewSet(viewsets.ModelViewSet):
    # Must be both authenticated AND have the correct role
    permission_classes = [
        IsAuthenticated & 
        RoleBasedPermission([UserRoles.ORGANIZATION])
    ]
    
    # ... rest of your viewset code

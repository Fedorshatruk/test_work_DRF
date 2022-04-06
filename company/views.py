from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from company.models import Employee, Department
from company.serializers import EmployeeModelSerializer, DepartmentModelSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = EmployeeModelSerializer
    filterset_fields = ['id', 'last_name']
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class DepartmentView(mixins.ListModelMixin, GenericViewSet):
    queryset = Department.objects.annotate(
                                  employees_count=Count('employees'),
                                  full_salary=Sum('employees__salary'))
    serializer_class = DepartmentModelSerializer
    permission_classes = [permissions.AllowAny]



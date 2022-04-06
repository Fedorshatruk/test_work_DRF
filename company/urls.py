from rest_framework.routers import DefaultRouter

from company.views import EmployeeViewSet, DepartmentView

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'department', DepartmentView, basename='department')
urlpatterns = router.urls

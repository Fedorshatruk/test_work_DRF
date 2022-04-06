from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from company.models import Employee, Department


class PositionFilter(SimpleListFilter):
    title = 'Должность'
    parameter_name = 'position'

    def lookups(self, request, model_admin):
        return model_admin.model.POSITION

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(position=self.value())


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'position',
        'department'
    )
    list_filter = (PositionFilter,)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'director'
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)

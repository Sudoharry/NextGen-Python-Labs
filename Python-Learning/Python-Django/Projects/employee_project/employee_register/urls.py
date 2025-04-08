from django.urls import path, include
from . import views 
from .views import bulk_import_employees, confirm_delete_employee


urlpatterns = [
    path('',views.employee_form, name='employee_insert'), # get and post request for insert operation
    path('list/', views.employee_list, name='employee_list'), # get and post request for update operation
    path('<int:id>/', views.employee_form, name='employee_update'), # get request to retrieve and display all records
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), # get request to delete record
    path('bulk-import/', bulk_import_employees, name='bulk_import'),
    path('employee/delete/<int:employee_id>/', confirm_delete_employee, name='confirm_delete_employee'),

]
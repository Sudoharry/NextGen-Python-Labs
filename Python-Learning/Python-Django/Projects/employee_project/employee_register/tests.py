from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Employee, Position
from .forms import EmployeeForm
import csv

class EmployeeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(title='Project Manager')
        self.employee = Employee.objects.create(
            fullname='Kapil Siju',
            mobile='9978742331',
            emp_code='1313',
            position=self.position
        )
    
    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kapil Siju')
    
    def test_employee_create_view(self):
        data = {
            'fullname': 'Kapil Siju',
            'mobile': '9978742331',
            'emp_code': '1313',
            'position': self.position.id
        }
        response = self.client.post(reverse('employee_insert', args=[self.employee.id]), data )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Employee.objects.filter(fullname='Kapil Siju').exists())
    
    def test_employee_update_view(self):
        data = {
            'fullname': 'Kapil Siju',
            'mobile': '9978742331',
            'emp_code': '1313',
            'position': self.position.id
        }
        response = self.client.post(reverse('employee_update', args=[self.employee.id]), data)
        self.assertEqual(response.status_code, 302)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.fullname, 'Kapil Siju')
    
    def test_employee_delete_view(self):
        response = self.client.get(reverse('employee_delete', args=[self.employee.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())
    
    # def test_employee_search_view(self):
    #     response = self.client.get(reverse('employee_search') + '?q=Kapil')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Kapil Siju')
    
    def test_bulk_import_employees(self):
        csv_data = b"fullname,mobile,emp_code,position\nKapil Siju,9978742331,1313,Project Manager\n"
        csv_file = SimpleUploadedFile("employees.csv", csv_data, content_type="text/csv")
        response = self.client.post(reverse('bulk_import'), {'csv_file': csv_file})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Employee.objects.filter(fullname='Kapil Siju').exists())

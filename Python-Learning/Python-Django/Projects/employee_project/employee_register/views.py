from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Position
from .forms import EmployeeForm, EmployeeUploadForm
import csv


# Employee List View
def employee_list(request):
    context = {
        'page_title': 'Employee List',  # Dynamic h1 title
        'project_description': 'A list of total employees in the company with complete details',
        'employee_list': Employee.objects.all()  # Employee data
    }
    return render(request, "employee_register/employee_list.html", context)

# Employee Create & Update View
def employee_form(request, id=0):
    context = {
        'page_title': 'Employee Register',  # Dynamic h1 title
        'project_description': 'A Python Django project for implementing CRUD operations dynamically',
        'button_label': 'Submit'  # Default button label for Create action
    }

    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = get_object_or_404(Employee, pk=id)  # Avoids errors if ID does not exist
            form = EmployeeForm(instance=employee)
            context['button_label'] = 'Update'  # Change button label for Update

        context['form'] = form
        return render(request, "employee_register/employee_form.html", context)

    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            if id == 0:
                messages.success(request, "Employee added successfully!")  # ✅ Success message on create
                return redirect('/employee/list')
            else:
                messages.success(request, "Employee updated successfully!")  # ✅ Success message on update
                return redirect('/employee/list')
        
        messages.error(request, "Error: Invalid input. Please check the form.")  # ❌ Error message
        context['form'] = form  # Pass form with errors back to template
        return render(request, "employee_register/employee_form.html", context)

# Employee Delete View
def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('/employee/list')

def confirm_delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        entered_name = request.POST.get("confirmation_name")

        if entered_name.strip().lower() == employee.name.strip().lower():
            employee.delete()
            messages.success(request, f"Employee '{employee.name}' has been deleted successfully.")
            return redirect("employee_list")  # Redirect to the employee list after deletion
        else:
            messages.error(request, "Entered name does not match. Deletion aborted.")

    return render(request, "confirm_delete.html", {"employee": employee})


# Employee Search View
def employee_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = Employee.objects.filter(fullname__icontains=query)
        else:
            results = Employee.objects.all()
        return render(request, 'employee_register/employee_search.html', {'results': results, 'query': query})

def bulk_import_employees(request):
    if request.method == "POST":
        form = EmployeeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"]

            #  Validate File Type
            if not csv_file.name.endswith(".csv"):
                messages.error(request, "This is not a CSV file.")
                return redirect("bulk_import")

            #  Read and Decode CSV File
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)
            next(reader, None)  # Skip header row if present

            employees_to_create = []

            for row in reader:
                if len(row) < 4:  # Ensure all fields exist (Name,Phone,Emp_code, Position)
                    messages.warning(request, f"Skipping incomplete row: {row}")
                    continue  

                fullname, mobile,emp_code, position_title = row

                #  Ensure Position Exists
                position_obj, _ = Position.objects.get_or_create(title=position_title)

                #  Add Employee to List
                employees_to_create.append(
                    Employee(fullname=fullname, mobile=mobile,emp_code=emp_code, position=position_obj)
                )

            #  Bulk Create Employees
            if employees_to_create:
                Employee.objects.bulk_create(employees_to_create)
                messages.success(request, f"{len(employees_to_create)} employees added successfully!")
            else:
                messages.warning(request, "No valid employees found in the file.")

            return redirect("employee_list")
    else:
        form = EmployeeUploadForm()

    return render(request, "bulk_import.html", {"form": form})

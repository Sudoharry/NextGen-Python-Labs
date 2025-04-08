# Auto fill feature can be implemented in the project where the is requirement of address or HR management where employee
# doesn't have to fill up the details which saves time and reduce the long efforts.

## views.py

"""
  def autofill_employee_data(request):
    try:
        # Fetch the latest employee data (or use logic to get user-specific data)
        employee = Employee.objects.last()
        if not employee:
            return JsonResponse({"error": "No employee data available"}, status=404)

        # Return employee data as JSON
        data = {
            "fullname": employee.fullname,
            "emp_code": employee.emp_code,
            "mobile": employee.mobile,
            "position": employee.position.id if employee.position else "",  # Adjust based on your model
        }
        return JsonResponse(data)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
'""" 

## forms.py - Add before the body tag

"""
<script>
    document.addEventListener("DOMContentLoaded", function () {
        fetch("/employee/autofill/")
            .then(response => response.json())
            .then(data => {
                if (!data.error) {
                    document.getElementById("id_fullname").value = data.fullname || "";
                    document.getElementById("id_emp_code").value = data.emp_code || "";
                    document.getElementById("id_mobile").value = data.mobile || "";
                    
                    // Handle select dropdown for position
                    let positionField = document.getElementById("id_position");
                    if (positionField) {
                        positionField.value = data.position;
                    }
                } else {
                    console.warn("Autofill data not available:", data.error);
                }
            })
            .catch(error => console.error("Error fetching autofill data:", error));
    });
    </script>

"""

## urls.py

    path('autofill/', autofill_employee_data, name='autofill_employee_data'),



### models.py

- This would be within the Register class of an employee_register app

"""
user_behavior_data = models.JSONField(default=dict,blank=True, null=True)  # Store AI-based behavior data

"""
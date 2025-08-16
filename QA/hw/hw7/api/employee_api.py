import requests


class EmployeeApi:
    BASE_URL = "http://5.101.50.27:8000"

    def create_employee(self, employee_data):
        url = f"{self.BASE_URL}/employee/create"
        response = requests.post(url, json=employee_data)
        return response

    def get_employee(self, employee_id):
        url = f"{self.BASE_URL}/employee/info/{employee_id}"  # Обрати внимание на 'info'
        response = requests.get(url)
        return response

    def update_employee(self, employee_id, updated_data):
        url = f"{self.BASE_URL}/employee/update/{employee_id}"
        response = requests.put(url, json=updated_data)
        return response

    def delete_employee(self, employee_id):
        url = f"{self.BASE_URL}/employee/delete/{employee_id}"
        response = requests.delete(url)
        return response

    def get_all_employees(self):
        url = f"{self.BASE_URL}/employee/list"
        response = requests.get(url)
        return response
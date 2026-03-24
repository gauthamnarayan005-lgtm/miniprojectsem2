from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import EmployeeProfile

User = get_user_model()

class EmployeeIDBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # First, try to authenticate using the standard username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                # If username isn't found, try treating the input as an employee_id_number
                employee_profile = EmployeeProfile.objects.get(employee_id_number=username)
                user = employee_profile.user
            except EmployeeProfile.DoesNotExist:
                return None

        # Check if the password matches the found user
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
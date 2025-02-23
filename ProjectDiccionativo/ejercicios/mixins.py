# ejercicios/mixins.py  
from django.contrib.auth.mixins import UserPassesTestMixin

class ProfessorOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.role == "profesor")

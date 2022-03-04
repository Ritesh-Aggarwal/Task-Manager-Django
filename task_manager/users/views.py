from django.views import generic

from .forms import UserSignUpForm


class SignUpView(generic.CreateView):
    form_class = UserSignUpForm
    success_url = "/user/login"
    template_name = "tasks/user_create.html"

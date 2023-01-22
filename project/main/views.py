from django.views.generic import CreateView
from .forms import RegisterUserForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))





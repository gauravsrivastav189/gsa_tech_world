from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .models import  Delivery, Revenue

class Profile(TemplateView):
    template_name='registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch a list of users (you can modify this query as needed)
        users = User.objects.all()
        context['users'] = users  # Pass the users to the template context
        return context


class Home(TemplateView):
    template_name='registration/home.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch a list of users (you can modify this query as needed)
        users = User.objects.all()
        context['users'] = users  # Pass the users to the template context
        return context

class Logout(TemplateView):
    template_name='registration/logout.html'

# @method_decorator(login_required , name='dispatch')
# class Show(TemplateView):
#     template_name='registration/show.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         u=User.objects.all()
#         context={'user':u}
#         return context


'''
@method_decorator(staff_member_required, name='dispatch')
class Show(ListView):
    model = User
    template_name = 'registration/show.html'
    context_object_name='user'
    # ordering = ['-id']
    # paginate_by = 4
    # to use pagination you will have to modify template as well
'''

from django.utils import timezone
from datetime import date

@method_decorator(staff_member_required, name='dispatch')
class Show(TemplateView):
    template_name = 'registration/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate today's date
        today = date.today()

        # Filter users registered today
        users = User.objects.filter(date_joined__date=today)

        # Filter pending status deliveries
        pending_deliveries = Delivery.objects.filter(status='pending')
        
        revenues = Revenue.objects.all()
        
        context['users'] = users
        context['deliveries'] = pending_deliveries  # Only pending status deliveries
        context['revenues'] = revenues

        return context




@method_decorator(login_required , name='dispatch')
class Detail(DetailView):
    model = User
    template_name = "registration/detail.html"
    context_object_name='u'

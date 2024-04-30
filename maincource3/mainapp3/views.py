from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import VkForm
from .models import Vk, Squad
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,CreateView
from urllib.parse import parse_qs
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
from urllib.parse import parse_qs
import vk_api
from .vk_api import get_name_from_vk
from django.views import View
import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from vk_api.exceptions import VkApiError
from django.contrib.messages.views import SuccessMessageMixin
class HomeView(View):
    def get(self, request):
        super_users_count = User.objects.filter(is_superuser=True).count()
        users_count = Vk.objects.count()
        squad = Squad.objects.count()

        context = {
            'users_count': users_count,
            'super_users_count': super_users_count,
            'squad': squad,
        }
        return render(request, 'index.html', context)


class VkRegView(SuccessMessageMixin, CreateView):
    model = Vk
    form_class = VkForm
    template_name = 'registrations.html'
    success_url = reverse_lazy('reg')
    success_message = "Токен успешно обновлен"
    
    def form_valid(self, form):
        url_parameters = parse_qs(form.cleaned_data['vk'].split('#')[-1])
        access_token = url_parameters.get('access_token', [None])[0]
        user_id = url_parameters.get('user_id', [None])[0]
        first_name, last_name = get_name_from_vk(access_token, user_id)
        existing_token = Vk.objects.filter(id_vk=user_id).first()
        

        
        if existing_token:
            if existing_token.token_vk == access_token:
                form.add_error('vk', 'Токен доступа уже существует.')
                return self.form_invalid(form)
            existing_token.token_vk = access_token
            existing_token.save()
            return redirect(self.success_url)
        else:
            form.instance.token_vk = access_token
            form.instance.id_vk = user_id
            form.instance.first_name = first_name
            form.instance.last_name = last_name
            form.save()

        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
        return self.success_message
    
    def get_success_url(self):
        return reverse('vkApi', kwargs={'pk': self.object.pk})



class UserProfileView(View):
    def get(self, request, pk):
        vk_user = get_object_or_404(Vk, pk=pk)
        first_name, last_name = get_name_from_vk(vk_user.token_vk,vk_user.id_vk)
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()



        context = {
            'first_name': first_name,
            'last_name': last_name,
            'current_date': current_date,
            'current_time': current_time,
        }
        return render(request, 'vkApi.html', context)





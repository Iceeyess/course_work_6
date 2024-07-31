from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from .apps import MailingConfig
from mailing.models import Mailing
from django.urls import reverse_lazy
from datetime import datetime
from pytz import timezone
from config.settings import TIME_ZONE, TOPIC_TUPLE
from .forms import MailingForm

# Create your views here.
topic_name = MailingConfig.name


class MainTemplateView(TemplateView):
    template_name = f'{topic_name}/index.html'


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    paginate_by = 4
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            client = form.save()
            client.owner = self.request.user
            client.save()
            return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        now = datetime.now(timezone(TIME_ZONE))  # Временная зон
        if form.is_valid():
            if (self.get_object().date_time_attempt < self.get_object().date_time_threshold and
                    self.get_object().date_time_threshold > now):
                # mail = Mailing.objects.get(pk=self.get_object().pk)
                # Mailing.objects.filter(pk=self.get_object().pk).update(status='В ожидании')
                # mail.status = 'В ожидании'
                # mail.save(update_fields=['status'])
                print(self.get_object().date_time_attempt, self.get_object().date_time_threshold, now)
                mail = form.save()
                mail.status = 'В ожидании'
                mail.save()
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForm
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    extra_context = {'topic_name': topic_name,  # Для возврата в меню
                     'TOPIC_TUPLE': TOPIC_TUPLE
                     }
    success_url = reverse_lazy('mailing:mailing_list')
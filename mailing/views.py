from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DetailView, DeleteView
from .apps import MailingConfig
from mailing.models import Mailing
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.
topic_name = MailingConfig.name


class MainTemplateView(TemplateView):
    template_name = f'{topic_name}/index.html'


class MailingListView(ListView):
    model = Mailing
    paginate_by = 4


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('date_time_first_try', 'period', 'message', 'client')
    extra_context = {'topic_name': topic_name}  # Для возврата
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            send_mail(
                'Subject here',
                'Here is the message.',
                '21cfk8lf6gbp@mail.ru',
                ['ice_eyes@mail.ru'],
                fail_silently=False,
            )
        return super().form_valid(form)



class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('date_time_first_try', 'period', 'message', 'client', )
    extra_context = {'topic_name': topic_name}  # Для возврата
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing
    fields = ('date_time_first_try', 'period', 'message', 'client', )
    extra_context = {'topic_name': topic_name}  # Для возврата


class MailingDeleteView(DeleteView):
    model = Mailing
    extra_context = {'topic_name': topic_name}  # Для возврата
    success_url = reverse_lazy('mailing:mailing_list')
from django.shortcuts import render
from .models import Event, Establishment, Band
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


def home(request):
    return render(request, 'home.html', {})


def sign_in(request):
    return render(request, 'registration/login.html', {})


def sign_up(request):
    return render(request, 'signup.html', {})


class CreateBandView(LoginRequiredMixin, CreateView):
    model = Band
    fields = ['web_link', 'playlist',
              'email', 'mobile', 'image']
    template_name = 'band/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBandView, self).form_valid(form)

    def get_success_url(self):
        # Overrided method
        return reverse('band_detail', kwargs={'pk': self.object.pk})


class CreateEstablishmentView(LoginRequiredMixin, CreateView):
    model = Establishment
    fields = ['name', 'address', 'email',
              'mobile', 'image']
    template_name = 'establishment/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEstablishmentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('establishment_detail', kwargs={'pk': self.object.pk})


class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'band', 'state',
              'date', 'description', 'establishment']
    template_name = 'event/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateEventView, self).form_valid(form)

    def get_success_url(self):
        return reverse('event_detail', kwargs={'pk': self.object.pk})


class BandDetail(DetailView):
    model = Band
    template_name = 'band/detail.html'


class ListEstablishment(ListView):
    model = Establishment
    template_name = 'establishment/list.html'
    context_object_name = 'list_establishment'


class ListBand(ListView):
    model = Band
    template_name = 'band/list.html'
    context_object_name = 'band_list'


class ListEvent(ListView):
    model = Event
    template_name = 'event/list.html'
    context_object_name = 'event_list'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.all().order_by('-date')

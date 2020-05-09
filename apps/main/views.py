from django.shortcuts import render
from .models import Event, Establishment, Band
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


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
        return reverse('band_detail', kwargs={'pk':self.object.pk})


class EditBandView(UpdateView):
    model = Band
    fields = ['name', 'web_link', 'playlist',
              'email', 'mobile', 'image']
    template_name = 'band/edit.html'
    success_url = reverse_lazy('home')


class BandDetail(DetailView):
    model = Band
    template_name = 'band/detail.html'

class EstablishmentDetail(DetailView):
    model = Establishment
    template_name = 'establishment/detail.html'


class EditEstablishmentView(UpdateView):
    model = Establishment
    fields = ['name', 'address',
              'email', 'mobile', 'image']
    template_name = 'establishment/edit.html'

    success_url = reverse_lazy('home')


class EventDetail(DetailView):
    model = Event
    template_name = 'event/detail.html'

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


class EditEventView(UpdateView):
    model = Event
    fields = ['name', 'band',
              'state', 'date', 'description']
    template_name = 'event/edit.html'

    success_url = reverse_lazy('home')



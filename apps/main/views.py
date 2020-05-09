from django.shortcuts import render
from .models import Event, Establishment, Band
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

def home(request):
    return render(request, 'home.html', {})


def search(request):
    return render(request, 'search.html', {})


def sign_in(request):
    return render(request, 'registration/login.html', {})


def sign_up(request):
    return render(request, 'signup.html', {})


class CreateBandView(LoginRequiredMixin, CreateView):
    model = Band
    fields = ['name', 'web_link', 'playlist',
              'email', 'mobile', 'image']
    template_name = 'band/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBandView, self).form_valid(form)

    def get_success_url(self):
        # Overrided method
        return reverse('band_detail', kwargs={'pk': self.object.pk})


class EditBandView(UserPassesTestMixin, UpdateView):
    model = Band
    fields = ['name', 'web_link', 'playlist',
              'email', 'mobile', 'image']
    template_name = 'band/edit.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        band = Band.objects.filter(pk=self.kwargs['pk']).first()
        return band != None and self.request.user.pk == band.user.pk


class BandDetail(DetailView):
    model = Band
    template_name = 'band/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        band = self.model.objects.get(pk=self.kwargs["pk"])
        events = Event.objects.filter(band=band).order_by('-date')
        context["list_events"]=events
        return context

class EditEstablishmentView(UserPassesTestMixin, UpdateView):
    model = Establishment
    fields = ['name', 'address',
              'email', 'mobile', 'image']
    template_name = 'establishment/edit.html'

    success_url = reverse_lazy('home')

    def test_func(self):
        establishment = Establishment.objects.filter(pk=self.kwargs['pk']).first()
        return establishment != None and self.request.user.pk == establishment.user.pk


class EstablishmentDetail(DetailView):
    model = Establishment
    template_name = 'establishment/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        establishment = self.model.objects.get(pk=self.kwargs["pk"])
        events = Event.objects.filter(user=establishment.user).order_by('-date')
        context["list_events"]=events
        return context

class EventDetail(DetailView):
    model = Event
    template_name = 'event/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        est = Establishment.objects.get(user=self.object.user)
        context['establishment'] = est
        return context


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


class DeleteEvent(UserPassesTestMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('home')
    template_name = 'event/confirm_delete.html'

    def test_func(self):
        event = Event.objects.filter(pk=self.kwargs['pk']).first()
        return event != None and\
                self.request.user.pk == event.user.pk


class DeleteBand(UserPassesTestMixin, DeleteView):
    model = Band
    success_url = reverse_lazy('home')
    template_name = 'band/confirm_delete.html'

    def test_func(self):
        band = Band.objects.filter(pk=self.kwargs['pk']).first()
        return band != None and self.request.user.pk == band.user.pk


class EditEventView(UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['name', 'band',
              'state', 'date', 'description']
    template_name = 'event/edit.html'

    success_url = reverse_lazy('home')

    def test_func(self):
        event = Event.objects.filter(pk=self.kwargs['pk']).first()
        return event != None and self.request.user.pk == event.user.pk


class DeleteEstablishment(UserPassesTestMixin, DeleteView):
    model = Establishment
    success_url = reverse_lazy('home')
    template_name = 'establishment/confirm_delete.html'

    def test_func(self):
        establishment = Establishment.objects.filter(pk=self.kwargs['pk']).first()
        if establishment != None and \
                self.request.user.pk == establishment.user.pk:
            remove_events(self.request.user)
            return True
    
def remove_events(user):
    events = Event.objects.filter(user=user)
    for event in events:
        event.delete()

        return establishment != None and \
               self.request.user.pk == establishment.user.pk

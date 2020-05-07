from django.shortcuts import render
from .models import Event, Establishment, Band
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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

class DeleteBand( UserPassesTestMixin, DeleteView):
    model = Band
    success_url = reverse_lazy('home')

    def test_func(self):
        if self.request.user.id == int(self.kwargs['pk']):
            return True


class DeleteEstablishment(UserPassesTestMixin, DeleteView):
    model = Establishment
    success_url = reverse_lazy('home')
    template_name = 'establishment/establishment_confirm_delete.html'
    def test_func(self):
        establishment = Establishment.objects.filter(pk=self.kwargs['pk']).first()
        if establishment != None and \
                self.request.user.pk == establishment.user.pk:
            return True









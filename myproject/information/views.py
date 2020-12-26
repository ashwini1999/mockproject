from information.models import Clientdetails,Projectdetails,User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView,DetailView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ClientForm,ProjectForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from dal import autocomplete

# Create your views here.

def Projectcount(request):
    current_user = request.user
    user_data = current_user.id
    # print(user_data)
    for project_data in Projectdetails.objects.all():
        for user_info in project_data.userdata.filter(id=user_data):
            user_names= user_info
            user=Projectdetails.objects.values_list('projectname', flat=True).filter(userdata=user_names)
            return render(request,  'information/count.html', {'user_project': user,'names':user_names})

# region #--------START OF CLIENT------

@method_decorator(login_required, name='dispatch')
class AddClient(CreateView):
    model = Clientdetails
    form_class = ClientForm
    template_name = 'information/client.html'

    def form_valid(self, form):
        client = form.save(commit=False)
        client.created_by = self.request.user
        client.save()
        messages.success(self.request, 'saved successfully')
        return redirect('add_client')

    def get_context_data(self, **kwargs):
        kwargs['clients'] = Clientdetails.objects.filter().order_by(('-created_at'))
        return super(AddClient, self).get_context_data(**kwargs)

@method_decorator(login_required, name='dispatch')
class EditClient(UpdateView):
    model = Clientdetails
    form_class = ClientForm
    template_name = 'information/client.html'

    def form_valid(self, form):
        client = form.save(commit=False)
        client.updated_by = self.request.user
        client.save()
        messages.success(self.request, 'updated successfully')
        return redirect('add_client')

    def get_context_data(self, **kwargs):
        kwargs['clients'] = Clientdetails.objects.filter().order_by(('-created_at'))
        return super(EditClient, self).get_context_data(**kwargs)


@login_required
def DeleteClient(request, pk):
    client = get_object_or_404(Clientdetails, pk=int(pk))
    client.delete()
    messages.success(request, 'deleted successfully')
    return redirect('add_client')

# endregion
# --------END OF CLIENT-------

class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


# region #--------START OF PROJECT-------

@method_decorator(login_required, name='dispatch')
class AddProject(CreateView):
    model = Projectdetails
    form_class = ProjectForm
    template_name = 'information/project.html'
   

    def form_valid(self, form, **kwargs):
        project = form.save(commit=False)
        project.created_by = self.request.user
        project.save()
        form.save_m2m()
        messages.success(self.request, 'saved successfully')
        return redirect('add_project')

    def get_context_data(self, **kwargs):
        kwargs['projects'] = Projectdetails.objects.filter().order_by(('-created_at'))
        return super(AddProject, self).get_context_data(**kwargs)
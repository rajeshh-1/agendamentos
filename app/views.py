from django.shortcuts import redirect, render
from app.forms import ContactForm, ContactGroupForm
from app.models import Contact, ContactGroup
from django.db.models.functions import Lower
from django.core.paginator import Paginator
# Create your views here.
class ViewContactGroup:

    def list(request):
        data = {}
        data['db'] = ContactGroup.objects.all()
        return render(request, './contactGroup/list.html', data)

    def form(request):
        data = {}
        data['form'] = ContactGroupForm()
        return render(request, './contactGroup/form.html', data)

    def create(request):
        form = ContactGroupForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/contact-group/list')

    def view(request, pk):
        data = {}
        data['db'] = ContactGroup.objects.get(pk=pk)
        return render(request, './contactGroup/view.html', data)


    def edit(request, pk):
        data = {}
        data['db'] = ContactGroup.objects.get(pk=pk)
        data['form'] = ContactGroupForm(instance=data['db'])
        return render(request, './contactGroup/form.html', data)

    def update(request, pk):
        data = {}
        data['db'] = ContactGroup.objects.get(pk=pk)
        form = ContactGroupForm(request.POST or None, instance=data['db'])
        if form.is_valid():
            form.save()
            return redirect('/contact-group/list')

    def delete(request, pk):
        db = ContactGroup.objects.get(pk=pk)
        db.delete()
        return redirect('/contact-group/list')


class ViewContact:

    def home(request):
        data = {}
        search = request.GET.get('search')
        all = []
        if search:
            all = Contact.objects.filter(name__icontains=search).order_by(Lower('name'))
        else:
            all = Contact.objects.all().order_by(Lower('name'))
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')

        data['db'] = paginator.get_page(pages)
        return render(request, 'index.html', data)

    def form(request):
        data = {}
        data['form'] = ContactForm()
        return render(request, './contact/form.html', data)

    def list(request):
        data = {}
        data['db'] = Contact.objects.all()
        return render(request, './contact/list.html', data)

    def create(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/contact/list')

    def view(request, pk):
        data = {}
        data['db'] = Contact.objects.get(pk=pk)
        return render(request, './contact/view.html', data)


    def edit(request, pk):
        data = {}
        data['db'] = Contact.objects.get(pk=pk)
        data['form'] = ContactForm(instance=data['db'])
        return render(request, './contact/form.html', data)

    def update(request, pk):
        data = {}
        data['db'] = Contact.objects.get(pk=pk)
        form = ContactForm(request.POST or None, instance=data['db'])
        if form.is_valid():
            form.save()
            return redirect('/contact/list')

    def delete(request, pk):
        db = Contact.objects.get(pk=pk)
        db.delete()
        return redirect('/contact/list')

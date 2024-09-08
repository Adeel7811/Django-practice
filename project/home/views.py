from django.views.generic.list import ListView
from django.views import View
from .models import Books
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ContactForm
# Create your views here.

# class HelloView(View):
#     def get(self, request):
#         return HttpResponse("Hello! world!")

class BookListView(ListView):
    model = Books
    template_name = "home/book.html"
    context_object_name = 'Books'

class BookDetails(View):
    def get(self,request, id):
        book = get_object_or_404(Books, pk=id)
        return render(request, 'home/details.html', {'book':book})


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'home/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ContactForm()  
        return render(request, 'home/contact.html', {'form': form})

        

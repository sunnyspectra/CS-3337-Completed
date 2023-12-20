from django.http import HttpResponse
from django.shortcuts import render
from .models import MainMenu
from .forms import BookForm
from django.http import HttpResponseRedirect
from .models import Book
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.shortcuts import redirect
from .models import Cart, CartItem, Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Book, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Book  # Replace with your actual model import

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def index(request):
    #return HttpResponse("<h1>Hello</h1>")
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )
def aboutus(request):

    return render(request,
                  'bookMng/aboutus.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )
@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'form': form,
                      'submitted' : submitted
                  }
                  )
@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'range_5': range(1, 6),  # Add this line to pass the range to the template
                  }
                  )

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def remove_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        # Add a success message or any other post-deletion logic
        return redirect('displaybooks')  # Redirect to the displaybooks page

@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )

@login_required(login_url=reverse_lazy('login'))
def messages(request):
    submitted = False
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Assign the user
            message.save()
            return HttpResponseRedirect('/messages?submitted=True')
    else:
        form = MessageForm()

    # Check if form was submitted successfully
    if 'submitted' in request.GET:
        submitted = True

    # Get all messages from the database
    messages = Message.objects.all()

    return render(request, 'bookMng/messages.html', {
        'item_list': MainMenu.objects.all(),
        'form': form,
        'submitted': submitted,
        'messages': messages,
    })


def search(request):
    books = Book.objects.filter(name__contains=request.GET.get('search'))
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/search.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  }
                  )

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    # Update the quantity if needed
    # cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect('/cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()
    return render(request, 'cart.html', {'cart_items': items})




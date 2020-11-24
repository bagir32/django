from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Book
from .forms import BookCreate


# Create your views here.
def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})
    #x = []
    #for i in range(10):
    #   x.append(i)
    #return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))


def index(request):
    shelf = Book.objects.all()
    return render(request, 'templates/book/library.html', {'shelf': shelf})


def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'templates/book/upload_form.html', {'upload_form':upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')

    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')

    return render(request, 'templates/book/upload_form.html', {'upload_form':book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')

    book_sel.delete()
    return redirect('index')

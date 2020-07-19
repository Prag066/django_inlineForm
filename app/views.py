from django.shortcuts import render,HttpResponseRedirect
from django.forms import formset_factory,inlineformset_factory
from .forms import ArticalForm
from .models import Author,Book
import datetime

def Index(request):
    ArticleFormSet = formset_factory(ArticalForm,extra=2,max_num=2,can_delete=True)
    if request.method == "POST":
        formset = ArticleFormSet(
            request.POST,request.FILES,
            initial=[
            {
                'title':'title',
                'pub_date':datetime.date.today()
            }
        ]
        )
        if formset.is_valid():
            pass
        # return render(request,'index.html',{'form':formset})
    else:
        formset = ArticleFormSet()
    return render(request,'index.html',{'formset':formset})


def inlineModelFromView(request,author_id=1):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=('title',))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST,request.FILES,instance=author)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('')
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request,'inlineform.html',{'formset':formset})
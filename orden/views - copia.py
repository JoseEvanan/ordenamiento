from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'orden/post_list.html', {'posts':posts})

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        v1= str(request.POST['entrada'])
        sal= mergesort(v1)
        
        print sal
        if form.is_valid():
            post = form.save(commit=False)
            post.salida=sal
            post.author = request.user
            print request.user
            print type(request.user)
            post.save()
            return redirect('orden.views.post_detail', pk=post.pk)
     

    else:
        form = PostForm()
        return render(request, 'orden/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'orden/post_detail.html', {'post': post})


#SORT DE PYTHON -TIM SORT ??? - mergesort??

def mergesort(x):
    result = []
    if len(x) < 2:
        return x
    medio = int(len(x)/2)
    der = mergesort(x[:medio]) 
    izq = mergesort(x[medio:]) 
    print str(izq) + "//" + str(der) 
    while (len(der) > 0) or (len(izq) > 0):
        if (len(der) > 0) and (len(izq) > 0):
            if der[0] > izq[0]:
                result.append(izq[0])
                izq.pop(0)
            else:
                result.append(der[0])
                der.pop(0)
        elif len(izq) > 0:
            for i in izq:
                result.append(i)
                izq.pop(0)
        else:
            for i in der:
                result.append(i)
                der.pop(0)
    return result
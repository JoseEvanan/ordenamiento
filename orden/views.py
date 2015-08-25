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
        sal= evaluacion(v1)
        
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




def evaluacion(elemento):
    valor=elemento
    print type(valor)
    cadena=valor.split(",")
    print cadena
    print type(cadena)
    tam=len(cadena)

    ent=[]
    cad=[]
    pos=[]

    for x in xrange(0,tam):
        try:
            ent.append(int(cadena[x]))
            pos.append(1)
            print "entero"
        except:
            cad.append(str(cadena[x]))
            pos.append(0)
            print "cadena"
    
    cad.sort(key=str.lower)
    ent.sort()
    string=""
    cadena[:]=[]

    i=0
    j=0
    for x in xrange(0,tam):
        if(pos[x]==0):
            cadena.append(cad[i])
            i=i+1   
        else:
            cadena.append(ent[j])
            j=j+1   
    print cadena[0]

    for y in xrange(0,tam):
        print tam
        print y
        if(y==0):
            string= str(cadena[y])
        else:
            string=string+","+str(cadena[y])
        print string
    return string 
        
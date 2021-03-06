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
        print type(v1)
        

        sal=""            
        for y in xrange(0,len(v1)):
            if(y==0):
                sal= str(v1[y])
            else:
                sal=sal+","+str(v1[y])

        
        
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

def evaluacion(elemento):
    valor=elemento
    cadena=valor.split(",")

    tam=len(cadena)
    print (str(tam) + "tamano")
    ent=[]
    cad=[]
    pos=[]
    cont=0
    for x in xrange(0,tam):
        cadena[x]=cadena[x].strip()
        if(len(cadena[x])!=0):
            try:
                ent.append(int(cadena[x]))
                pos.append(1)
            except:
                cad.append(str(cadena[x]))
                pos.append(0)
        else:
            cont=cont+1
    tam=tam-cont              
    cad.sort(key=str.lower)
    ent.sort()
    string=""
    cadena[:]=[]
    i=0
    j=0
    x=0
    for x in xrange(0,tam):
        print x
        if(pos[x]==0):
            cadena.append(cad[i])
            i=i+1   
        else:
            cadena.append(ent[j])
            j=j+1 

    
    for y in xrange(0,tam):
        if(y==0):
            string= str(cadena[y])
        else:
            string=string+","+str(cadena[y])

    return string 
        
## comparadores en un clases y patrones de diseno8
def mergesort(slista):
    
    x=[]
    for i in xrange(0,len(slista)):
        x.append(int(slista[i]))
    result = []
    der=[]
    izq=[]
    if len(x) < 2:
        return x
    medio = int(len(x)/2)
    der = mergesort(x[:medio]) 
    izq = mergesort(x[medio:]) 
    print str(izq) + "//" + str(der) 
    while (len(der) > 0) or (len(izq) > 0):
        if len(der) > 0 and len(izq) > 0:
            if der[0] > izq[0]:
                result.append(izq[0])
                print type(izq)
                izq.pop(0)
            else:
                result.append(der[0])
                print type(der)
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
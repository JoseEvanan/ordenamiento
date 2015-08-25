from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
# Create your tests here.

class PostTestCase(TestCase):
	def setUp(self):
		user = auth.authenticate(username='jose', password='maucaylle')
		jorge = auth.authenticate(username='jorge', password='jorge')
		print "setup"
		Post.objects.create(author=self.user ,title="ejemplo4" , entrada="c,d,a,4,2,1" , salida="a,c,d,1,2,4")
		Post.objects.create(author=self.jorger ,title="ejemplo5" , entrada="f,2,d,r,9,g,5,s,3,1,c,6",salida="c,1,d,f,2,g,3,r,5,6,s,9")

def test_autor(self):
	post1=Post.objects.get(author=self.user)
	print "autor"
	assertEqual(post1.title,"ejemplo4")

def test_resultado(self):
	post2=Post.objects.get(author=self.user ,entrada="f,2,d,r,9,g,5,s,3,1,c,6")
	print "resultado"
	assertEqual(post.salida,"c,1,d,f,2,g,3,r,5,6,s,9")


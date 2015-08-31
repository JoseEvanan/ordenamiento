from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
# Create your tests here.

class PostTestCase(TestCase):
	def setUp(self):
		print "setup"
		Post.objects.create(title="test1" , entrada="22,21,19,18,15,14,9,7,5" , salida="5,7,9,14,15,18,19,21,22")
		Post.objects.create(title="test2" , entrada="",salida="")
		Post.objects.create(title="test3" , entrada="1,2,3,4,5,6,7,8,9,10" , salida="1,2,3,4,5,6,7,8,9,10")
	
	def test_autor(self):
		post1=Post.objects.get(title="test1")
		self.assertEqual(post1.entrada,"22,21,19,18,15,14,9,7,5")

	def test_resultado(self):
		post2=Post.objects.get(entrada="22,21,19,18,15,14,9,7,5")
		self.assertEqual(post2.salida,"5,7,9,14,15,18,19,21,22")

	def test_blanco(self):
		post3=Post.objects.get( entrada="")
		self.assertEqual(post3.salida,"")

	def test_string(self):
		post4=Post.objects.get(title="test3")
		comparar=post4.__str__()
		self.assertEqual(comparar,"test3")

 

  


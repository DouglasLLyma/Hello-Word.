from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, n1 ,n2 ):
    return HttpResponse ('<h1>Hello {} de {} anos, resultado = {}.</h1>'.format(nome, idade,(n1 + n2)))
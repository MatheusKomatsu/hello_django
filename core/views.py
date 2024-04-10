from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} com {} anos </h1>'.format(nome,idade))

def soma(request,number1,number2):
    return HttpResponse('<h1>O resultado da soma é {} </h1>'.format(number1 + number2))

def sub(request,number1,number2):
    return HttpResponse('<h1>O resultado da subtração é {} </h1>'.format(number1 - number2))

def multi(request,number1,number2):
    return HttpResponse('<h1>O resultado da multiplicação é {} </h1>'.format(number1 * number2))


def div(request,number1,number2):
    return HttpResponse('<h1>O resultado da divisão é {} </h1>'.format(number1 / number2))




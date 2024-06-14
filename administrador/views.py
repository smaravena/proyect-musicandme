from django.shortcuts import render


def homeadm(request):
    context = {}
    return render(request,'administrador/test.html',context)


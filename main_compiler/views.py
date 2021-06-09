from django.shortcuts import render, redirect
import sys
from main_compiler.models import Savedata
# Create your views here.


def index(request):

    return render(request, 'index.html',)


def runcode(request):

    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open("code.txt", 'w')
            sys.stdout.write("#Welcome to the VP's Online Compiler \n")
            sys.stdout.write("#This Complier created by Vikrant Patil \n")

            exec(codeareadata)

            sys.stdout.close()

            sys.stdout = original_stdout

            output = open('code.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e

    else:
        print("no")

    return render(request, 'index.html', {'code': codeareadata, "output": output})


def save(request):
    # pass

    if request.method == "POST":
        print('hiii')
        name = request.POST['Name']
        codeareadata = request.POST['codearea']
        outputdata = request.POST.get('output')

        print(name, codeareadata, outputdata)

        b = Savedata(name=name, codedata=codeareadata,
                     outputarea=outputdata)
        b.save()
        return redirect('compiler')
    else:
        print('no')

    return render(request, 'index.html')

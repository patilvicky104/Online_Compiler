from django.shortcuts import render, redirect

import sys
# Create your views here.


def index(request):
    # if request.method == 'POST':
    #     form = CompilerForm(request.POST)

    #     if form.is_valid():
    #         # form.save()
    #         pass
    #     return redirect('compiler')

    # else:
    #     form = CompilerForm()

    return render(request, 'index.html',)


def runcode(request):

    if request.method == "POST":
        codeareadata = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open("code.txt", 'w')

            exec(codeareadata)

            sys.stdout.close()

            sys.stdout = original_stdout

            output = open('code.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e

    return render(request, 'index.html', {'code': codeareadata, "output": output})

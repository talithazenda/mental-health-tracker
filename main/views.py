from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245554',
        'name': 'Talitha Zenda Shakira',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
from django.shortcuts import render


def upload(request):
    # form = request(request.POST or None, request.FILES or None)
    # print(form)


    return render(request, 'home.html')
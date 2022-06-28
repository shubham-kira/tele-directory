from django.shortcuts import render

def master_list(request):
    return render(request, 'teleList/master_list.html', {})

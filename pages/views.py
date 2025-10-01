from django.shortcuts import render


def page_1(request):
    # design a counter of visits (request.session works a lot like a dictionary)
    # strongly discouraged to use complicated data structures or instances
    # keep things simple; id, primary key, store key e.g. redis
    visitor_count = request.session.get('dci_student_visits', 0)
    # increase the value of visits
    request.session['dci_student_visits'] = visitor_count + 1
    return render(request, 'pages/page-1.html')


def page_2(request):
    return render(request, 'pages/page-2.html')
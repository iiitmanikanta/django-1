from django.shortcuts import render
# from .models import Message


def home(request):
    # messages = Message.objects.order_by('order')
    a=1
    if a==1:
        if 2==2:
            print "for quantifycode"
    messages = ['a', 'b', 'c']
    context_dict = {
        'messages': messages
    }
    return render(request, 'starter_app/home.html', context_dict)

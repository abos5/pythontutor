from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


def get_name(request):

    if request.method == 'POST':
        return render(request, 'webblog/thanks.html')
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = NameForm()
    return render(request, 'webblog/name.html', {'form': form})


def thanks(request):
    return render(request, 'webblog/thanks.html')


# Create your views here.

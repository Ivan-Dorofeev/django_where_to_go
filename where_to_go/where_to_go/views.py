from django.shortcuts import render


def main(request):
    context = {'title': 'Здесь скоро появится карта. Ура!', }
    return render(request, 'index.html', context)

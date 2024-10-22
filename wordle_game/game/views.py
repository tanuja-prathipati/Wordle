from django.shortcuts import render
from django.http import JsonResponse

# Sample list of words
WORD_LIST = ['apple', 'grape', 'peach', 'berry', 'mango']

def index(request):
    return render(request, 'game/index.html')

def play(request):
    if request.method == 'POST':
        guess = request.POST.get('guess', '').lower()
        if guess in WORD_LIST:
            response = {'status': 'success', 'message': 'Correct guess!'}
        else:
            response = {'status': 'error', 'message': 'Try again!'}
        return JsonResponse(response)
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

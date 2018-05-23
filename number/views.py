from django.shortcuts import render
from number.factorization import check_number


# Response generation
def number(request):
    data = ''
    if request.method == 'POST':
        # Generating the result of work with the number
        data = check_number(request.POST.get("number"))
    return render(request, 'number/number.html', locals()) # Generate response page

from django.shortcuts import render

# Create your views here.
def privacy_policy(request):
    return render(request, 'info_docs/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'info_docs/terms.html')

def about_us(request):
    return render(request, 'info_docs/about_us.html')

def contact_us(request):
    return render(request, 'info_docs/contact_detail.html')
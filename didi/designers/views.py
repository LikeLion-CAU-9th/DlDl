from django.shortcuts import render,redirect, get_object_or_404
from .models import Designer_Info

# 파일 업로드 관련
# from django.http import HttpResponseRedirect
# from .forms import UploadFileForm


# Create your views here.
def designer_home(request):

    designer_infos = Designer_Info.objects.all()
    return render(request, 'designer_home.html', {'designer_infos':designer_infos})

def detail(request, id):
    
    info = get_object_or_404(Designer_Info, pk = id)
    return render(request, 'detail.html', {'info':info})

def new(request):
    return render(request, 'new.html')

def portfolio_upload(request):
    return render(request, 'portfolio_upload.html')

def create(request):
    if request.method == 'POST':
        new_designer = Designer_Info()
        new_designer.cover_image = request.FILES['cover']
        new_designer.name = request.POST['name']
        new_designer.personerity_pick_1 = request.POST['personerity_1']
        new_designer.personerity_pick_2 = request.POST['personerity_2']
        new_designer.personerity_pick_3 = request.POST['personerity_3']
        new_designer.introduce = request.POST['introduce']
        new_designer.save()
    return redirect('detail', new_designer.id)





# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})
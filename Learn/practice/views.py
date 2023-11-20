from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect


from .models import Project,Video
from .forms import Video_form 
from .models import Item

def home (request):
    projects = Project.objects.all()
    return render(request, 'practice/home.html',{'projects':projects})



def index(request):
    all_video=Video.objects.all()
    form = Video_form()
    if request.method == 'POST':
        form = Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Upload successful")
        # else:
    return render(request, 'practice/index.html', {'form':form, 'all_video':all_video})    


def my_template(request):
    # Query the Item model to get the video object
    item = Item.objects.all()  # Assumes you have an Item model with a video_url field
    return render(request, 'practice/my_template.html', {'item': item})


# def upload_item(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Extract the uploaded video file from the form
#             video_file = request.FILES.get('video_file')
            
#             # Save the video file to a temporary location
#             # You can use Django's `default_storage` to handle file storage
#             video_path = default_storage.save('temp/' + video_file.name, video_file)

#             # Construct the video URL or file path and save it to the model
#             video_url = default_storage.url(video_path)
#             item = form.save(commit=False)
#             item.video_url = video_url
#             item.save()
            
#             # Redirect to success page or perform other actions
#             return HttpResponseRedirect('/success/')
#     else:
#         form = ItemForm()
#     return render(request, 'upload_item.html', {'form': form})

# # # frank
# Frank@07


# Create your views here.

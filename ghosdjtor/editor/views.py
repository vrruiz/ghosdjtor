import os.path
import json

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import UploadedImage


def index(request):
    """ Main index. Editor view. """
    # Render editor
    body = render_to_string('editor.html', {})
    data = {
       'body': body
    }
    # Render page layout
    return render(request, 'index.html', data)

@csrf_exempt
def postimage(request):
    """ Called by ghost/dropzone via POST to upload images """
    image_data = { 'type': 'error' }
    if request.method == 'POST':
        # Save image
        image = UploadedImage(image = request.FILES['file'])
        image.save()
        print(image, image.image.url)
        image_data = {
            'type' : 'success',
            'path' : image.image.url,
            'id': 'dropzone'
        }
    # Return response in JSON format
    json_data = json.dumps(image_data)
    return HttpResponse(json_data, content_type='application/json')

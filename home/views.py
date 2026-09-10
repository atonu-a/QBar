import base64
import io
from django.shortcuts import render, redirect
import qrcode

def index(request):
    qr_image = None
    url = ''
    file_name = ''

    if request.method == "POST":
        url = request.POST.get('url', '').strip()
        file_name = request.POST.get('filename', '').strip() or 'qrcode'

        if url:
            img = qrcode.make(url)
            

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            qr_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {
        'qr_image': qr_image,
        'url': url,
        'filename': file_name
    }
    return render(request, 'base.html', context)
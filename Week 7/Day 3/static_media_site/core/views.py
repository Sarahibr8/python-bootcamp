from django.shortcuts import render
from django.conf import settings


def upload_document(request):
    uploaded_file = None

    if request.method == "POST":
        uploaded_file = request.FILES.get("file")

        if uploaded_file:
            file_path = settings.MEDIA_ROOT / uploaded_file.name

            with open(file_path, "wb+") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

    return render(
        request,
        "core/upload.html",
        {
            "uploaded_file": uploaded_file,
            "media_url": settings.MEDIA_URL,
        },
    )
from django.shortcuts import render
from .models import Post


def feed(request):
    if request.method == "POST":
        username = request.POST.get("username")
        description = request.POST.get("description")
        uploaded_file = request.FILES.get("image")

        if uploaded_file:
            allowed_types = ["image/jpeg", "image/png"]

            if uploaded_file.content_type not in allowed_types:
                return render(request, "core/feed.html", {
                    "error": "Only JPG, JPEG, and PNG files are allowed."
                })

            Post.objects.create(
                username=username,
                description=description,
                image=uploaded_file
            )

    posts = Post.objects.all()

    return render(request, "core/feed.html", {
        "posts": posts
    })
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()

    return render(request, "core/feed.html", {
        "posts": Post.objects.all()
    })
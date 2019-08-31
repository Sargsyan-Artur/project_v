from django.shortcuts import render
from .forms import PostForm, CommentForm
from .models import PostFile, Comments
from django.contrib import messages
from django.views.generic.edit import BaseCreateView
from django.http import HttpResponse
from django.views import generic
from polls import models

# import sys
# sys.path.insert(1, '/users_registration')
# print(sys.path)
# import sys
# from pathlib import Path
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# print(sys.path)

# pandas ip  poxelov


class FileDownloadApload(generic.CreateView, BaseCreateView):
    form_class = PostForm
    template_name = "home.html"

    def post(self, request):
        user_id = request.user.id
        user = models.MyUser.objects.get(pk=user_id)
        all_upload_files = user.postfile_set.all().order_by("-pk")

        if request.method == "POST":

            form = PostForm(request.POST, request.FILES)
            name = str(request.FILES["file"])

            if form.is_valid():

                user_file = user.postfile_set.create(
                    file=request.FILES["file"], name=name
                )
                form = PostForm()
                messages.info(request, "Thanks for upload. You are uploaded file.")

                return HttpResponse(
                    render(
                        request,
                        "home.html",
                        {"form": form, "all_upload_files": all_upload_files},
                    )
                )
        else:

            form = PostForm()

        return render(
            request, "home.html", {"form": form, "all_upload_files": all_upload_files}
        )

    def get(self, request):

        form = PostForm()
        user_id = request.user.id
        user = models.MyUser.objects.get(pk=user_id)
        all_upload_files = user.postfile_set.all().order_by("-pk")

        if request.method == "GET":

            if "id" in request.GET:

                file_id = request.GET["id"]
                try:
                    fileload = all_upload_files.get(id=file_id)
                except PostFile.DoesNotExist:
                    return HttpResponse({"Error": "Record does not exist"}, status=404)

                filesize = fileload.file.size
                response = HttpResponse(fileload.file, content_type="")
                response["Content-Disposition"] = "attachment; filename=%s" % fileload
                response["Content-Length"] = filesize
                return response
            else:
                return HttpResponse(
                    render(
                        request,
                        "home.html",
                        {"form": form, "all_upload_files": all_upload_files},
                    )
                )


def add_comment_to_post(request, pk):
    form = CommentForm()
    try:

        file = PostFile.objects.get(pk=pk)

    except PostFile.DoesNotExist:
        return HttpResponse({"Error": "Record does not exist"}, status=404)

    all_comm_this_post = file.comments_set.all().order_by("-pk")

    context = {"file": file, "form": form, "all_comm_this_post": all_comm_this_post}
    if request.method == "POST":

        coment_db = file.comments_set.create(
            comment=request.POST["comment"], author=request.user.first_name
        )
        form = CommentForm()
        context = {"file": file, "form": form, "all_comm_this_post": all_comm_this_post}

        return render(request, "comment.html", context)

    else:

        return render(request, "comment.html", context)

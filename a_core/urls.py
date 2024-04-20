
from django.contrib import admin
from django.urls import path, include
from a_posts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home-page"),
    path("ask_question/", question_create_view, name="ask-question"),
    path("edit_question/<str:pk>", question_edit_view, name="edit-question"),
    path("delete_question/<str:pk>", delete_question_view, name="delete-question"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
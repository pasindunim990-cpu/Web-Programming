# Add to the existing myApp/urls.py.
path("students/<int:page>/", views.studentlist, name="studentlist"),
path("modules/", views.modulelist, name="modulelist"),

# In the project urls.py, append this for development media serving:
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

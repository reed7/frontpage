from django.shortcuts import render
from .models import MyProfile
from .utils import svg_path


def index(request):
    profile = MyProfile.objects.get(pk=1)
    qa = profile.questionanswer_set.filter(display=True).order_by('display_order')

    return render(request, "home_page/index.html", {"profile": profile, "qa": qa, "svg_path": svg_path})

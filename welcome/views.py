import os
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    hostname = os.getenv("HOSTNAME", "unknown")
    PageView.objects.create(hostname=hostname)
    print("print debug")
    logger.info("info log message")
    return render(
        request,
        "welcome/index.html",
        {
            "hostname": hostname,
            "database": database.info(),
            "count": PageView.objects.count(),
        },
    )


def health(request):
    return HttpResponse(PageView.objects.count())

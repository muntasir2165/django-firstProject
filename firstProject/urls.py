"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstApp import views as fa
# from firstApp.views import display
# from firstApp.views import displayDateTime
from quoteApp import views as qa
# from quoteApp.views import displayQuote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', fa.display),
    # path('hello/', display),
    path('datetime/', fa.displayDateTime),
    # path('datetime/', displayDateTime),
    path('quote', qa.displayQuote)
    # path('quote', displayQuote)
]

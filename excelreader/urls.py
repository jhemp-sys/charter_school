"""excelreader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from datareader.views import WebView, DataUploadView, DataTableView
from datareader.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('upload/', upload, name='data_upload'),
    path('upload/first', first_post, name='first_post'),
    path('upload/bs', bs_post, name='bs_post'),
    path('upload/pl', pl_post, name='pl_post'),
    # path('table/bs', bs, name='bs'),
    # path('table/', DataTableView.as_view(), name='data_table'),
]

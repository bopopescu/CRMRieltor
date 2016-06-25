# -*- coding: utf-8 -*-


"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from homes import views
from notes.views import note_add, note_del, note_edit
from setting_street.views import street_list, add_street, delete_street

urlpatterns = [
    # site
    url(r'^$', views.homes, name='homes'),
    url(r'^objects$', views.object_list, name='objects'),
    url(r'^buyers$', views.buyers_list, name='buyers'),
    url(r'^maklers$', views.maklers_list, name='maklers'),
    url(r'^arendators$', views.arendators_list, name='arendators'),
    url(r'^buyers/add_buyer$', views.add_buyer, name='add_buyer'),
    url(r'^arendators/add_arendator$', views.add_arendator, name='add_arendator'),
    url(r'^objects/add_object$', views.add_object, name='add_object'),
    url(r'^tasking$', views.tasking, name='tasking'),
    url(r'^setting$', views.setting, name='setting'),
    url(r'^meeting$', views.meeting, name='meeting'),
    # end site
    # start settings urls
    url(r'^setting/setting_street$', street_list, name='setting_street'),
    # end settings urls

    # admin
    url(r'^admin/', admin.site.urls),
    # endadmin

    # request notes
    url(r'^note_add$', note_add),
    url(r'^note_del$', note_del),
    url(r'^note_edit$', note_edit),
    # end request notes

    # start request street
    url(r'^setting/add_street$', add_street),
    url(r'^setting/delete_street$', delete_street),
    # end request street

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

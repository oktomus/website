from django.conf.urls import * 
from .views import WorkDetail, WorkList

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)$', 
        WorkDetail.as_view(),
        name='work_detail'
        ),
    url(r'^$', 
        WorkList.as_view(),
        name='work_list'
        ),
]
from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    #feature reports
    url(r'report/(\d+)', sdc_analysis, name='sdc_analysis'), #user requested sdc analysis 
)

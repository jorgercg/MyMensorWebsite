"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from mymwebsite import mymviews
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    url(r'^google2b3414d31be14bcd.html$', mymviews.gglowner, name='gglowner'),
]

urlpatterns += i18n_patterns(
    url(r'^$', mymviews.index, name='index'),
    url(r'^terms/', mymviews.terms, name='terms'),
    url(r'^privacy/', mymviews.privacy, name='privacy'),
    url(r'^docs/', mymviews.docs, name='docs'),
    url(r'^videos/', mymviews.videos, name='videos'),
    url(r'^faq/', mymviews.faq, name='faq'),
    url(r'^download/', mymviews.download, name='download'),
    url(r'^cases/$', mymviews.cases, name='cases'),
    url(r'^cases/genusemediaplan/$', TemplateView.as_view(template_name="cases/genusemediaplan.html"), name='genusemediaplan'),
    url(r'^cases/followingjobs/$', TemplateView.as_view(template_name="cases/followingremotejobs.html"), name='followingremotejobs'),
    url(r'^cases/usingyourowndata/$', TemplateView.as_view(template_name="cases/usingyourowndata.html"), name='usingyourowndata'),
    url(r'^cases/routessales/$', TemplateView.as_view(template_name="cases/routessales.html"), name='routessales'),
    url(r'^cases/routestrademarketing/$', TemplateView.as_view(template_name="cases/routestrademarketing.html"), name='routestrademarketing'),
    url(r'^cases/routesservices/$', TemplateView.as_view(template_name="cases/routesservices.html"), name='routesservices'),
    url(r'^cases/routessecurity/$', TemplateView.as_view(template_name="cases/routessecurity.html"), name='routessecurity'),
    url(r'^cases/transparencygeneral/$', TemplateView.as_view(template_name="cases/transparencygeneral.html"), name='transparencygeneral'),
    url(r'^cases/transparencypub/$', TemplateView.as_view(template_name="cases/transparencypub.html"), name='transparencypub'),
    url(r'^cases/transparencyngo/$', TemplateView.as_view(template_name="cases/transparencyngo.html"), name='transparencyngo'),
    url(r'^cases/transparencyhousmng/$', TemplateView.as_view(template_name="cases/transparencyhousmng.html"), name='transparencyhousmng'),
    url(r'^cases/productivity/$', TemplateView.as_view(template_name="cases/productivity.html"), name='productivity'),
    url(r'^cases/shipmaintenance/$', TemplateView.as_view(template_name="cases/shipmaintenance.html"), name='shipmaintenance'),
    url(r'^cases/profsurveyors/$', TemplateView.as_view(template_name="cases/profsurveyors.html"), name='profsurveyors'),
    url(r'^cases/businessideas/$', TemplateView.as_view(template_name="cases/businessideas.html"), name='businessideas'),
    url(r'^cases/assetmanagement/$', TemplateView.as_view(template_name="cases/assetmanagement.html"), name='assetmanagement'),
    url(r'^howto/$', mymviews.howto, name='howto'),
    url(r'^howto/genusemediaplan/$', TemplateView.as_view(template_name="howto/genusemediaplan.html"),name='genusemediaplanhowto'),
    url(r'^howto/followingjobs/$', TemplateView.as_view(template_name="howto/followingremotejobs.html"),name='followingremotejobshowto'),
    url(r'^howto/usingyourowndata/$', TemplateView.as_view(template_name="howto/usingyourowndata.html"),name='usingyourowndatahowto'),
    url(r'^howto/routessales/$', TemplateView.as_view(template_name="howto/routessales.html"), name='routessaleshowto'),
    url(r'^howto/routestrademarketing/$', TemplateView.as_view(template_name="howto/routestrademarketing.html"), name='routestrademarketinghowto'),
    url(r'^howto/routesservices/$', TemplateView.as_view(template_name="howto/routesservices.html"), name='routesserviceshowto'),
    url(r'^howto/routessecurity/$', TemplateView.as_view(template_name="howto/routessecurity.html"), name='routessecurityhowto'),
    url(r'^howto/transparencygeneral/$', TemplateView.as_view(template_name="howto/transparencygeneral.html"), name='transparencygeneralhowto'),
    url(r'^howto/transparencypub/$', TemplateView.as_view(template_name="howto/transparencypub.html"), name='transparencypubhowto'),
    url(r'^howto/transparencyngo/$', TemplateView.as_view(template_name="howto/transparencyngo.html"), name='transparencyngohowto'),
    url(r'^howto/transparencyhousmng/$', TemplateView.as_view(template_name="howto/transparencyhousmng.html"), name='transparencyhousmnghowto'),
    url(r'^howto/productivity/$', TemplateView.as_view(template_name="howto/productivity.html"), name='productivityhowto'),
    url(r'^howto/shipmaintenance/$', TemplateView.as_view(template_name="howto/shipmaintenance.html"), name='shipmaintenancehowto'),
    url(r'^howto/profsurveyors/$', TemplateView.as_view(template_name="howto/profsurveyors.html"), name='profsurveyorshowto'),
    url(r'^howto/businessideas/$', TemplateView.as_view(template_name="howto/businessideas.html"), name='businessideashowto'),
    url(r'^howto/assetmanagement/$', TemplateView.as_view(template_name="howto/assetmanagement.html"), name='assetmanagementhowto'),
    url(r'^howto/setupautoshare/$', TemplateView.as_view(template_name="howto/setupautoshare.html"), name='setupautosharehowto'),

)

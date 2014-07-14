from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse, Http404
import datetime
from django.conf import settings
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.forms.forms import NON_FIELD_ERRORS
from apps.epa.forms import *
from django.views.decorators.cache import cache_control

def login(request):
	form = LoginForm()
	values={
		'form':form,
	}
	return render_to_response('accounts/login.html',values, context_instance = RequestContext(request))
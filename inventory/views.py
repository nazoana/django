from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from forms import ContactForm
from models import Commodity

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the inventory index.")
    full_path = request.get_full_path()
    return render_to_response('inventory/index.html',  
    	{'hw': "hello, there!" + (full_path), 'home_tab': "selected"},
    	context_instance=RequestContext(request)
    	)


def incoming(request):
    return render_to_response('inventory/incoming.html',  
    	{'incoming_tab': "selected"},
    	context_instance=RequestContext(request)
    	)
    	
def dispatching(request):
    return render_to_response('inventory/dispatching.html',  
    	{'dispatching_tab': "selected"},
    	context_instance=RequestContext(request)
    	)
    	
def returning(request):
    return render_to_response('inventory/returning.html',  
    	{'returning_tab': "selected"},
    	context_instance=RequestContext(request)
    	)

def reports(request):
    return render_to_response('inventory/reports.html',  
    	{'reports_tab': "selected"},
    	context_instance=RequestContext(request)
    	)
    	
def help(request):
    return render_to_response('inventory/help.html',  
    	{'help_tab': "selected"},
    	context_instance=RequestContext(request)
    	)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

# This is where search form data is posted and processed.
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term !')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters !')
		else:
			commodities = Commodity.objects.filter(name__icontains=q)
			return render_to_response('inventory/search_result.html', 
										{'commodities': commodities, 'query': q}, 
										context_instance=RequestContext(request)
									)
	return render_to_response('inventory/search.html', 
								{'errors': errors}, 
								context_instance=RequestContext(request)
							)
							
def contact(request):
	c = {}
	c.update(csrf(request))
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#send_mail(
			#	cd['subject'],
			#	cd['message'],
			#	cd.get('email', 'noreply@mercycorps.org'),
			#	['mkhan@mercycorps.org'],
			#)
			#return HttpResponse("Your post was submitted successfully!")
			return HttpResponseRedirect('/inventory/search/')
		else:
			return render_to_response('inventory/contact.html',
										{'form': form, 'contact_link': "selected"}, 
										context_instance=RequestContext(request)
									)
	else:
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
		return render_to_response('inventory/contact.html', 
									{'form': form, 'contact_link': "selected"}, 
									context_instance=RequestContext(request),
								)

def faq(request):
    return render_to_response('inventory/faq.html',  
    	{'faq_link': "selected"},
    	context_instance=RequestContext(request)
    	)
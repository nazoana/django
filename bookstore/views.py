from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from models import Book
from forms import ContactForm

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the inventory index.")
    full_path = request.get_full_path()
    return render_to_response('bookstore/index.html',  
    	{'hw': "Bookstore....  " + (full_path)},
    	context_instance=RequestContext(request)
    	)

# This is for displaying the display_meta http request.	
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
# This is for displaying the search_form html page
#def search_form(request):
#    return render_to_response('bookstore/search_form.html', 
#    	{'hw': "Bookstore....  " },
#    	context_instance=RequestContext(request)
#    	)

# This is where search form data is posted and processed.
def search(request):
#	if 'q' in request.GET:
#		message = 'You searched for: %r' % request.GET['q']
#	else:
#		message = 'You submitted an empty form.'
#	return HttpResponse(message)
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('bookstore/search_result.html', 
										{'books': books, 'query': q}, 
										context_instance=RequestContext(request)
									)
	return render_to_response('bookstore/search_form.html', 
								{'errors': errors}, 
								context_instance=RequestContext(request)
							)
	#return HttpResponse('Please submit a search term.')
	
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
			return HttpResponseRedirect('/bookstore/search/')
		else:
			return render_to_response('bookstore/contact_form.html',
										{'form': form, 'hometab': "selected"}, 
										context_instance=RequestContext(request)
									)
	else:
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
		return render_to_response('bookstore/contact_form.html', 
									{'form': form, 'hometab': "selected"}, 
									context_instance=RequestContext(request),
								)
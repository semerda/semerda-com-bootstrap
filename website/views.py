"""

Using PEP 8 -- Style Guide for Python Code
http://www.python.org/dev/peps/pep-0008/

"""

# Django framework. Ref: http://www.djangobook.com/
from django.shortcuts            import render_to_response
from django.template             import RequestContext
from django.conf                 import settings

# Generate pseudo-random numbers. Ref: http://docs.python.org/library/random.html
import random

# Standard Python modules
from datetime                        import datetime


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def home_view(request):
    """ Render Homepage.

        Using Django's templates, template language & filters to format datetime
        Ref: https://docs.djangoproject.com/en/1.3/topics/templates/
        Templates are located under - app/templates/*
    """
    
    # Content to pass into template
    page_content_dict = {'server_node' : settings.SERVER_NODE}

    # Choose a random element - can add up to z chars, make sure associated template is available.
    # This is non sticky A/B testing so user can refresh page over and see new content.
    ab_test = random.choice('ab')

    # Inputs: template / dictionary of values / context instance
    return render_to_response('website/home_%s.html' % ab_test,
                              page_content_dict,
                              context_instance=RequestContext(request))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def about_view(request):
    """ Render Survey page.

        Using Django's templates, template language & filters to format datetime
        Ref: https://docs.djangoproject.com/en/1.3/topics/templates/
        Templates are located under - app/templates/*
    """

    # Content to pass into template
    page_content_dict = {'server_node' : settings.SERVER_NODE}

    # Inputs: template / dictionary of values / context instance
    return render_to_response('website/about.html',
                              page_content_dict,
                              context_instance=RequestContext(request))

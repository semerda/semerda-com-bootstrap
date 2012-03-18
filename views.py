"""

Using PEP 8 -- Style Guide for Python Code
http://www.python.org/dev/peps/pep-0008/

"""

# Django framework. Ref: http://www.djangobook.com/
from django.shortcuts            import render_to_response
from django.template             import RequestContext
from django.conf                 import settings


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def exception_404_view(request):
    """ Render 404 (page not found)
        Ref: https://docs.djangoproject.com/en/dev/topics/http/views/#the-404-page-not-found-view

        TODO: Make this a funny page. Inspiration here: http://www.quora.com/What-are-the-funniest-404-pages
    """

    # Content to pass into template
    page_content_dict = {}

    # Inputs: template / dictionary of values / context instance
    return render_to_response('404.html',
                              page_content_dict,
                              context_instance=RequestContext(request))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def exception_error_view(request):
    """ Render 500 (server error)
        Ref: https://docs.djangoproject.com/en/dev/topics/http/views/#the-500-server-error-view
    """

    # Content to pass into template
    page_content_dict = {}

    # Inputs: template / dictionary of values / context instance
    return render_to_response('500.html',
                              page_content_dict,
                              context_instance=RequestContext(request))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
def exception_permission_denied_view(request):
    """ Render 403 (HTTP Forbidden)
        Ref: https://docs.djangoproject.com/en/dev/topics/http/views/#the-403-http-forbidden-view
    """

    # Content to pass into template
    page_content_dict = {}

    # Inputs: template / dictionary of values / context instance
    return render_to_response('403.html',
                              page_content_dict,
                              context_instance=RequestContext(request))

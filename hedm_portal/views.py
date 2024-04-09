from django.shortcuts import render


def example_view(request):
    """
    Example custom view for rendering custom things.

    Rendering any template off of base should be fine, for example:

    ```
     

    {% extends "globus-portal-framework/v2/base.html" %}

    {% block body %}

    <h1>Hello {{context}}</h1>

    {% endblock %}

    
    ```
    Please note the ALCF portal uses custom branding, and any changes rendered locally will
    change according to branding there. Double check any styling changes before deployment.
    """
    context = {'context': 'world'}
    return render(request, 'gmca/globus-portal-framework/v2/example-view.html', context)

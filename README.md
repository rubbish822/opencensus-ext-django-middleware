# opencensus-ext-django-middleware

fork from https://github.com/census-instrumentation/opencensus-python/tree/master/contrib/opencensus-ext-django


`OpenCensus Django Integration
============================================================================

|pypi|

.. |pypi| image:: https://badge.fury.io/py/opencensus-ext-django.svg
   :target: https://pypi.org/project/opencensus-ext-django/

Installation
------------

::

    pip install opencensus-ext-django
    pip install opencensus-ext-django-middleware

Usage
-----

For tracing Django requests, you will need to add the following line to
the ``MIDDLEWARE_CLASSES`` section in the Django ``settings.py`` file.

.. code:: python

    MIDDLEWARE_CLASSES = [
        ...
        'django_ext_middleware.middleware.OpencensusMiddleware',
    ]

And add this line to the ``INSTALLED_APPS`` section:

.. code:: python

    INSTALLED_APPS = [
        ...
        'opencensus.ext.django',
    ]

Additional configuration can be provided, please read
`Customization <https://github.com/census-instrumentation/opencensus-python#customization>`_
for a complete reference.

.. code:: python
### use JaegerExporter example
````
OPENCENSUS_TRACE = {
        # 'SAMPLER': 'opencensus.trace.samplers.probability.ProbabilitySampler',
        # 'REPORTER': 'opencensus.trace.print_exporter.PrintExporter',
        # 'EXPORTER': 'opencensus.ext.zipkin.trace_exporter.ZipkinExporter',
        'EXPORTER': 'opencensus.ext.jaeger.trace_exporter.JaegerExporter',
        # 'PROPAGATOR': 'opencensus.trace.propagation.google_cloud_format.'
        #               'GoogleCloudFormatPropagator',
}


OPENCENSUS_TRACE_PARAMS = {
    # 'BLACKLIST_PATHS': ['/_ah/health'],
    # 'GCP_EXPORTER_PROJECT': None,
    # 'SAMPLING_RATE': 0.5,
    'JAEGER_EXPORTER_SERVICE_NAME': 'service_name',
    'JAEGER_EXPORTER_AGENT_HOST_NAME': 'localhost',
    'JAEGER_EXPORTER_AGENT_PORT': 6831,
    'JAEGER_SET_ATTRIBUTES': 'your_app.your_set_attributes',
}

References
----------

* `OpenCensus Project <https://opencensus.io/>`_

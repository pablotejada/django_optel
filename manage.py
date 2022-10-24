#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



def instrument():
    import json

    from opentelemetry import trace as OpenTelemetry
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
        OTLPSpanExporter,
    )
    from opentelemetry.instrumentation.django import DjangoInstrumentor
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider, sampling
    from opentelemetry.sdk.trace.export import (
        BatchSpanProcessor,
    )
    
    DjangoInstrumentor().instrument()


    #ONLY NECESSARY IF ONEAGENT NOT INSTALLED
    token = 'dt0c01.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    env_url = 'https://fvj02804.sprint.dynatracelabs.com'
    print("INSTRUMENTING")
    merged = dict()
    for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json"]:
        try:
            data = ''
            with open(name) as f:
                data = json.load(f if name.startswith("/var") else open(f.read()))
                merged.update(data)
        except:
            pass

    merged.update({
        "service.name": "python-quickstart", #TODO Replace with the name of your application
        "service.version": "1.0.1", #TODO Replace with the version of your application
    })
    resource = Resource.create(merged)

    tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)
    OpenTelemetry.set_tracer_provider(tracer_provider)

    tracer_provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter(
            # TODOO WITH OA running on the same host:
            endpoint="http://localhost:14499/otlp/v1/traces",

            # WITHOUT OA RUNNING:
            #TODOO Replace <URL> to your SaaS/Managed-URL
            #endpoint= f"https://{env_id}.live.dynatrace.com/api/v2/otlp/v1/traces",
            # endpoint= f"{env_url}/api/v2/otlp/v1/traces",
            # headers={
            #     #TODOO Replace <TOKEN> with your API Token with `Ingest OpenTelemetry traces` permission
            #     "Authorization": f"Api-Token {token}" 
            # },
        )))


def main():
    """Run administrative tasks."""
    
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    
    #instrument with OpTel
    instrument()
    # os.environ.setdefault(
    #     "DJANGO_SETTINGS_MODULE", "instrumentation_example.settings"
    # )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

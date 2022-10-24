# Django OpenTelemetry

Django sample application with Open Telemetry Integration to view traces. Followed documentation <a href="https://www.dynatrace.com/support/help/extend-dynatrace/opentelemetry/opentelemetry-traces/opentelemetry-ingest/opent-python" target="_blank">documentation</a>

* See requirements.txt 
* If OneAgent is running in the machine, no need to configure endpoints or tokens

To view pyhton modules list:
```
pip list
```

To install modules

```
pip install -r requirements.txt
```

To run django app instrumented:

```
opentelemetry-instrument python manage.py runserver
```



# Trace Examples in Dynatrace:
Failed Request trace
![image](https://user-images.githubusercontent.com/70635871/196998312-881f8379-6862-4a47-9f76-2323ab3d3ca9.png)


Failed Request Trace
![image](https://user-images.githubusercontent.com/70635871/196998466-414c3f02-5635-4a57-8787-011722db8dbb.png)

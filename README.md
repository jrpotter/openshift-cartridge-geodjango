Openshift GeoDjango Cartridge
=============================
[Version 1.0.0 - 08/07/2014]

The following was an experiment on the inner workings of the PaaS OpenShift. The following cartridge is installable as is, but will not allow one to run a functional django project so be warned!

Though there are quickstart Python 3/Django 1.6 cartridges and quickstarts, I did not come across any functional GeoDjango cartridges/quickstarts. This cartridge aims to remediate this. Included are the following components

* GeoDjango
* PostgreSQL Extensions
  * PostGIS
  * Tiger
* GeoIP

as well as a template GeoDjango project (setup with [dj-static](https://github.com/kennethreitz/dj-static) and gunicorn for quick startup.

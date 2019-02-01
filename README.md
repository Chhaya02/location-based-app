# Location-Based-App
Django and GeoDjango to build a location-based web application.
Nearby Shops will be listed, by using the GeoDjango.

## Prerequisites
  - Python(3.5, +)
  - Django web framework (2.1.+)
  - GeoDjango dependencies : 
        GEOS,
        GDAL,
        PROJ.4
  - PostgreSQL and PostGIS database along with Docker
  
  Refer to the docs for detailed instructions about how to install these dependencies on [macOS](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/#macos) and [Windows](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/#windows).  
  
## Installing
 ### Installing Python 3
  You can simply head to the official website and download the binaries for your operating system.
 
 ### Installing GeoDjango Dependencies
  sudo aptitude install gdal-bin libgdal-dev
  sudo aptitude install python3-gdal
  sudo aptitude install binutils libproj-dev

### Setting up a Spatial Database With PostgreSQL and PostGIS
  docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4

## Setting up Your Project
  - Creating a Virtual Environment
  - Installing Django
  - Creating a Django Project 
      django-admin.py startproject project_name
  - Configuring the PostgreSQL Database
    1.Open the settings.py file and add django.contrib.gis.db.backends.postgis as the engine with the credentials for the           PostGIS database you configured earlier:
    ```
    DATABASES = {
      'default': {
          'ENGINE': 'django.contrib.gis.db.backends.postgis',
          'NAME': 'gis',
          'USER': 'user001',
          'PASSWORD': '123456789',
          'HOST': 'localhost',
          'PORT': '5432'
      }
    }
  
**Note: You need to change the database credentials accordingly if you didn’t specify the same credentials when running the Docker container.**

### PostgreSQL adapter for Python
  pip install psycopg2-binary

### Adding GeoDjango
  Open the settings.py file and locate the INSTALLED_APPS array. Then add the 'django.contrib.gis' module:
  ```
    INSTALLED_APPS = [
      # [...]
      'django.contrib.gis'
  ]
```
### Creating a Django Application
  python manage.py startapp app_name
```
  INSTALLED_APPS = [
    # [...]
    'shops'
  ]
```
### Creating a Django Model

### Creating the Database Tables
  - python manage.py makemigrations
  - python manage.py migrate

### Adding a Super User
  - python manage.py createsuperuser

### Adding Initial Data
  You need some initial demo data for your application, but instead of manually adding data, you can use a data migration.
  Before creating a migration, let’s first get some real-world data from [integrated Wizard](https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard), which makes it easy to create queries.
  
  In our case, we want to get all the shops in a city. Simply click on the [Wizard button](http://overpass-turbo.eu/). A small window will pop up. In the text field, write a query like “shop in Indore” and click on build and run query.
  
  Next, click on the export button and click on download/copy as raw OSM data to download a JSON file that contains the raw OSM data. Save the file as data.json in your project’s root folder.

Now, let’s create an empty migration for importing the content of the data.json file in the database, using the following command:
 - python manage.py makemigrations shops --empty

See migration file, use of load_data() and migrations.RunPython(load_data) is used to export data.
Now, Run the migrate commenad
- python manage.py migrate

### Displaying Nearby Shops
  Use a html file to rander the details.

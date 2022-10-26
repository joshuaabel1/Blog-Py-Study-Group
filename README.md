# Blog-Py-Study-Group
<pre>Practice for the group of study</pre>


# Como levantar el proyecto:



<pre>Primero debemos crear nuestro entorno virtual.
</pre>

``` bash  

python -m virtualenv venv 

```

<pre>una vez tenemos nuestro entorno, pasamos a instalar el "requirements.txt" .
</pre>

``` bash  

pip install -r requirements.txt

```

<pre>Ahi estaran las librerias necesarias para que nuestro proyecto funciona .
Lo siguiente es correr nuestras migraciones y archivos estaticos.
</pre>

``` bash  
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

```

<pre>Despues de esto creamos nuestro usuario admin.
</pre>

``` bash  
python manage.py createsuperuser

```
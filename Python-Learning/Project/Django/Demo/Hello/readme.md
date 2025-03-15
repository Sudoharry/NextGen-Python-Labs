# Commands:

1) For creating a django project use this command

``` django-admin startproject Hello ```

- 


2) For running the web server(django)

``` python manage.py runserver```

- This is the command to execute Django's management script, which provides various tools for managing your project.



3) How to create a app in django project

``` python3 manage.py startapp home ```

- This is a subcommand specifically designed to create a new Django application within your project.


4) Add a urls.py in the app like in the project directory


5) How the URL dispatchers works:

- Firstly, you have to create a URL with path in urls.py and then you have create a function in the view.


6) Render

- It's generally use to render the template.(static file and template)


7) Template and Static folder will be added in the root project.

- Static files -> Images, css
- You can access the static files on <ip-address:port>/static/test.txt
- You will access the text message that's written in the test file within the static folder.

Note: Static folder is accessible to public. So, never share any senstive text or information within the static file.
      If anyone can use static/ and attempt to see the file, then it won't be able to access the files within the folder.

8) Within the settings.py files we will copy the os.path.join(BASE_DIR, "static") and change static to templates and add it to DIR= [] within the templates.


9) ``` python manage.py makemigrations ``` 

- This command will see if there has been any changes recently made. If you've changed any database schema

10)  ``` python manage.py migrate ```

- Migrate is used to get the default table like authentication. (There were no table for authentication)
- Django provides default authentication which can be used for login
- You have to make read/write access to table authentication.

11) ``` python3 manage.py createsuperuser ```

- You can create the superuser which can be acts as admin. All you need to do is, make a username add strong password with more than 8 characters.
- So,django will store this username and password in the user table within the db.sqlite


12) 
    ``` 
        admin.site.site_header = "UMSRA Admin"
        admin.site.site_title = "UMSRA Admin Portal"
        admin.site.index_title = "Welcome to UMSRA Researcher Portal" 
    ```

  - We can make this 3 changes in the title and name of the admin portal, we can add to admin project -> url.py 
  - Above the url patterns and below the imports in the main project. 

13) The base.html and index.html can be rendered through {% block %} {% endblock}

- Use 

{% extends 'base.html'%}

{% block title%}Home{% endblock title%}

{% block body%}This is body block{% endblock body%}



14) Nav Bar in bootstrap website

15) Admin title, head and body change - ('https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html')

16) Carousel 

- Use <div class="container">
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="..." alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="..." alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="..." alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>

17) Unsplash.com (Search: source.unsplash.com)


18) Jumbotron

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


9) 


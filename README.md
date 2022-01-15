# Codentino: A Django Blog Project
Live Demo: [codentino.com](https://codentino.com)

## Features at a glance:
- **Posts:** Markdown support, publish/unpublish, autocreated table of contents
- **Series:** A blog post can belong to one or many series. Order of posts can be determined for each series.
- **Tags:** Posts and series can be tagged. Nested tags are possible.
- **Comments:** Possible to comment and reply comments (nested comments) for authorized users.
- **Social Login:** You can login via google in the demo. But thanks to `django-allauth` this can be extended.
- **More:** Sitemap, pages.

## Developement Setup
 - The prerequisite for this guide is to have `docker-compose` installed.
 - By following the guide under this title you will have `django` and `postres` services. The `nginx`, `letsencrypt` and `certbot` services are the subject of "Production Setup".

 ```bash
 # Make sure docker-compose is installed.
 docker-compose -v
 ```

 ```bash
 # Clone the repo
 git clone https://github.com/kutver/codentino.git
 ```

 ```bash
 # Enter the repository
 cd codentino
 ```

 ```bash
 # Create your .env file using example.env
 cp example.env .env
 ```

 ```bash
 # Edit your .env file using your favorite text editor, for instance vim.
 vim .env
 ```

 ```bash
 # Build the project
 docker-compose up --build
 ```

 See your blog: http://127.0.0.1:8000/

 Once the application is setup in your local environment, you will want to create a superuser.
 
 The application is designed to be developed inside the container.
 
 Therefore, run the following command from inside the `/codentino/django` folder in the container.

 ```bash
 # Inside the container
 python manage.py createsuperuser
 ```
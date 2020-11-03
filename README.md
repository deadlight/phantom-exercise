# Phantom code exercise: Karl Williams

```
 .-.
(o o) boo!
| O \
 \   \
  `~~~'
```

## Running the project

### Dependencies and virtual environment

For simple, modern dependency and virtual environment management, I use [poetry]().
Poetry is the recommended method of running the project in development.

### Setup

Once you have installed poetry a virtual environment with the requirements installed can be created with:

`poetry install`

Your server IP and domain name must be added to `phantomnames/settings.py`. For example, the configuration for my server is already included, you can add to or replace these values:

```
ALLOWED_HOSTS = [
    '87.98.218.185', # Karl's development server
    'forbiddencartographies.com', # Karl's development server domain
]
```

### Running the development server

Open a shell into your poetry environment:

`poetry shell`

Inside that shell navigate to the `phantomnames` directory (`cd phantomnames`) and run the following commands:

Migrate the database ready for use:

`./manage.py migrate`

Create a superuser (you will be prompted to enter various user details by the script):

`./manage.py createsuperuser`

Now you can run the development server:

`./manage.py runserver 0.0.0.0`

In a browser, login to:

`[YOUR SERVER DOMAIN]/admin`

And login with the credentials your created with `createsuperuser`

### Configuring Google sign-in

One limitation of the current setup is that it must be accessible publically on a domain (not an IP address) in order to use the Google OAuth service.

This also needs some configuration in Google's developer dashboard and your Django admin as outlined in sections 7 and 8 of this [django-allauth setup guide](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5)

## Live version

A hosted version of the project is running on [my server](http://forbiddencartographies.com:8080/)

Note: this is the Django development server running with debug enabled and is not a proposed production deployment

## Technology & architecture choices

I have chosen to use a fairly out-of-the-box setup of Django with the addition of the `django-allauth` module to handle Google authentication.

This project could be augmented with JavaScript on the frontend but I deemed it unnecessary for this simple proof of concept. Likewise, I have used simple HTML templates and a barebones CSS stylesheet to make the site useable and less ugle to stare at during development.

I decided to keep the first name and last name associated with a Phantom Name user-entered rather than pulled from the Google authentication to allow for a more customisable experience and so that fewer user details are needed from Google.


## Improvements & next steps

### Testing

I have not written any testing for this application. This is mostly due to time constraints. I usually find that writing tests first is a good practice and facilitiates faster development but, in this case, I was seeing the prohect as more of an experimental prototype where complete end-to-end functionality for be more beneficial.

I would prefer to have extensive pytest scripts testing various use-cases, starting with mocking expected behaviour of the views.

### Linting & CI

My preference is for linting to be carried out in-editor, on commit and on submission of a PR as part of the CI process.

I have been linting manually or using IDE plugins but this would become cumbersome with a longer-term project or a collaborateive environment and so my next priority would be addding automated linting to the porject.

### Deployment

The project so far only uses the Django development server, which is not suitable for production deployment.

As Google App Engine was the preferred solution and given that I have no experience with GAE, I would be very keen deploy using it but thought that it was outside of the time limit I could give this exercise.

### Template repitition

The templates are simple and functional but I would like to reduce the amount of very similar HTML written in them. A good candidate for inclusion as a sub-template would be the "card" that ghosts appear in througout the site.

### Loading data

I have manually entered some ghosts into the Django admin but I have included a simple CSV representation of the data in the repository which I would plan to use as a useful set of data that could be imported for local development and used to create environments for testing.

### CSS

I wrote very simple CSS for this set of pages using what I think of as a "loosely [BEM](http://getbem.com/)" style but I would push for much more structure and a common language for design elements. I would consider using a preprocessor like Sass if the CSS got any more complicated to take advantage of time and complexity saving features.

Of course, there are many existing styling frameworks available and choice of styling would be influenced by such frameworks already in use by or endosed by the team or clients.

### JavaScript

I prefer to keep JavaScript as minimal as possible and, in this case, deceded that it was entirely unrequired for the first pass at this project. For functionality this simple, I would like to see JavaScript used to add enhancements to more simple HTML & CSS solutions that would remain as a fallback.

### Design & UX

This prototype has had a small consideration to being intuitive, following UX standards and having a pleasing and accessible design but I would like to use this prototype as a kicking-off point for a conversation with UI, UX and grpahic designers to come up with a beautiful solution.
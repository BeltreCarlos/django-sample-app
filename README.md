## README

Install Pipenv if you don't have it already

```bash
brew install pipenv
```

Create virtual env (from project root)

```bash
pipenv --three
```

Start shell within virtual env

```bash
pipenv shell
```

Run server

```
 python manage.py runserver
```

Running `coverage`(from `/api/`):

```bash
coverage run --source="." manage.py test

# Check coverage report
coverage report
```

Running migrations

```bash
# Create migrations after making changes to model
python manage.py makemigrations <ModelName>

python manage.py migrate
```

Create a SuperUser

```bash
python manage.py createsuperuser
```

Create new Project

```bash
django-admin startproject <ProjectName>
```

Create new App

```bash
django-admin startapp <AppName>
```

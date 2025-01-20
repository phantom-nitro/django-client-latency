# Getting Started(Dev)

```
git clone https://github.com/phantom-nitro/django-client-latency.git
```

## Create virtual environment and activate
```
cd django-client-latency
python -m venv venv
venv\Scripts\activate
```

## Install dependencies
```
pip install -r requirements.txt
cd theme/static_src/
npm install
cd ../..
```

## Create .env file(Dev)
```
DJANGO_SECRET_KEY=your-django-secret-key
DJANGO_SETTINGS_MODULE=ping_site.settings.dev
```

## Build TailwindCSS
```
python manage.py tailwind build
```

## Run the Django development server(open separate terminal in same directory)
```
python manage.py migrate
python manage.py runserver
```

Open http://localhost:8000 with your browser to see the result.

"""
Django test settings for edx_shopify project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'foobar'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'waffle',
    'openedx.core.djangoapps.site_configuration',
    'openedx.core.djangoapps.self_paced',
    'openedx.core.djangoapps.user_api',
    'openedx.core.djangoapps.content.course_overviews',
    'openedx.core.djangoapps.content.block_structure',
    'openedx.core.djangoapps.bookmarks',
    'student',
    'milestones',
    'course_modes',
    'config_models',
    'lms.djangoapps.verify_student',
    'celery_utils',
    'edx_shopify',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'edx_shopify_testdb.sqlite3',
        'ATOMIC_REQUESTS': True,
    }
}

ROOT_URLCONF = 'edx_shopify.urls'

WEBHOOK_SETTINGS = {
    'edx_shopify': {
        'shop_domain': 'example.com',
        'api_key': 'foobar',
    }
}

FEATURES = {
    'USE_MICROSITES': False,
}
MICROSITE_BACKEND = 'microsite_configuration.backends.filebased.FilebasedMicrositeBackend'  # noqa: E501
MICROSITE_TEMPLATE_BACKEND = 'microsite_configuration.backends.filebased.FilebasedMicrositeTemplateBackend'  # noqa: E501

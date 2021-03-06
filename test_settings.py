"""
Django test settings for edx_shopify project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import contracts
import tempfile
import os

from uuid import uuid4
from xmodule.modulestore import prefer_xmodules
from xmodule.x_module import XModuleMixin
from xmodule.modulestore.inheritance import InheritanceMixin
from xmodule.modulestore.edit_info import EditInfoMixin
from lms.djangoapps.lms_xblock.mixin import LmsBlockMixin

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
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'djcelery',
    'waffle',
    'openedx.core.djangoapps.site_configuration',
    'openedx.core.djangoapps.self_paced',
    'openedx.core.djangoapps.user_api',
    'openedx.core.djangoapps.content.course_overviews',
    'openedx.core.djangoapps.content.block_structure',
    'openedx.core.djangoapps.bookmarks',
    'openedx.core.djangoapps.catalog',
    'openedx.core.djangoapps.dark_lang',
    'openedx.core.djangoapps.video_pipeline',
    'openedx.features.course_duration_limits',
    'openedx.features.content_type_gating',
    'django_comment_common',
    'student',
    'milestones',
    'completion',
    'courseware',
    'course_modes',
    'config_models',
    'lms.djangoapps.verify_student',
    'celery_utils',
    'track',
    'eventtracking.django.apps.EventTrackingConfig',
    'experiments',
    'oauth2_provider',
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

USAGE_KEY_PATTERN = r'(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))'  # noqa: E501
ASSET_KEY_PATTERN = r'(?P<asset_key_string>(?:/?c4x(:/)?/[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))'  # noqa: E501
USAGE_ID_PATTERN = r'(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))'  # noqa: E501

COURSE_KEY_PATTERN = r'(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)'
COURSE_ID_PATTERN = COURSE_KEY_PATTERN.replace('course_key_string',
                                               'course_id')
COURSE_ENROLLMENT_MODES = {
    "audit": 1,
    "verified": 2,
    "professional": 3,
    "no-id-professional": 4,
    "credit": 5,
    "honor": 6,
}

ALL_LANGUAGES = ([u"en", u"English"],)

XQUEUE_INTERFACE = {
    "url": "https://sandbox-xqueue.example.com",
    "django_auth": {
        "username": "lms",
        "password": "***REMOVED***"
    },
    "basic_auth": ('foo', 'bar'),
}

BLOCK_STRUCTURES_SETTINGS = dict(
    COURSE_PUBLISH_TASK_DELAY=30,
    TASK_DEFAULT_RETRY_DELAY=30,
    TASK_MAX_RETRIES=5,
)

CELERY_ALWAYS_EAGER = True
HIGH_PRIORITY_QUEUE = 'edx.core.high'
DEFAULT_PRIORITY_QUEUE = 'edx.core.default'
LOW_PRIORITY_QUEUE = 'edx.core.low'
HIGH_MEM_QUEUE = 'edx.core.high_mem'
RECALCULATE_GRADES_ROUTING_KEY = LOW_PRIORITY_QUEUE
POLICY_CHANGE_GRADES_ROUTING_KEY = LOW_PRIORITY_QUEUE
POLICY_CHANGE_TASK_RATE_LIMIT = '300/h'

COMMON_TEST_DATA_ROOT = 'tmp'
DATA_DIR = tempfile.mkdtemp()

THIS_UUID = uuid4().hex[:5]
MONGO_PORT_NUM = int(os.environ.get('EDXAPP_TEST_MONGO_PORT', '27017'))
MONGO_HOST = os.environ.get('EDXAPP_TEST_MONGO_HOST', 'localhost')
CONTENTSTORE = {
    'ENGINE': 'xmodule.contentstore.mongo.MongoContentStore',
    'DOC_STORE_CONFIG': {
        'host': MONGO_HOST,
        'db': 'test_xcontent_{}'.format(THIS_UUID),
        'port': MONGO_PORT_NUM,
    }
}

DOC_STORE_CONFIG = {
    'host': 'localhost',
    'db': 'xmodule',
    'collection': 'modulestore',
    # If 'asset_collection' defined, it'll be used
    # as the collection name for asset metadata.
    # Otherwise, a default collection name will be used.
}
MODULESTORE = {
    'default': {
        'ENGINE': 'xmodule.modulestore.mixed.MixedModuleStore',
        'OPTIONS': {
            'mappings': {},
            'stores': [
                {
                    'NAME': 'split',
                    'ENGINE': 'xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore',  # noqa: E501
                    'DOC_STORE_CONFIG': DOC_STORE_CONFIG,
                    'OPTIONS': {
                        'default_class': 'xmodule.hidden_module.HiddenDescriptor',  # noqa: E501
                        'fs_root': DATA_DIR,
                        'render_template': 'edxmako.shortcuts.render_to_string',  # noqa: E501
                    }
                },
                {
                    'NAME': 'draft',
                    'ENGINE': 'xmodule.modulestore.mongo.DraftMongoModuleStore',  # noqa: E501
                    'DOC_STORE_CONFIG': DOC_STORE_CONFIG,
                    'OPTIONS': {
                        'default_class': 'xmodule.hidden_module.HiddenDescriptor',  # noqa: E501
                        'fs_root': DATA_DIR,
                        'render_template': 'edxmako.shortcuts.render_to_string',  # noqa: E501
                    }
                }
            ]
        }
    }
}

# These are the Mixins that should be added to every XBlock.  This
# should be moved into an XBlock Runtime/Application object once the
# responsibility of XBlock creation is moved out of modulestore -
# cpennington
XBLOCK_MIXINS = (LmsBlockMixin, InheritanceMixin,
                 XModuleMixin, EditInfoMixin)

# Allow any XBlock in the LMS
XBLOCK_SELECT_FUNCTION = prefer_xmodules

# Paths to wrapper methods which should be applied to every XBlock's FieldData.
XBLOCK_FIELD_DATA_WRAPPERS = ()

TRACK_MAX_EVENT = 0
DEBUG_TRACK_LOG = False
TRACKING_BACKENDS = {
    'logger': {
        'ENGINE': 'track.backends.logger.LoggerBackend',
        'OPTIONS': {
            'name': 'tracking'
        }
    }
}
EVENT_TRACKING_ENABLED = True
EVENT_TRACKING_BACKENDS = {
    'tracking_logs': {
        'ENGINE': 'eventtracking.backends.routing.RoutingBackend',
        'OPTIONS': {
            'backends': {
                'logger': {
                    'ENGINE': 'eventtracking.backends.logger.LoggerBackend',
                    'OPTIONS': {
                        'name': 'tracking',
                        'max_event_size': TRACK_MAX_EVENT,
                    }
                }
            },
            'processors': [
                {'ENGINE': 'track.shim.LegacyFieldMappingProcessor'},
                {'ENGINE': 'track.shim.PrefixedEventProcessor'}
            ]
        }
    },
    'segmentio': {
        'ENGINE': 'eventtracking.backends.routing.RoutingBackend',
        'OPTIONS': {
            'backends': {
                'segment': {'ENGINE': 'eventtracking.backends.segment.SegmentBackend'}  # noqa: E501
            },
            'processors': [
                {
                    'ENGINE': 'eventtracking.processors.whitelist.NameWhitelistProcessor',  # noqa: E501
                    'OPTIONS': {
                        'whitelist': []
                    }
                },
                {
                    'ENGINE': 'track.shim.GoogleAnalyticsProcessor'
                }
            ]
        }
    }
}
EVENT_TRACKING_PROCESSORS = []

SITE_NAME = 'localhost:8000'

EDX_ROOT_URL = ''

COURSE_MODE_DEFAULTS = {
    'bulk_sku': None,
    'currency': 'usd',
    'description': None,
    'expiration_datetime': None,
    'min_price': 0,
    'name': 'Audit',
    'sku': None,
    'slug': 'audit',
    'suggested_prices': '',
}

contracts.disable_all()

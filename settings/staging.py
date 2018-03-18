from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_MqkEKmeAamO8IWBasqpxuJNO')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_kLGpsYB2d5Ho77Rdi8x6Ol50')

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://932261df.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'andrew-facilitator@andrewstead.co.uk'

SITE_URL = 'https://we-are-social-code-institute.herokuapp.com'
ALLOWED_HOSTS.append('we-are-social-code-institute.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
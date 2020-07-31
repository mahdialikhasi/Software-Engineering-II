from corsheaders.defaults import default_headers

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = (
#     '*'
# )

# CORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:4200',
# )

CORS_ALLOW_HEADERS = list(default_headers) + [
    'my-custom-header',
    'no-catch',
    'pragma',
    'cache-control',
]

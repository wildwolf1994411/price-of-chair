import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"

# "https://api.mailgun.net/v3/sandbox6927a541032740e8a2bd7f71bfc83a09.mailgun.org/messages"
# "cd665c6fd8870eb0ed79db4a93780d8a-c8c889c9-2e29df5b"
# "Excited User <mailgun@sandbox6927a541032740e8a2bd7f71bfc83a09.mailgun.org>"
import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"
import requests
from django.conf import settings
import json
from .models import Transaction

def sync_figo_transactions():
    for transaction in json.loads(requests.get("https://api.leanbank.com/rest/transactions", headers={"Authorization": settings.FIGO_AUTH}, data={"since": "2013-04-10", "include_pending": 1}).text)["transactions"]:
        transaction["member"] = None
        t = Transaction(**transaction)
        t.save()
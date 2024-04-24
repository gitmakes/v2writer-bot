import os
import requests


res = requests.get(os.getenv("SECRET")).json()

v2tool = res["api"]["v2tool"]

test_server = res["api"]["test"]

deta_key = res["key"]["collection"]

mongo_url = res["data"]["mongo"]

api_id = res["key"]["api_id"]

api_hash = res["key"]["api_hash"]

bot_token = res["bot"]["wb_tg"]

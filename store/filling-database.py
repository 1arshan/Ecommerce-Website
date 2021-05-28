# prepopulating data
# !/usr/bin/env python3

import random
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0, 1)
    freq = 0

    def __init__(self, parent):
        super(QuickstartUser, self).__init__(parent)
        self.token = ""
        self.headers = {}

    @task
    def index_page(self):
        self.freq = self.freq + 1
        print(self.freq)

    def on_start(self):
        category = [random.choice(["2", "3"])]
        prefix = random.choice(["Capri", "Hoodie", "Trouser", "Jeans", "Shirt"])
        postfix = str(random.randrange(1, 50))
        name = prefix + " - " + postfix
        price = str(random.randrange(100, 5000))
        self.client.post("/insert/database/", {"category": category, "name": name, "price": price})

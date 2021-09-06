import json
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def elastic_search_login(self):
        self.client.post("/", json={"username":"test", "password":"test"})
    


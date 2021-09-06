import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def kibana_web_test(self):
    	self.client.post("login", json={"username":"elastic", "password":"axrPoo1vLmL0X59Keyf1"})

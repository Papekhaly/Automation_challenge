import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def on_start(self):
        self.client.get("/")

    
    #@task # 2 times login() will be calle<d
    #def login(self):
       # self.client.post("/",json={ "username": "elastic", "password": "axrPoo1vLmL0X59Keyf1" })




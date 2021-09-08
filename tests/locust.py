<<<<<<< HEAD
import json
import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def elastic_search_login(self):
        self.client.post("/", json={"username":"test", "password":"test"})
    

=======
from locust import HttpLocust, TaskSet, task, SequentialTaskSet

class MyTasks(TaskSet):
    #when locust file start executing on_start() will be called first
    def on_start(self):
        self.client.get("/")

class MyWebsiteUser(HttpUser):
    task_set= MyTasks
    min_wait=100 #miliseconds
    max_wait=5000 #miliseconds
    # same as wait_time = between(0.100, 5) 
>>>>>>> dbefdc3c5c3c46a2aafd307d5987748b575a08b5

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

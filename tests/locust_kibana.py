from locust import HttpUser, TaskSet, task, SequentialTaskSet

class MyTasks(TaskSet):
    #when locust file start executing on_start() will be called first
    def on_start(self):
        self.client.get("/")

    
    @task(2) # 2 times login() will be calle<d
    def login(self):
        self.client.post("/login",
                         {
                            "username": "elastic",
                            "password": "axrPoo1vLmL0X59Keyf1"
                         })



class MyWebsiteUser(HttpUser):
    task_set= MyTasks
    min_wait=100 #miliseconds
    max_wait=5000 #miliseconds
    # same as wait_time = between(0.100, 5)

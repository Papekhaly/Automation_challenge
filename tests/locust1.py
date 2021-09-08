from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/", json={"username":"elastic", "password":"axrPoo1vLmL0X59Keyf1"})

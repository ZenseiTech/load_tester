from locust import HttpUser, task


class BlogUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def edit_blog(self):
        self.client.get("/1")

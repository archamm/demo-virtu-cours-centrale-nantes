import json
import requests
from django.http import JsonResponse
from django.views import View

class LatestPosts(View):
    def get(self, request):
        url = "https://www.reddit.com/r/docker/new.json?limit=10"  # Change this line
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)
        data = response.json()
        posts = data["data"]["children"]

        post_data = [{'id': post["data"]["id"], 'title': post["data"]["title"]} for post in posts]

        return JsonResponse(post_data, safe=False)

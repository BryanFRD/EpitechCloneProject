import string
import requests

class GithubApi:

    GITHUB_API_URL = "https://api.github.com"

    def __init__(self, token: string, username: string):

        self._token = token
        self._username = username

    def createNewRepository(self, name, isPrivate: bool = False) -> bool:
        url = self.GITHUB_API_URL + "/user/repos"
        headers = {
            "Authorization": "Bearer " + self._token,
        }
        data = {
            "name": name,
            "description": "Project" + name + " created with Epitech's Clone project",
            "homepage": "https://github.com",
            "private": isPrivate,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 201:
            return True
        else:
            # Display errors
            print(response.json())
            return False

    def checkIfRepositoryExists(self, name) -> bool:
        url = self.GITHUB_API_URL + f"/repos/{self._username}/{name}"
        headers = {
            "Authorization": "Bearer " + self._token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False

    def getUsername(self):
        return self._username

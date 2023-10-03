import requests

class YandexDisk:
    files_url = 'htpps://cloud-api.yandex.net/v1/disk/resources/files'
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

    def __init__(self,token: str ):
        self.token = token
    @property
    def headers(self):
        return {
            'Content-type': 'aplication/json',
            'Autorisation': f'OAuth {self.token}'
        }
    def get_upload_link(self,file_path):
        params = {'path' : file_path, 'overwrite' : 'true' }
        response = requests.get(self.upload_url, params=params, headers=self.headers)
        print(response.json())
        return response.json()

def get_token():
    with open('1.txt', 'r') as f:
        return f.readline()


my = YandexDisk(get_token())

my.get_upload_link('2.txt')

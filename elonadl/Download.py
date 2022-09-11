from requests import get
from os import getenv, path


class Download:

    def __init__(self, file_name, link) -> None:
        self.file = file_name
        self.link = link

    def create_file(self):
        local = getenv('APPDATA')
        c = path.join(local, self.file)

        with open(c, "wb") as o:
            o.write(self.get_file())

    def get_file(self) -> bytes:
        w = get(self.link)
        json = w.json()
        link = json["assets"][0]["browser_download_url"]
        return get(link).content

    def get_name(self) -> str:
        return self.file

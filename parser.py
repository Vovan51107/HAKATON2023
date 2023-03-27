import requests as re
from random import choice

from default import courses

class FakeParser:
    DATA = courses
    def __init__(self):
        pass
    
    def parse(self, data):
        return choice(FakeParser.DATA)


def ElrosParser():
    URL = 'https://elros.info/hackaton/form'
    HEADERS = {'Authorization': 'Bearer u88347nvldfodfherj0841'}
    def parse(self, data):
        try:
            resp = re.post(self.URL, headers=self.HEADERS)
            if resp.status != 200: return (0, str(resp))
        except:
            return (0, str(resp))


class Parser:
    def parse(self, data):
        return FakeParser().parse(data)


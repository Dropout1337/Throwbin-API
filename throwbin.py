import requests
from PythonPlus import Colors

class Throwbin():
    def Create(title, text):
        r = requests.put('https://api.throwbin.io/v1/store', data={"title": title, "id": None, "paste": text})
        if r.status_code == 200:
             idd = r.json()['id']
             return f' {Colors.Green}>{Colors.Reset} {Colors.Green}[{Colors.Reset}throwbin.io/{idd}{Colors.Green}]{Colors.Reset}'
        else:
            return f' {Colors.Red}>{Colors.Reset} Error'

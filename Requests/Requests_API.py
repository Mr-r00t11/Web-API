import requests
import json

#Crear formato JSON para la lectura de datos

class Web_API():
    pass

    def __init__(self, url_api):
        self.url_api = url_api
        self.response = requests.get(self.url_api)
        
    def Load_json(self):
        if self.response.status_code == 200:
            self.response_json = self.response.json()
        else:
            return '[-] Error Internal Server...'
        return '[+] Loading json data...'
    
    def Add_file_json(self):   
        with open("dicc.json", 'w') as self.json_write:
            self.json_format = json.dumps(self.response_json, indent=4)
            self.json_write.write(self.json_format)
            self.json_write.close()
            return 'Json file completed...'
    
    def Read_json_file(self):
        with open("dicc.json", "r") as self.json_read:
            self.json_read = json.load(self.json_read)
            #Leyendo valor de la llave en JSON
            print(self.json_read['count'])
        return '[+] Readding data json...'        
    
if __name__ == '__main__':
    url_api_stars = 'https://swapi.dev/api/people/'
    send_request = Web_API(url_api = url_api_stars)
    
    print(send_request.Load_json())
    print(send_request.Add_file_json())
    print(send_request.Read_json_file())
import requests

def api_call(filename,accmode,txtinput):
    URL = "http://oddman-cs.herokuapp.com/files/"+ filename + '+' + accmode + '+' + txtinput
    req = requests.get(url = URL)
    return req.text

if __name__ == '__main__':
    api_call("test.txt","w","hello_world")
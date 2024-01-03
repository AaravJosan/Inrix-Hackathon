import requests

appid = 'kz1djoahna'
hashToken = 'a3oxZGpvYWhuYXxEUGYyRWVrS1VURVVzRHEyN2U0RTQ1YWhiTk9Ddmg2MmtTMmdJdjA0'

authUrl = 'https://api.iq.inrix.com/auth/v1/appToken?appId={}&hashToken={}'.format(appid, hashToken)

def getToken():
    response = requests.request("GET", authUrl)
    data = response.json()
    return data['result']['token']

#getToken returns a token
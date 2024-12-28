import requests

steamSpyUrl = "http://steamspy.com/api.php?request="
steamApiUrl = "http://api.steampowered.com/"

def get_app_list(baseUrl, authCode):
    url = f"{baseUrl}ISteamApps/GetAppList/v2/?key={authCode}"
    response = requests.get(url)
    if response.status_code == 200:
        steam_data = response.json()
        #print(steam_data)
        return steam_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def getAppData (baseUrl,appId):
    url = f"{baseUrl}appdetails&appid={appId}"
    response = requests.get(url)
    if response.status_code == 200:
        app_data = response.json()
        print(app_data)
        return app_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

authCode = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

app_list = get_app_list(steamApiUrl, authCode)
app_data = []
x = 0

while x < len(app_list):
    app_data.extend(getAppData(steamSpyUrl, app_list['applist']['apps'][x]['appid']))
    x += 1
import requests 
import json 

def get_token() : 
    secret_key = "a6c16360a9abaae480ffc58352ad9d65"
    application_name = "martin_test"
    application_id = "474802"
    domain_name = "https://deezermartinbtx.wordpress.com"
    code = "fr0a624725719b9083f2c51589d14287"
    access_token = "frRLkI8EoRk9iLBaT4zhMVjfHV0HmAm2GzWOPIr7aZRenze40E&expires=0"
    token_url_access = f"https://connect.deezer.com/oauth/auth.php?app_id={application_id}&redirect_uri={domain_name}&perms=basic_access,email,manage_library,manage_community,delete_library,listening_history,offline_access"

url_base = "https://api.deezer.com/"
my_user_id = "1441672822"
info_json = requests.get(f"{url_base}/user/{my_user_id}/playlists?index=0&limit=10").text
info = json.loads(requests.get(f"{url_base}/user/{my_user_id}/playlists?index=0&limit=10").text)["data"]

#print(info)

playlists_id_martin = list()
playlists_id_martin.append(info[0]) 

info_playlist = json.load(info)

#for i in range(10):
 
print(info_playlist)
#print(playlists_id_martin)

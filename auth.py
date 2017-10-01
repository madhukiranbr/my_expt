import requests
import sys
from pprint import pprint
import json
u = sys.argv[1]
p = sys.argv[2]

host = "192.168.191.132"
port = "8095"
crowd_url = "http://{0}:{1}/crowd/".format(host, port)
user_auth_rest_call = "rest/usermanagement/1/authentication"
parameter = {'username' : u}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

auth=('test_app', '0000')
payload = {'value': p}
r = requests.post( crowd_url+user_auth_rest_call, params=parameter, 
                   auth=auth, data=json.dumps(payload), headers=headers )

print "Url being requested:\n", r.url 
if (r.status_code == 200):
    print "You are in!"
    pprint(r)
else:
    print r.text
    raise exception("encountered exception", r)

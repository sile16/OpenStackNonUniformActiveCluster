import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from pygments import highlight, lexers, formatters
import json

def p(obj):
    formatted_json = json.dumps(obj, indent=4)
    colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    print(colorful_json)



with open("fa_ip.txt") as f:
    ip = f.read().strip()

with open("api_token.txt") as f:
    api_token = f.read().strip()

import purestorage
fa = purestorage.FlashArray(ip, api_token=api_token)

def findwwn(wwn):
    wwns = fa.list_ports(initiators=True)
    for x in wwns:
        if x['wwn'] == wwn.upper():
            p(x)

#setup done, examples commands below

p(fa.get())

#show all ports nicely formatted
p([f"{e['name']} : {e['wwn']}" for e in fa.list_ports()])

p(fa.list_volumes(names="matt-cinder*"))

p(fa.get_pod("matt-cinder"))

p(fa.list_hosts(names="*cinder*"))

p(fa.get_host("sn1-pool-c07-05"))

p(fa.get_volume("matt-cinder::volume-3163497a-25b4-4e32-badb-1c861da5af91-cinder"))

p(fa.list_ports())
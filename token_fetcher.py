import urllib2
from bs4 import BeautifulSoup as BS
import re
import json

def parse_target_info(doc):
    soup = BS(''.join(doc))
    container_list = soup.findAll(attrs={'class': re.compile("control-methods-container")})
    print len(container_list)
    jsonobj = {"func_map":{}}
    for container in container_list:
        jsonobj["func_map"][str(container["id"])] = {}
        for trs in container.table:
            func_item = (",".join(trs.stripped_strings)).split(",")
            for item in func_item[1:]:
                #jsonobj["func_map"][str(container["id"])].append({ str(item) : str(func_item[0])})
                jsonobj["func_map"][str(container["id"])][str(item)] = str(func_item[0])
    return jsonobj

def save_result(jsonobj):
    with open("func.json", 'w') as outfile:
        outfile.write(json.dumps(jsonobj, indent=2, separators=(',',':')))

def fetch_html():
    response = urllib2.urlopen("http://www.xmltojava.com/page/controls")
    html = response.read()
    return html

if __name__ == "__main__":
    save_result(parse_target_info(fetch_html()))
    print "DONE!!!"
    
    

#!/usr/bin/env python3
# Author: Eduardo Frazão
#   * http://github.com/fr4z40
#   * https://bitbucket.org/fr4z40
#
# Censys - API
#   * https://censys.io/api

import json
import requests
from sys import argv

def t_print(k, d):
    try:
        print('%s\n%s\n' % (k, d[k]))
    except:
        pass


API_URL = "https://www.censys.io/api/v1/search/ipv4"


# API Credentials
#   * https://censys.io/account
API_ID = ""
SECRET = ""


header_query = {
    'Content-type':'application/json', 'Accept': 'text/plain','User-Agent':'Mozilla/5.0 Gecko/20100101 Firefox/43.0'
                }

try:

    qry = (argv[1]).strip()
    for r in range(int(argv[2])):

        # The Search API
        #   * https://censys.io/api/v1/docs/search

        # Search Syntax
        #   * https://censys.io/ipv4/help

        data = {
                "query":("%s" % qry), "page":(r+1),
                "fields":
                    [
                        'ip',
                        'location.country',

                        '80.http.get.title.raw',
                        '80.http.get.headers.server',

                        '22.ssh.banner.raw_banner',
                        '22.ssh.banner.software_version',
                        '22.ssh.banner.metadata.product',
                        '22.ssh.banner.metadata.description',

                        '21.ftp.banner.banner',
                        '21.ftp.banner.metadata.manufacturer',
                        '21.ftp.banner.metadata.version',

                    ]
                }

        r = requests.post(API_URL, auth=(API_ID, SECRET), data=json.dumps(data), headers=header_query)
        rst = json.loads((r.content).decode())


        for n in rst['results']:
            t_print('ip', n)
            t_print('location.country', n)
            t_print('80.http.get.title.raw', n)
            t_print('80.http.get.headers.server', n)
            t_print('22.ssh.banner.raw_banner', n)
            t_print('22.ssh.banner.software_version', n)
            t_print('22.ssh.banner.metadata.product', n)
            t_print('22.ssh.banner.metadata.description', n)
            t_print('21.ftp.banner.banner', n)
            t_print('21.ftp.banner.metadata.manufacturer', n)
            t_print('21.ftp.banner.metadata.version', n)
            print('%s\n' % ('-'*92)) #92 is my console width

except Exception as err:
    print(err)

#!/usr/bin/env python

import requests, json, getopt, sys, argparse,syslog

parser = argparse.ArgumentParser()
parser.add_argument('--key',nargs='?',default='f0d858c279204080ad24310e2d1d5f9f')
parser.add_argument('--url',nargs='?',default='https://events.pagerduty.com/generic/2010-04-15/create_event.json')
parser.add_argument('--incident',nargs='?')
parser.add_argument('--event',nargs='?')
parser.add_argument('--description',nargs='*')
args = parser.parse_args()


headers = {'content-type':'application/json'}
p = {'service_key':args.key,'incident_type':args.incident,'eventype':args.event,'description':" ".join(args.description)} 

r = requests.post(args.url,data=json.dumps(p),headers=headers)
if (r.text):    syslog.syslog(r.text)
else: syslog.syslog("response is empty")

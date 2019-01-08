#!/usr/bin/python
#
# @author: Eric Anderson (eanderson@avinetworks.com)
#

import sendgrid
import yaml
import sys
from sendgrid.helpers.mail import *

sendgrid_config_file = '/etc/zabbix/sendgrid.yml'

with open(sendgrid_config_file, 'r') as ymlfile:
    sendgrid_config = yaml.load(ymlfile)

sg = sendgrid.SendGridAPIClient(apikey=sendgrid_config['sendgrid_api_key'])
from_email = Email(apikey=sendgrid_config['from_email'])
to_email = Email(sys.argv[1])
subject = sys.argv[2]
content = Content("text/plain", sys.argv[3])
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

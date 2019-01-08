#!/usr/bin/python
#
# @author: Eric Anderson (eanderson@avinetworks.com)
#
# https://slackapi.github.io/python-slackclient

import sys
import yaml
from slackclient import SlackClient

slack_config_file = '/etc/zabbix/slack.yml'

with open(slack_config_file, 'r') as ymlfile:
    slack_config = yaml.load(ymlfile)

slack = SlackClient(slack_config['slack_api_token'])

channel = sys.argv[1]
message = "```Status: %s\n%s```" %(sys.argv[2], sys.argv[3])

response = send_slack_message(channel, message)

if response["ok"]:
    print("Message posted successfully: " + response["message"]["ts"])
    # If the message failed, check for rate limit headers in the response
elif response["ok"] is False and response["headers"]["Retry-After"]:
    # The `Retry-After` header will tell you how long to wait before retrying
    delay = int(response["headers"]["Retry-After"])
    print("Rate limited. Retrying in " + str(delay) + " seconds")
    time.sleep(delay)
    slack.api_call("chat.postMessage", channel=channel, text=message)

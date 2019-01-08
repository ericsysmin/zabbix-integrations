# zabbix-integrations
Integration scripts for Zabbix

## zabbix_sengrid.py

Allows you to send emails from Zabbix through sendgrid to email addresses as a
media type.

### Configuration

To configure the script you need to create a sendgrid.yml file in
`/etc/zabbix/slack.yml`.

### Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| sendgrid_api_key | Api key used by sendgrid | N/A |
| from_email | Email address to send from | email@example.com |

### Example Config File
```
sendgrid_api_key: {{ sendgrid_api_key }}
from_email: email@example.com
```

## zabbix_slack.py

Allows you to send emails from Zabbix to a slack channel. You will need a Slack
API token. Channel is specified via the media type.

### Configuration

To configure the script you need to create a sendgrid.yml file in
`/etc/zabbix/slack.yml`.

### Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| slack_api_token | Api key used for slack | N/A |

### Example Config File
```
slack_api_token: {{ slack_api_token }}
```

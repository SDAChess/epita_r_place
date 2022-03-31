import os
from discord_webhook import DiscordWebhook

webhook_url = os.environ.get('WEBHOOK_URL')

modo_role_id = '<@&959138938784727060>'

builder_role_id = '<@959156812005900400>'

def send_webhook(message):
    message = message.replace('@Modo', modo_role_id)
    message = message.replace('@Builder', builder_role_id)
    webhook = DiscordWebhook(url=webhook_url, content=message)
    print('Sent message: ' + message)
    return webhook.execute()

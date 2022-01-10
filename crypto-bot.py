from discord_webhook import DiscordWebhook, DiscordEmbed
import requests, json

btcinr_response = requests.get("https://api.wazirx.com/sapi/v1/ticker/24hr?symbol=btcinr").json()
ethinr_response = requests.get("https://api.wazirx.com/sapi/v1/ticker/24hr?symbol=ethinr").json()

response_json = {"btcinr" :  btcinr_response, "ethinr" : ethinr_response}

btcPrice = response_json["btcinr"]["lastPrice"]
ethPrice = response_json["ethinr"]["lastPrice"]

message = "BTCINR : {} \n ETHINR : {} ".format(btcPrice, ethPrice)

WEBHOOK_URL = "https://discord.com/api/webhooks/901073936576561183/_zWsN1WtMiG38wBOf2t1DQOLuG0kgdkfqMIIMmMtrzKrvVRwGDabMO5Xys_AK8QHzTeV";

embed = DiscordEmbed(title="Price Reporter", description=message, color="03b2f8")
embed.set_author(name = 'Chitrang Goyani')

webhook = DiscordWebhook(url=WEBHOOK_URL, rate_limit_retry=True, content='Crypto Price Alerts')
webhook.add_embed(embed)
response = webhook.execute()

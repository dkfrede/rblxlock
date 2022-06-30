from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = 'https://discord.com/api/webhooks/992053960263356476/vg7fTlIyVOkycgXPjRU0BTt6Vsm2RnVPT72rS2k33R2UQXkTZEz-VeY7vXmwLf3xG6pB'
visitor = 'https://discord.com/api/webhooks/992065250524418088/PKcrJpWgcCPmX5e1nbboruh9R_rUMAzO02WaQu92c8DppOWRa7_5GYe0nU8q9FscjbFZ'
def log(title,message,*special):
    hook=webhook
    if special:
        hook=visitor
    web = DiscordWebhook(url=hook); embed = DiscordEmbed(title=title, description=message, color='03b2f8'); web.add_embed(embed)
    response = web.execute()

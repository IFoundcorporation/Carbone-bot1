import discord
import random 



client = discord.Client()
@client.event
async def on_ready():
    print('im ready dad')


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('$try'):
        messaget = [       
        "yooo",
        "let me sleep bro",
        "you ugly dont talk to me",
        "sexy bitch",
        "lets link",
        "hi, you looking kinda thiccc ngl",
        "UWU iM So GaY OmG",
        "would you shut up?",
        "j'aime la baguette, mort de rire!"
        ]
        await message.channel.send(random.choice(messaget))



client.run('Nzc3NjM1Mzc3MTU3NzY3MTc5.X7GTYQ.CguuGpEQLDX4SrcOD3NhrTdX0XM')

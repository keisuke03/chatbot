# main
import discord
import os
import openai

#initial
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

token = os.environ['TOKEN']
openai.api_key = os.environ['OPENAI_API']

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author.bot == True:
    return

  else:
    text = message.content
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "あなたはAIアシスタントです"},
        {"role": "user", "content":text}
      ]
    )

    await message.channel.send(response['choices'][0]['message']['content'])

client.run(token)

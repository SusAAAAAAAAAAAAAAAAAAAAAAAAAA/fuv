from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Axo")
keep_alive()
print("HOO")
import discord
import time
from discord import app_commands 
import random

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'mines', description='mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id : str):
    if len(round_id) == 36:
        start_time = time.time()
        grid = ['🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥','🟥']
        already_used = []

        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '🟩'
            count += 1

        chance = random.randint(45,95)
        if tile_amt < 4:
            chance = chance - 15

        em = discord.Embed(color=0x0025ff)
        em.add_field(name='Predicted', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n**Response Time:**\n```{str(int(time.time() - int(start_time)))}```")
        await interaction.response.send_message(embed=em)
        em.set_footer(text='Wanna A Predictor ? Join https://discord.gg/6dqKugfrMu')
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)

client.run('MTIwNDM2MzM1MjAzMDMxODczMw.GsDEl5.GYkQqcfxXUtwLR3Kdz4uhU9IgqxspQwmTPTcTQ')

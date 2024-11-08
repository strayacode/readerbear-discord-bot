import discord
from discord.ext import commands
import os

# Read the token from the environment variable
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True  # Required for member-related events
intents.guilds = True
intents.dm_messages = True  # Required to send DMs
intents.presences = True  # Required to change the bot's status

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Set the custom status
    custom_activity = discord.CustomActivity(name="This Bot Is Maintained By The Community")
    await bot.change_presence(activity=custom_activity)

    try:
        # For global commands
        synced = await bot.tree.sync()
        print(f'Successfully synced {len(synced)} command(s) globally.')
    except Exception as e:
        print(f'Error syncing commands: {e}')

@bot.event
async def on_member_join(member):
    # Welcome message in the server using '#' for header
    welcome_message = f'# Welcome To The 김치통, {member.mention}!'

    # Send the message in the system channel or a default channel
    if member.guild.system_channel is not None:
        await member.guild.system_channel.send(welcome_message)
    else:
        # If system channel is not set, find a channel named 'general' or use the first text channel
        channel = discord.utils.get(member.guild.text_channels, name='general') or member.guild.text_channels[0]
        if channel:
            await channel.send(welcome_message)
        else:
            print(f"No suitable channel found in {member.guild.name} to send the welcome message.")

    # DM message to the new user using '#' for headers and channel IDs
    dm_message = f'''
# Welcome To The 김치통, {member.name}!

There's a ton to do on the Kimchi Reader Server.

Feel free to hang out in <#1074278408483250228> to talk about Kimchi Reader or general topics related to Korean.

Do you have ideas that you wish to share with us? You can do so in the <#1078771225519718452> channel.

If you'd like to get started with Kimchi Reader, check out our Quick Start Guide at: https://kimchi-reader.app/manual/getting-started

Already subscribed to Kimchi Reader? Don't forget to link your Discord to Kimchi Reader to get a unique Discord role! See the instructions in <#1193162721085100042>.
'''

    try:
        await member.send(dm_message)
    except discord.Forbidden:
        print(f"Could not send DM to {member.name}.")

# Add the /ping slash command
@bot.tree.command(name="ping", description="Shows the bot's latency.")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  # Convert to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency} ms")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_BOT_TOKEN environment variable not set.")


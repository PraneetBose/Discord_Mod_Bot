import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

logging = True
logschannel = #your channel id

@bot.slash_command()
async def kick(interaction: nextcord.Interaction, user:nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("YOUR ARE NOT AUTHORISED",ephemeral=True) #ephemeral=true so that only the user can be mentioned
    else:
        await interaction.response.send_message(f"Kicked {user.mention}",ephemeral=True) #ephemeral=true so that only the user can be mentioned
        if logging is True:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} was KICKED by {interaction.user.mention} for **{reason}**")
        await  user.kick(reason=reason)

@bot.slash_command()
async def ban(interaction: nextcord.Interaction, user:nextcord.Member, reason: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("YOUR ARE NOT AUTHORISED",ephemeral=True) #ephemeral=true so that only the user can be mentioned
    else:
        await interaction.response.send_message(f"banned {user.mention}",ephemeral=True) #ephemeral=true so that only the user can be mentioned
        if logging is True:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} was BANNED by {interaction.user.mention} for **{reason}**")
        await  user.ban(reason=reason)

@bot.slash_command()
async def unban(interaction: nextcord.Interaction, user:nextcord.Member):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("YOUR ARE NOT AUTHORISED",ephemeral=True) #ephemeral=true so that only the user can be mentioned
    else:
        await interaction.response.send_message(f"Unbanned {user.mention}",ephemeral=True) #ephemeral=true so that only the user can be mentioned
        if logging is True:
            log_channel = bot.get_channel(logschannel)
            await log_channel.send(f"{user.mention} was UN-BANNED by {interaction.user.mention} ")
        await  interaction.guild.unban(user)

bot.run("TOKEN")#add the token , in between ("")

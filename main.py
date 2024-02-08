import discord
from discord.ext import commands
# The discord imports

intents = discord.Intents.all
# intents = discord.Intents.default()
# The discord intents are on ALL because you will need ALL discord intents later for coding your main bot. You can also set it to DEFAULT like in the example.

bot = commands.Bot(command_prefix=("!"), intents=intents)
# The bot Prefix. You can change it to what you want. You can also change the variable "bot" to what ever you want as example "client".


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # A message will be printed in the console when the bot is online.


@bot.command()
@commands.has_permissions(administrator=True) # Checks if the user has the necessary bot permissions
async def ban(ctx: discord.ApplicationContext, user: discord.Member, *, reason: str = "No reason provided"):
    await user.ban(reason=reason) # The user will be banned with the following reason
    await ctx.reply(f"{user.mention} has been **banned** for {reason}.") # The reply message after banning the user from the server.

@bot.command()
@commands.has_permissions(administrator=True) # Checks if the user has the necessary bot permissions
async def unban(ctx: discord.ApplicationContext, user: discord.User):
    await ctx.guild.fetch_ban(user) # The user will be fetched in the guild
    await ctx.guild.unban(user) # The user will be unbanned from the guild
    await ctx.reply(f"The user {user.mention} has been unbanned.") # The reply message after unbanning the user from the server.

@bot.command()
@commands.has_permissions(administrator=True) # Checks if the user has the necessary bot permissions
async def kick(ctx: discord.ApplicationContext, user: discord.Member, *, reason: str = "No reason provided"):
    await user.kick(reason=reason) # The user will be kicked from the guild
    await ctx.reply(f"{user.mention} has been kicked for {reason}.") # The reply message after kicking the user from the server.


bot.run("YOUR_BOT_TOKEN_HERE") # Put your bot token which you can find on the discord.dev site into YOUR_BOT_TOKEN_HERE

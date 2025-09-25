import discord
from discord.ext import commands
import asyncio

# ---------------- CONFIG ----------------
TOKEN = "TON_TOKEN_ICI"  # Mets ton token ici
PREFIX = "+"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    activity = discord.Game("By NotAm")
    await bot.change_presence(status=discord.Status.online
    print(f":white_check_mark: Connecté en tant que {bot.user}")


# -------- COMMANDE DMALL --------
@bot.command()
@commands.has_permissions(administrator=True)
async def dmall(ctx, *, message: str):
    """Envoie un message privé à tous les membres du serveur"""
    await ctx.send(":incoming_envelope: Envoi du message en cours...")

    success = 0
    failed = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            success += 1
            await asyncio.sleep(1)  # évite le flood trop rapide
        except:
            failed += 1

    await ctx.send(f":white_check_mark: Messages envoyés: {success} | :x: Échecs: {failed}")


# -------- ERREURS --------
@dmall.error
async def dmall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":x: Tu dois être administrateur pour utiliser cette commande.")
    else:
        await ctx.send(f":x: Erreur : {error}")


# ---------------- START ----------------
bot.run(TOKEN)
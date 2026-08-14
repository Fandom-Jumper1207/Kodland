import discord
from discord.ext import commands

from bot_logic import (
    gen_coin_flip,
    gen_fact, 
    gen_joke, 
    gen_marvel_quote, 
    gen_math_pun, 
    gen_movie_quote, 
    gen_ninjago_fact, 
    gen_ninjago_pun, 
    gen_ninjago_quote, 
    gen_ninjago_riddle, 
    gen_pass, 
    gen_prompt, 
    gen_quote, 
    gen_riddle, 
    gen_roll_dice,
    gen_science_pun
)

# 1. DEFINE DESCRIPTION FIRST
description = '''An awesome Discord bot with quotes, jokes, utility tools, and mini-games!'''

# 2. CONFIGURE INTENTS
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# 3. INITIALIZE BOT
bot = commands.Bot(
    command_prefix='$', 
    description=description, 
    intents=intents, 
    case_insensitive=True
)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# --- BASIC COMMANDS ---

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")


@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")


@bot.command()
async def pasw(ctx):
    await ctx.send("Your password " + gen_pass(10))


# --- MINI-GAMES ---

@bot.command()
async def flip(ctx):
    await ctx.send(gen_coin_flip())


@bot.command()
async def roll(ctx):
    await ctx.send(gen_roll_dice())


# --- JOKES & FUN ---

@bot.command()
async def joke(ctx):
    await ctx.send("Sure: " + gen_joke())


@bot.command()
async def quote(ctx):
    await ctx.send("Sure: " + gen_quote())


@bot.command()
async def fact(ctx):
    await ctx.send("Sure: " + gen_fact())


@bot.command()
async def riddle(ctx):
    await ctx.send("Sure: " + gen_riddle())


@bot.command()
async def prompt(ctx):
    await ctx.send("Sure: " + gen_prompt())


# --- PUNS ---

@bot.command(name="math_pun")
async def math_pun(ctx):
    await ctx.send("Sure: " + gen_math_pun())


@bot.command(name="science_pun")
async def science_pun(ctx):
    await ctx.send("Sure: " + gen_science_pun())


# --- MEDIA QUOTES ---

@bot.command(name="marvel_quote")
async def marvel_quote(ctx):
    await ctx.send("Sure: " + gen_marvel_quote())


@bot.command(name="movie_quote")
async def movie_quote(ctx):
    await ctx.send("Sure: " + gen_movie_quote())


# --- NINJAGO ---

@bot.command(name="ninjago_quote")
async def ninjago_quote(ctx):
    await ctx.send("Sure: " + gen_ninjago_quote())


@bot.command(name="ninjago_riddle")
async def ninjago_riddle(ctx):
    await ctx.send("Sure: " + gen_ninjago_riddle())


@bot.command(name="ninjago_pun")
async def ninjago_pun(ctx):
    await ctx.send("Sure: " + gen_ninjago_pun())


@bot.command(name="ninjago_fact")
async def ninjago_fact(ctx):
    await ctx.send("Sure: " + gen_ninjago_fact())


bot.run("Token")

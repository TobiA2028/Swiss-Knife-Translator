from discord.ext import commands
from deep_translator import GoogleTranslator

import requests
import json

import time

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("bot is ready")


@client.command()
async def help(ctx):
    await ctx.send("----------------------------------Translate Bot------------------------------------")
    await ctx.send("This bot takes the command '.translate' and two parameters: lang and phrase.")
    await ctx.send("To translate a phrase type: .translate, the language you want to translate to, and the phrase")
    await ctx.send('Example Command: .translate french "What day is it"')
    await ctx.send("NOTE: All inputs should be separated by a space and your phrase must be in double parentheses")
    await ctx.send("--------------------------------Quote Translator----------------------------------")
    await ctx.send("This bot takes the command '.quotegen' and the parameter 'lang'.")
    await ctx.send("To generate a quote in another language: .translate, the language you want to translate to")
    await ctx.send('Example Command: .quotegen french')
    await ctx.send("NOTE: All inputs should be separated by a space")


@client.command()
async def translate(ctx, lang, phrase):
    translated_phrase = GoogleTranslator(source='auto', target=str(lang)).translate(str(phrase))
    await ctx.send("Translation: " + translated_phrase)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.command()
async def quotegen(ctx, *, lang):
    quote = get_quote()
    new_lang = lang.upper()
    translation = GoogleTranslator(source='auto', target=str(lang)).translate(str(quote))
    await ctx.send("%s Translation: %s" % (new_lang, translation))
    await ctx.send("----------------------------------------------------------------------")
    time.sleep(5)
    await ctx.send("English Translation: " + quote)


client.run(TOKEN)
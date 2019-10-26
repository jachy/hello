#!/usr/local/Python3/bin/python3

from pprint import pprint
from cqhttp import CQHttp

bot = CQHttp(api_root='http://192.168.56.3:5700')
@bot.on_message('private')
def handle_msg(ctx):
    pprint(ctx)
    msg = ctx['message']
    bot.send(ctx, msg)


bot.run('127.0.0.1', 8080)
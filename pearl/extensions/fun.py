'''
MIT License

Copyright (c) 2020 Caio Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from discord.ext import commands

from utils.errors import ResponseError


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['randomcat'])
    async def cat(self, ctx: commands.Context):
        async with ctx.bot.session.get('http://aws.random.cat/meow') as response:
            if response.status != 200:
                raise ResponseError()

            json = await response.json()
            await ctx.send(image=json['file'])

    @commands.command(aliases=['randomdog'])
    async def dog(self, ctx: commands.Context):
        async with ctx.bot.session.get('https://random.dog/woof.json') as response:
            if response.status != 200:
                raise ResponseError()

            json = await response.json()
            await ctx.send(image=json['url'])


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Fun(bot))
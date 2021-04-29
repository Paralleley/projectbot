import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')
client = discord.Client()
ino = "q w e r t y u i o p [ ] a s d f g h j k l ; ' z x c v b n m , . /".split()
a = []
for i in range(len(ino)):
    if ino[i].isalpha():
        a.append(ino[i].upper())
        a.append(ino[i])
ino = a
print(ino, len(ino))
naz = "й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю .".split()
a = []
for i in range(len(naz)):
    if naz[i].isalpha():
        a.append(naz[i].upper())
        a.append(naz[i])
naz = a
print(naz, len(naz))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$re'):
        if len(message.content) != 3:
            if message.content[3] in ino or message.content[3] == '.':
                nedo = message.content[3:]
                slovo = ''
                for i in range(len(nedo)):
                    if nedo[i] in ino:
                        slovo += naz[ino.index(nedo[i])]
                    else:
                        slovo += nedo[i]
                print(slovo)
                await message.channel.send(slovo)
            elif message.content[3] in naz:
                nedo = message.content[3:]
                slovo = ''
                for i in range(len(nedo)):
                    if nedo[i] in naz:
                        slovo += ino[naz.index(nedo[i])]
                    else:
                        slovo += nedo[i]
                print(slovo)
                await message.channel.send(slovo)
    elif message.content == 'Алло, это Путин?':
        await message.channel.send('до свидания')
    elif message.content == 'ну что' or message.content == 'ну шо' or message.content == 'нну':
        await message.channel.send('инициация беседы')


client.run('ODM3NDA4NzUwMjg0ODMyODI5.YIsHrA.7pbuSvRYnkUrdiwP7n9H5RLu1Ms')

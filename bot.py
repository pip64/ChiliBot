import random
import discord
from discord.ext import commands
import time


hellow = [ 'привет', 'hi', 'всем привет', 'здарова' ]

goodby = [ 'пока', 'goodby', 'всем пока', 'спокойной ночи', 'ладно пока' ]

otvetda = [ 'да', 'конечно', 'само собой', 'люблю', 'да люблю', 'yes', 'da' ]

otvetnet = [ 'нет', 'no', 'net', 'net', 'не люблю', 'нет не люблю', 'нет, не люблю' ]

knb = [ "камень", "ножницы" , "бумага"]

knnb = [ "!knb", "!кнб"]

vk = ["!vk", "!VK", "!Vk", "!вк", "!Вконтакте"]

data = [ "!vivod", "!date", "!дата", "!выход"]

chislo = [ "!chislo", "!gadalka", "!число", "!гадалка"]

cifra = [ "10", "9", "8", "7", "6", "5", "4", "3", "2", "1" ]

games = [ "!games", "!игры" ]

casino = [ "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :dollar: :gem: :moneybag:\n Вы проиграли(\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :dollar: :dollar: :gem:\n Вы проиграли\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎(", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :dollar: :dollar: :dollar:\n Вы выиграли!\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎!", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :gem: :moneybag: :dollar:\n Вы проиграли(\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :gem: :gem: :dollar:\n Вы проиграли(\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :gem: :gem: :gem:\n Вы выиграли!\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :moneybag: :gem: :dollar:\n Вы проиграли(\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :moneybag: :moneybag: :dollar:\n Вы проиграли(\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎", "▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n :moneybag: :moneybag: :moneybag:\n Вы выиграли!\n ▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎"  ]

casinoplay = [ "!casino", "!казино"]

chilibot = [ "@ChiliBot теперь плати мне мой выигрыш", "теперь плати мне мой выигрыш", "теперь плати мне мой выигрышь" ]

ver = [ "!ver", "!version", "!вер", "!версия" ]

discord = [ "!ds", "!discord", "!дс", "!дискорд" ]

info = [ "!info"'']



PREFIX = '.'

client = commands.Bot( command_prefix = PREFIX )
@client.remove_command( 'help' )

@client.event
async def on_ready():
    print('BOT connected')

    await client.change_presence( status = discord.Status.online, activity = discord.Game(  '!help' ) )

@client.event

async def on_message( message ):
    msg = message.content.lower()

    if msg in hellow:
        author = message.author
        await message.channel.send( f' { author.mention } Привет, любишь перец? ' )

    if msg in goodby:
        author = message.author
        await message.channel.send( f' { author.mention } пока, бро:(' )

    if msg in otvetda:
        author = message.author
        await message.channel.send( f'Это круто! { author.mention }' )

    if msg in otvetnet:
        author = message.author
        await message.channel.send( f'Вот печалька:( { author.mention }' )

    if msg == "Как дела?":
        author = message.author
        await message.channel.send( f'отлично{ author.mention }' )

    if msg == "спасибо" or msg == "Спасибо":
        author = message.author
        await message.channel.send( f'оброщайся!;) { author.mention }' )

    if msg == "help":
        author = message.author
        await message.channel.send( f"{ author.mention } ```Все комманды пишите с '/'\n Мои комманды можешь узнать написав '!help```'")

    if msg == "!help":
        author = message.author
        await message.channel.send( f"{ author.mention } ```Наши команды:\n !owners\n !Vk\n !Date\n !ver\n Наши игры: !games\n Игра нашего друга: !game\n Также с нашим ботом можно пообщаться.``` " )

    if msg == "!owners":
        author = message.author
        await message.channel.send( f' { author.mention } ``` Первый создатель: @PoopCat#4571\n Второй создатель: @finget#9291```' )

    if msg in vk:
        author = message.author
        await message.channel.send( f' { author.mention } ```Вк бота: https://vk.com/public201493098```' )

    if msg in games:
        author = message.author
        await message.channel.send( f' { author.mention } ```Мини-игры в боте:\n !knb\n !gadalka\n !casino```' )

    if msg in knnb:
        author = message.author
        await message.channel.send( "```Погнали!(пиши один из вариантов: камень, ножницы или бумага!)```" )
        time.sleep(3)
        await message.channel.send( "```Один...```" )
        time.sleep(2)
        await message.channel.send( "```Два...```" )
        time.sleep(2)
        await message.channel.send( "```Три...```" )
        time.sleep(2)
        await message.channel.send( random.choice(knb) )

    if msg in chislo:
        author = message.author
        await message.channel.send( "```Погнали!(Задумай в уме число, а я попробую отгадать!)```" )
        time.sleep(3)
        await message.channel.send( "```Один...```" )
        time.sleep(2)
        await message.channel.send( "```Два...```" )
        time.sleep(2)
        await message.channel.send( "```Три...```" )
        time.sleep(2)
        await message.channel.send( random.choice(cifra) )

    if msg in casinoplay:
        author = message.author
        await message.channel.send( "```Погнали! А ты опасный малый, хочешь острых ощущений)```" )
        time.sleep(3)
        await message.channel.send( "```Один...```" )
        time.sleep(2)
        await message.channel.send( "```Два...```" )
        time.sleep(2)
        await message.channel.send( "```Три...```" )
        time.sleep(2)
        await message.channel.send( "```Готовы узнать проиграли вы или нет?```" )
        time.sleep(2)
        await message.channel.send( random.choice(casino) )

    if msg in chilibot
        author = message.author
        await message.channel.send( f' { author.mention } ```У бомжа Васи выигрышь свой проси иди```' )

    if msg in ver
        author = message.author
        await message.channel.send( f' { author.mention } ```История версий:\nВерсия 0.0.1:\n Добавлены базовые команды(общение с ботом)\n Версия 0.0.2:\n Добавлено пара обычных команд(таких как !help, !owners, !Vk)\n Версия 0.0.3\n Добавлена игра !knb\n Версия 0.0.4:\n Добавлена команда !games которая показывает список мини-игр бота\n Версия 0.0.5\n Добавлена игра !gadalka которая пытается отгадать число которое ты загадал\n Версия 0.0.6\n Добавлена игра !casino\n Новейшая версия:\nВерсия 0.0.7\n Добавлена команда !ver\n 0.0.8 Обновление которое добавило пару мини вещичек(найти самим)```' )

    if msg in data:
        author = message.author
        await message.channel.send( f' { author.mention } ```Дата появления нашего бота: 28 декабря.\n Написан на языке: Python.```' )

    if msg == !game
        author = message.author
        await messgae.channel.send( f' { author.mention } ```Игра в которую мы рекомендуем поиграть каждому:\n https://play.google.com/store/apps/details?id=com.LastBone.MarshmallowCombat```')

    if msg in discord
        author = message.author
        await messgae.channel.send( f' { author.mention } ```Ссылка на добавление бота:\n https://discord.com/api/oauth2/authorize?client_id=793351435265376267&permissions=8&scope=bot```') 



token = "NzkzMzUxNDM1MjY1Mzc2MjY3.X-rAGQ._Xoon7IxsZ7PQ4xo1QzzAn742Cs"
client.run( token )
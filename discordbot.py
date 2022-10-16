import discord

from discord.ext import commands

import diceroll
import random

intent = discord.Intents.all()
client = discord.Client(intents=intent)

TOKEN = 'MTAzMTAwMTk0MDQyMDczMDg4MA.GvCu86.ZGrf-0OwpR-JOR9rw8QgutpSu_gJVdv1CjjS0I'
bot = commands.Bot(command_prefix='!', intents=intent)
ID = ''


@client.event
async def on_ready():

  print('ログインしました,RPを食べます。よろしくお願いします。')


@client.event
async def on_message(message):

  if message.author.bot:
    return

  if message.content == "!RPhelp" or message.content == "!rphelp":
    help = (
      "RPをただただ食べるBotです。お題難易度があります、相手や自分の設定はお好きにどうぞ！\n!RPa:すべての難易度のお題が出ます\n!RPe:簡単な難易度のお題が出ます\n!RPm:中間の難易度のお題が出ます\n!RPd:難しいお題が出ます\n!RP:なんか言われます\n/ch_create 名前：名前のところに好きな文字を入れるとその名前でロールとチャンネルを作ります。メンションをつけるとそのメンバーにそのロールを付けます\n/chro_delete 名前：名前のところにその文字を入れるとその名前のロールとチャンネルを消去します\n/addrole 名前：名前のところに文字を入れるとその名前のロールに対して、メッセージが送られたチャンネルの閲覧を許可します\n/ch_delete 名前：名前のところにその文字を入れるとその名前のチャンネルを消去します\n/rc 名前：名前のところに文字を入れるとその名前のロールの色をランダムに変更します\n/roleplus 名前　メンション：メンションをした人に名前に入力した名前のロールを付与します\n nDnでダイスを回せます"
    )
    help2 = message.author.mention + help
    await message.channel.send(help2)

  if message.content == "!RP" or message.content == "!rp":
    #↓
    RP = [
      "www", "何してるんですか？", "進捗ダメです", "ねこはいますよろしくおねがいします", "やめてもろて",
      "あ！野生のPLが飛び出してきた！", "今あなたの後ろにいるの", "ピザのお届けです", "では、1d20/1d100のSANcです",
      "食らっちゃうよ～ん", "ちくわ大明神", "あなたはいまほんとうにただしいあなた？", "わたしはわたし？それともあなた？", "33-4",
      "いまあなたのうしろにいるの", "そしたら私がふりおろすから", "お腹すきました", "ドンペリ入りま～す", "ご主人！お帰りにゃ！",
      "お知らせです" + message.author.mention + "さんがお呼びでした", "笹食ってる場合じゃねぇ",
      "一体いつから俺が喋ると錯覚していた？", "もうちっとだけ続くんじゃ"
    ]
    choice = message.author.mention + random.choice(RP)  #←
    await message.channel.send(choice)

  if message.content == "!RPa" or message.content == "!rpa":
    #↓
    RP = [
      "「いってらっしゃい」「おかえりなさい」", "「おはよう」「おやすみ」", "「こっちにおいで」",
      "「ご飯にする？お風呂にする？それとも…」", "「さよなら」", "苦手な食べ物を前にして", "お化け屋敷にて", "「愛してるよ」",
      "「さようなら」", "初めましてじゃない「初めまして」", "「大好きだよ」「大嫌いだよ」", "嘘がバレた時の一言",
      "小さな嘘を、ひとつ", "死亡フラグ、立ててもろて", "焦った一言", "関係性が深い相手が死んだときの一言", "殺すときの一言",
      "死ぬときの一言", "復讐相手に一言", "恨み言", "大切な人が川の此方へ来た時の一言"
    ]
    choice = message.author.mention + random.choice(RP)  #←
    await message.channel.send(choice)

  if message.content == "!RPe" or message.content == "!rpe":
    #↓
    RP = [
      "「いってらっしゃい」「おかえりなさい」", "「おはよう」「おやすみ」", "「こっちにおいで」",
      "「ご飯にする？お風呂にする？それとも…」", "「さよなら」", "苦手な食べ物を前にして", "お化け屋敷にて"
    ]
    choice = message.author.mention + random.choice(RP)  #←
    await message.channel.send(choice)

  if message.content == "!RPm" or message.content == "!rpm":
    #↓
    RP = [
      "「愛してるよ」", "「さようなら」", "初めましてじゃない「初めまして」", "「大好きだよ」「大嫌いだよ」", "嘘がバレた時の一言",
      "小さな嘘を、ひとつ", "死亡フラグ、立ててもろて", "焦った一言"
    ]
    choice = message.author.mention + random.choice(RP)  #←
    await message.channel.send(choice)

  if message.content == "!RPd" or message.content == "!rpd":
    #↓
    RP = [
      "関係性が深い相手が死んだときの一言", "殺すときの一言", "死ぬときの一言", "復讐相手に一言", "恨み言",
      "大切な人が川の此方へ来た時の一言"
    ]
    choice = message.author.mention + random.choice(RP)  #←
    await message.channel.send(choice)

  # /ch_create チャンネル名 というコマンドで反応する
  # /ch_createだけだと末尾の空白がDiscordの仕様により自動で削除されるため反応しない
  if message.content.startswith('/ch_create '):

    # チャンネル名を取得
    ch_name = message.content.replace('/ch_create ', '').split()[0]
    if ch_name.startswith('@'):
      await message.channnel.send("作り方が間違っています！")
    guild = message.guild
    mentions = message.mentions

    addrole = await guild.create_role(name=ch_name)
    await message.author.add_roles(addrole)
    for mention in mentions:
      await mention.add_roles(addrole)
    msg = "Roles ok"
    await message.channel.send(msg)
    # 権限を編集して作成するには以下のコードを追加
    permission = {
      message.guild.default_role:
      discord.PermissionOverwrite(read_messages=False),
      message.guild.me:
      discord.PermissionOverwrite(read_messages=True),
      addrole:
      discord.PermissionOverwrite(read_messages=True)
    }

    # チャンネルを作成するカテゴリを取得
    categoryid = message.channel.category_id
    category = message.guild.get_channel(categoryid)

    #取得したカテゴリに指定した名前でチャンネルを作成
    ch = await category.create_text_channel(name=ch_name,
                                            overwrites=permission)

    await message.channel.send("チャンネルを作成しました。")

  if message.content.startswith('/chro_delete '):
    guild = message.guild
    mentions = message.mentions

    rolename = message.content.replace('/chro_delete ', '')
    await message.channel.send("delete")
    role = discord.utils.get(message.guild.roles, name=rolename)
    target = discord.utils.get(message.guild.channels, name=rolename)
    await role.delete()
    await target.delete()

  if message.content.startswith('/role_delete '):
    guild = message.guild
    mentions = message.mentions

    rolename = message.content.replace('/role_delete ', '')
    await message.channel.send("delete")
    role = discord.utils.get(message.guild.roles, name=rolename)
    await role.delete()

  if message.content.startswith('/ch_delete '):
    guild = message.guild
    mentions = message.mentions

    rolename = message.content.replace('/ch_delete ', '')
    await message.channel.send("delete")
    target = discord.utils.get(message.guild.channels, name=rolename)
    await target.delete()

  if message.content.startswith('/addrole '):
    guild = message.guild
    channel = message.channel
    rolename = message.content.replace('/addrole ', '').split()[0]
    role = discord.utils.get(guild.roles, name=rolename)
    await channel.set_permissions(role, read_messages=True)

  if message.content.startswith('/rc '):
    guild = message.guild
    r = random.randint(1, 256)
    g = random.randint(1, 256)
    b = random.randint(1, 256)
    rolename = message.content.replace('/rc ', '').split()[0]
    role = discord.utils.get(guild.roles, name=rolename)
    await role.edit(colour=discord.Colour.from_rgb(r, g, b))

  if message.content.startswith('/roleplus '):

    # チャンネル名を取得
    rolename = message.content.replace('/addrole ', '').split()[0]
    role = discord.utils.get(guild.roles, name=rolename)
    if rolename.startswith('@'):
      await message.channnel.send("作り方が間違っています！")
    guild = message.guild
    mentions = message.mentions

    for mention in mentions:
      await mention.add_roles(role)
    msg = "Roles ok"
    await message.channel.send(msg)

  if message.content.startswith('/r '):
    n = message.content.replace('/r ', '').split()[0]
    diceroll.call(n)


client.run(TOKEN)

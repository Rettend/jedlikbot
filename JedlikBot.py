import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands
#-------------------DATA---------------------

owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='-', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
permissions = discord.Permissions
PRserver = "Block TDM"
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
#--------------------------------------------

#-----------------SETUP----------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Block TDM!'))

class NoPermError(Exception):
    pass
#--------------------------------------------

#----------------COMMANDS--------------------
@bot.command(pass_context=True)
async def slap(ctx, member : discord.Member=None, *, Reason=None):
    if member is None:
        await bot.reply("**Usage: `-slap {member} {Reason}` thx.**")
    else:
        await bot.say(f"**{ctx.message.author} slaps {member.mention}, for __{Reason}__**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-unban {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `-slap {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            banneds = await bot.get_bans(ctx.message.server)
            if user not in banneds:
                bot.say("**Plz mention a banned user!**")
            else:
                room = ctx.message.channel
                await bot.unban(ctx.message.server, user)
                LogRoom = bot.get_channel(id="488714781738532864")
                await bot.say(f"**{user.mention} got unbanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
                em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xe91e63)
                em.add_field(name="User", value=f"{user.mention}")
                em.add_field(name="Moderator", value=f"{ctx.message.author}")
                em.add_field(name="Reason", value=f"{Reason}")
                em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
                em.set_footer(text=timer)
                await bot.send_message(LogRoom, embed=em)
                Private = await bot.start_private_message(user)
                await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unbanned from {PRserver}, Ready to join back?\nhttps://discord.gg/Cf833k8**")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User=None, Day : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Day is None:
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="488714781738532864")
            await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nBAMM!! You got banned from {PRserver}, bai bai!**\n*Thor made hes best...*")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-kick {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `-kick {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.kick(user)
            LogRoom = bot.get_channel(id="488714781738532864")
            await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓚𝓘𝓒𝓚⧸⎠╱", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got kicked from {PRserver}, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `-mute {member} {duration(in sec)} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="488714781738532864")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.add_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x11806a)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.add_field(name="Duration", value=f"{duration} sec")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nRoses are red, violets are blue and {user.mention} is muted!**")
            await asyncio.sleep(duration)
            await bot.remove_roles(user, MutedRole)
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Time is up...")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unmuted, dont get too excited..**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-unmute {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `-unmute {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="488714781738532864")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.remove_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unmuted, dont get too excited..**")
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "OMG REALLY SLOW!!"
    elif 399 > pinges > 141:
        mesg = "Ah not good!"
    elif pinges < 140:
        mesg = "Perfect ;)"
    em = discord.Embed(title=None, description=f":ping_pong: It seems `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `-lock {duration (in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `-lock {duration (in sec)} {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
        LogRoom = bot.get_channel(id="488714781738532864")
        em = discord.Embed(title="╲⎝⧹𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x1f8b4c)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="488714781738532864")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `-unlock {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="488714781738532864")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        await bot.reply("**The usage is `-clear {number of messages to delete}` ty.**")
    else:
        number += 1
        deleted = await bot.purge_from(ctx.message.channel, limit=number)
        num = number - 1
        LogRoom = bot.get_channel(id="488714781738532864")
        em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        msg = await bot.send_message(ctx.message.channel, embed=em)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(4)
        await bot.delete_message(msg)

@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**Usage: `-game {something}` thanks.**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status changed to: __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**Usage: `-name {something}` ty, boi.**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick is now: __{name}__!", colour=0x3498db)
        await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def say(ctx, *, words=None):
    if words is None:
        await bot.reply("**Usage: `-say {something}` ty.**")
    else:
        await bot.say(f"**{words}**")
        
@bot.listen()
async def on_member_join(member):
    botserver = bot.get_server(id="488644647111884810")
    membersroom = bot.get_channel(id="488700806980304906")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    room = bot.get_channel(id="488713523497664513")
    em = discord.Embed(title=f"__{member.name}__ Joined!", description=f"**Welcome {member.mention}, have a great time here! Chat, Search for playing-mates or just listen to music ;)**", colour=0x3498db)
    em.set_thumbnail(url="https://cdn.discordapp.com/emojis/391322023739129856.png?v=1")
    await bot.send_message(room, embed=em)
   
@bot.listen()
async def on_member_remove(member):
    botserver = bot.get_server(id="488644647111884810")
    membersroom = bot.get_channel(id="488700806980304906")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    room2 = bot.get_channel(id="488713523497664513")
    await bot.send_message(room2, f"**{member} left without saying anything...** <:thinkSad:488707679502729226>")
#-----------------------------------------------
#-----------------------------------------------

@bot.event
async def on_message(message):
    if message.content.startswith("-infos"):
        if message.author.id in owner:
            planroom = bot.get_channel(id="488701294287126528")
            dev = discord.utils.get(ctx.message.server.roles, name="Developer Team")
            mod = discord.utils.get(ctx.message.server.roles, name="Moderator")
            gt = discord.utils.get(ctx.message.server.roles, name="Game Tester")
            bf = discord.utils.get(ctx.message.server.roles, name="Bug Finder")
            gamehelper = discord.utils.get(ctx.message.server.roles, name="Game Helper")
            await bot.send_message(message.channel, f"**__The Official Discord Server of Block TDM__**\n\n\n"
                                   "__Roles:__\n\n"
                                   f"{dev}: The Developers of the game, scripters, builders and Designers\n"
                                   f"{mod}: The Server Moderators, they can use the moderation commands, beware spammers!!\n"
                                   f"{gt}: awesome persons, they help to make the game better.\n"
                                   f"{bf}: there are lot of bugs in every game, we need to find them <:pepeBigEyes:488707890044076032>\n"
                                   f"{gamehelper}: a helpful guy, who has good ideas for the game :)\n\n"
                                   "__Infos:__\n\n"
                                   f"The Game-updates wont get posted to this server only to the Roblox website.\n"
                                   f"But the future plans will be in the {planroom} room.\n"
                                   f"**The Bot of the server is {bot.user.mention}, made by Rettend**\n"
    if message.content.startswith("-time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, the time is: __{timer}__**")
    if message.content.startswith("-mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":small_blue_diamond: r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}\n"
                     ":black_small_square: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":small_orange_diamond: r-unban {member} \"{Reason}\"\n"
                     ":black_small_square: UnBans the Banned user, the user now can rejoin by instant-invite links\n\n\n")
        em.add_field(name="Mod commands", value=":small_blue_diamond: r-kick {member} {Reason}\n"
                     ":black_small_square: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":small_orange_diamond: r-mute {member} {duration(in sec)} {Reason}\n"
                     ":black_small_square: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":small_blue_diamond: r-unmute {member} {Reason}\n"
                     ":black_small_square: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":small_orange_diamond: r-lock {Reason}\n"
                     ":black_small_square: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":small_blue_diamond: r-unlock {Reason}\n"
                     ":black_small_square: Unlocks the currently locked channel, now everyone can send messages there\n"
                     "\n"
                     ":small_orange_diamond: r-clear {number of messages to delete}\n"
                     ":black_small_square: Deletes a specific amount of messages")
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('-8ball'):
        await bot.send_message(message.channel, random.choice(['**It is certain :8ball:**',
                                                              '**It is decidedly so :8ball:**',
                                                              '**Without a doubt :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Boi, go sleep... :8ball:**',
                                                              '**As i see it, yes :8ball:**',
                                                              '**As i see it, *No U*   :8ball:**',
                                                              '**Most likely :8ball:**',
                                                              '**Outlook good :8ball:**',
                                                              '**Yes :8ball:**',
                                                              '**Signs point to yes :8ball:**',
                                                              '**Reply hazy try again :8ball:**',
                                                              '**Ask again later, nub :8ball:**',
                                                              '**Better not tell you :8ball:**',
                                                              '**Cannot predict now :8ball:**',
                                                              '**Concentrate and ask again :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Dont count on it :8ball:**',
                                                              '**My reply is no :8ball:**',
                                                              '**My sources say no :8ball:**',
                                                              '**Outloook not so good :8ball:**',
                                                              '**Very doubtful :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Ask it to ur mum :8ball:**',
                                                              ':feelsUltraREE: ***REEEE* :8ball:**',]))
    if message.content.startswith("-help"):
        Rettend = discord.utils.get(message.server.members, id="361534796830081024")
        em = discord.Embed(title="HELP", description="__Hey! Dont get Scared, Ask for help!__\n"
                           "\n"
                           ":small_blue_diamond: Try `r-mod` to get the moderator commands, but you need to be Moderator to use them!\n"
                           ":white_small_square: Use the `r-list` command to get all of the commands!\n"
                           f":small_blue_diamond: If you have any questions, ask it to {Rettend.mention}", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/430347128100093962.gif?v=1")
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('-lenny'):
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        await bot.send_message(message.channel, "**A wild Lenny has appeard:**\n\n\t" + lenny)
    if message.content.startswith('!oof'):
        o = ['o00', 'oo', 'oO', 'o0', 'Oo', '0o', 'OOo', 'O0o', 'ooO', 'oo0', 'oo0oO', 'o0o', '0ooO', 'oo0oOO', 'ooo', '0oo', 'oooo', 'Ooo0', 'O0oo', 'ooo0', ]
        f = ['f', 'ff', 'fff']
        mark = ['!', '!!', '!!', '!1', '!!1', '!1!!', '1!!!', '!1!1!', '1!', '!!1!', '!!!1!', '!!!!', '!11!']
        msg1 = random.choice(o)
        msg2 = random.choice(f)
        msg3 = random.choice(mark)
        await bot.send_message(message.channel, msg1 + msg2 + msg3)
    if message.content.startswith('-leavepls'):
        em5 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:", colour=0x3498db)
        msg = await bot.send_message(message.channel, embed=em5)
        await asyncio.sleep(1)
        em4 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em4)
        await asyncio.sleep(1)
        em3 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em3)
        await asyncio.sleep(1)
        em2 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em2)
        await asyncio.sleep(1)
        em1 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n", colour=0x3498db)
        await bot.edit_message(msg,  embed=em1)
        await asyncio.sleep(1)
        em0 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em0)
        await asyncio.sleep(1)
        em = discord.Embed(title="lol Joke", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/423864027610087426.png?v=1")
        await bot.edit_message(msg,  embed=em)
    if message.content.startswith('-list'):
        await bot.send_message(message.channel, "**Usage: `r-list 1` and `r-list 2`**")
    if message.content.startswith('-list 1'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=
                            ':white_small_square: r-slap\n'
                            ':small_blue_diamond: r-ping\n'
                            ':white_small_square: r-game\n'
                            ':small_blue_diamond: r-nick\n'
                            ':white_small_square: r-say', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of Block TDM Discord, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help 2 for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('-list 2'):
        emb = discord.Embed(title='MY COMMANDS:', description="Hey, check out my commands!", colour=0x3498db)
        emb.add_field(name='--------------------', value=
                            ':small_blue_diamond: r-time\n'
                            ':white_small_square: r-mod\n'
                            ':small_blue_diamond: r-help\n'
                            ':white_small_square: r-8ball\n'
                            ':small_blue_diamond: r-lenny\n'
                            ':white_small_square: r-oof\n'
                            ':small_blue_diamond: r-leavepls\n'
                            ':white_small_square: r-list', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        emb.set_footer(text='The Official Bot of Block TDM Discord, inviting and using the Bot in other servers breaks the Term of Use.\nType r-help for more commands!!')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT


    
    
       
token = os.environ.get('DISCORD_TOKEN')
bot.run(token)

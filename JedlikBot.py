import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands
#-------------------DATA---------------------

owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='!', description=None)
bot.remove_command("help")
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
permissions = discord.Permissions
"""timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""
#--------------------------------------------

#-----------------SETUP----------------------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Suli!'))
    await bot.create_channel(bot.user.server, 'JedlikBot szoba', type=discord.ChannelType.text)

class NoPermError(Exception):
    pass
#--------------------------------------------

#----------------COMMANDS--------------------
"""@bot.command(pass_context=True)
async def selfrole(ctx, role : discord.Role=None):
    dj_role = discord.utils.get(ctx.message.server.roles, id="403594320634052610")
    radish_role = discord.utils.get(ctx.message.server.roles, id="380764242757943326")
    thonker_role =discord.utils.get(ctx.message.server.roles, id="381139610924875787")
    noe_role = discord.utils.get(ctx.message.server.roles, id="435090845960634378")
    selfroles = [dj_role, radish_role, thonker_role, noe_role]
    global color
    if selfrole is radish_role:
        color = 0xe74c3c
    elif selfrole is dj_role:
        color = 0x3498db
    elif selfrole is thonker_role:
        color = 0x206694
    elif selfrole is noe_role:
        color = 0x95a5a6
    if role is None:
        e = discord.Embed(title="Selfroles", description="The usage is `r-selfrole {selfrole}`," + f" the available Selfroles are:\n{dj_role.mention}\n{radish_role.mention}\n{thonker_role.mention}\n{noe_role.mention}", colour=0x3498db)
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        e.set_footer(text=timer)
    elif role not in selfroles:
        e = discord.Embed(title="Selfroles", description=f"That role isnt a Selfrole! The available Selfroles are:\n{dj_role.mention}\n{radish_role.mention}\n{thonker_role.mention}\n{noe_role.mention}", colour=0x3498db)
        e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        e.set_footer(text=timer)
    else:
        if role not in ctx.message.author.roles:
            await bot.add_roles(ctx.message.author, role)
            e = discord.Embed(title="Selfroles", description=f"Selfrole found!\nSelfrole ({role.mention}) added succesfuly!", colour=color)
            e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            e.set_footer(text=timer)
        else:
            await bot.remove_roles(ctx.message.author, role)
            e = discord.Embed(title="Selfroles", description=f"Selfrole found!\nSelfrole ({role.mention}) removed succesfuly!", colour=color)
            e.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            e.set_footer(text=timer)
    await bot.say(embed=e)"""

@bot.command(pass_context=True)
async def kivok(ctx):
    LemonRoom = bot.get_channel(id="435081405899210754")
    msg = [" vagy Anyád", " vagy Sir Lancelot", " buzi :couple_mm: vagy", " :regional_indicator_t: :regional_indicator_e:", " vagy a Terminátor!!", ", Igen.", " vagy én", " Nem.", " vagy a Te", " vagy SuperMario", "... Its Raining Man!", " vagy a HALÁL", " vagy anyád gyereke", " vagy ( ͡° ͜ʖ ͡°) <-- ő", " egy csirke vagy", " még mindig egy csirke vagy", " vagy Senki", " vagy, mé ki vagy te?", ", PÉÉÉNISZ", " vagy az ördög >:)", " vagy Donald Trump", " megilyedtél (ha ha)", " vagy Valaki"]
    smsg = random.choice(msg)
    colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = random.choice(colours)
    em = discord.Embed(title="Ki vagyok?", description=f"**\n{ctx.message.author}, Te{smsg}**", colour=col)
    em.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.send_message(ctx.message.channel, embed=em)

@bot.command(pass_context=True)
async def pofon(ctx, member : discord.Member=None, *, Reason=None):
    if member is None:
        await bot.reply("**Használat: `r-pofon {felhasználó} {ok}` köcce.**")
    else:
        await bot.say(f"**{ctx.message.author} pofonvágta {member.mention}-t mer: __{Reason}__**")

@bot.command(pass_context=True)
async def kill(ctx, user : discord.User=None):
    if user is None:
        await bot.reply("**Használat: `r-kill {felhasználó}` köszi :).**")
    else:
        life = ["Yes", "Yes2"]
        yourlife = random.choice(life)
        if yourlife == "Yes":
            await bot.say(f"**{ctx.message.author} megölte {user.mention}-t, mer megteheti**")
        elif yourlife == "Yes2":
            await bot.say(f"**{ctx.message.author} megölte {user.mention}-t mer mér ne?**")

"""@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `r-unban {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-slap {member} {Reason}` ty.**")
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
                LogRoom = bot.get_channel(id="401752340366884885")
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
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    elif Day is None:
        await bot.reply("**The usage is `r-ban {member} {0 - 7 amount of days to delete his messages} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="401752340366884885")
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
        await bot.reply("**The usage is `r-kick {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-kick {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.kick(user)
            LogRoom = bot.get_channel(id="401752340366884885")
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
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `r-mute {member} {duration(in sec)} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="401752340366884885")
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
        await bot.reply("**The usage is `r-unmute {member} {Reason}` ty.**")
    elif Reason is None:
        await bot.reply("**The usage is `r-unmute {member} {Reason}` ty.**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="401752340366884885")
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
            await bot.send_message(Private, f"**`Server: {PRserver}`\nHey! You got unmuted, dont get too excited..**")"""
        
@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Az sok!"
    elif pinges > 1000:
        mesg = "AZTAROHADT DE LASSÚ"
    elif 399 > pinges > 141:
        mesg = "a nem jó!"
    elif pinges < 140:
        mesg = "tökéletes ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Ez most `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

"""@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `r-lock {duration (in sec)} {Reason}` ty.**")
    elif duration is None:
        await bot.reply("**The usage is `r-lock {duration (in sec)} {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
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
        LogRoom = bot.get_channel(id="401752340366884885")
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
        await bot.reply("**The usage is `r-unlock {Reason}` ty.**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Registered")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="401752340366884885")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)"""
    
@bot.command(pass_context=True)
async def clear(ctx, number : int=None):
    if ctx.message.author.id in owner:
        if number is None:
            await bot.reply("**The usage is `r-clear {number of messages to delete}` ty.**")
        else:
            number += 1
            deleted = await bot.purge_from(ctx.message.channel, limit=number)
            num = number - 1
            em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            """msg = await bot.send_message(ctx.message.channel, embed=em)
            await asyncio.sleep(4)
            await bot.delete_message(msg)"""

"""@bot.command(pass_context=True)
async def roll(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `r-roll {number} {number}` ty.**")
    elif y is None:
        await bot.reply("**The usage is `r-roll {number} {number}` ty.**")
    else:
        msg = random.randint(x, y)
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Oh, my choose: {msg}**")
"""
@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `r-sub {szám} {szám}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `r-sub {szám} {szám}` köcce.**")
    else:
        msg = x - y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Ez: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `r-mul {szám} {szám}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `r-mul {szám} {szám}` köcce.**")
    else:
        msg = x * y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Ez: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `r-div {szám} {szám}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `r-div {szám} {szám}` köcce.**")
    else:
        msg = x / y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Ez: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `r-exp {szám} {szám}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `r-exp {szám} {szám}` köcce.**")
    else:
        msg = x ** y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Ez: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**Használat: `r-add {szám} {szám}` köcce.**")
    elif y is None:
        await bot.reply("**Használat: `r-add {szám} {szám}` köcce.**")
    else:
        msg = x + y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**Ez: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**Használat: `r-game {valami}` köcce.**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status mostmár: __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**Használat: `r-name {valami a nevednek}` köcce.**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author} neve már: __{name}__!", colour=0x3498db)
        await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def say(ctx, *, words=None):
    if words is None:
        await bot.reply("**Használat: `r-say {valami}` köcce.**")
    else:
        await bot.say(f"**{words}**")
#-----------------------------------------------
#-----------------------------------------------

@bot.event
async def on_message(message):
    if message.content.startswith("!pénisz"):
        await bot.send_message(message.channel, "**Pééééééééénisz!!!**")
    if message.content.startswith("!anyád"):
        await bot.send_message(message.channel, "**tied**")
    if message.content.startswith("!time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, az idő: __{timer}__**")
    """if message.content.startswith("!mod"):
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
        await bot.send_message(message.channel, embed=em)"""
    if message.content.startswith('!8ball'):
        await bot.send_message(message.channel, random.choice(['**Ez természetes :8ball:**',
                                                              '**Ez már eldölt tehát ja :8ball:**',
                                                              '**Mér ne :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Haver, menyj aludni... :8ball:**',
                                                              '**ALUGYÁ ÉS HAGGYÁ ENGEM :8ball:**',
                                                              '**Ahogy látom, *No U*   :8ball:**',
                                                              '**Ahogy látom, igen :8ball:**',
                                                              '**Jók a kilátások :8ball:**',
                                                              '**Ja :8ball:**',
                                                              '**Nem :8ball:**',
                                                              '**Sztem nem :8ball:**',
                                                              '**Máskor... :8ball:**',
                                                              '**Inkább nem mondom meg xd :8ball:**',
                                                              '**Mittomén :8ball:**',
                                                              '**Koncentrálj majd kérdezd újra. :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Igen. :8ball:**',
                                                              '**Lehet :8ball:**',
                                                              '**Az univerzum szerintem nem :8ball:**',
                                                              '**Az univerzum fáradt :8ball:**',
                                                              '**Az univerzum üzente: Anyád :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Anyádtól kérdezd :8ball:**',
                                                              '**? :8ball:**',]))
    if message.content.startswith('!lenny'):
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
    if message.content.startswith('!leavepls'):
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
    if message.content.startswith('!list'):
        await bot.send_message(message.channel, "**Használd az `r-list 1` és `r-list 2` parancsokat**")
    if message.content.startswith('!list 1'):
        emb = discord.Embed(title='MY COMMANDS:', description="Ezek vannak", colour=0x3498db)
        emb.add_field(name='--------------------', value=
                            ':white_small_square: !kivok\n'
                            ':small_blue_diamond: !pofon\n'
                            ':white_small_square: !kill\n'
                            ':small_blue_diamond: !ping\n'
                            ':white_small_square: !suv\n'
                            ':small_blue_diamond: !mul\n'
                            ':white_small_square: !div\n'
                            ':small_blue_diamond: !exp\n'
                            ':white_small_square: !add\n'
                            ':small_blue_diamond: !nick\n'
                            ':white_small_square: !mond\n'
                            ':small_blue_diamond: !game\n', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('!list 2'):
        emb = discord.Embed(title='MY COMMANDS:', description="Ezek vannak még", colour=0x3498db)
        emb.add_field(name='--------------------', value=':small_blue_diamond: r-time\n'
                            ':white_small_square: r-8ball\n'
                            ':small_blue_diamond: r-lenny\n'
                            ':white_small_square: r-oof\n'
                            ':small_blue_diamond: r-leavepls\n'
                            ':white_small_square: r-list\n', inline=False)
        emb.set_thumbnail(url='https://cdn.discordapp.com/emojis/385152309090451467.png?v=1')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT


    
    
       
token = os.environ.get('DISCORD_TOKEN')
bot.run(token)

from asyncio.tasks import wait
from gc import DEBUG_SAVEALL
from typing import final
import discord
import random
import time
import asyncio
from discord.message import convert_emoji_reaction
from sqlalchemy import create_engine, Table, Column, Integer, Float, MetaData, select, desc 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import user



#DATABASE TABLE

engine = create_engine('sqlite:///classement.db')
db = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class classement(db):
    __tablename__ = 'classement'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    wins = Column(Integer)
    loses = Column(Integer)
    winrate = Column(Float)
    score = Column(Integer)

    def __repr__(self):
        return "<User(user_id='%s', wins='%s', loses='%s', winrate='%s')>" % (self.user_id, self.wins, self.loses, self.winrate)

db.metadata.create_all(engine)



CHOICE = ["π€", "π","β"]
YES_NO = ["β", "β"]
DISCORD_BOT_TOKEN = "ENTER YOUR TOKEN HERE"



def get_random_choice():
    """This function return a random choice for the bot"""
    choice = random.choice(CHOICE)
    return choice

def check(reaction, user):
    return reaction, user

def who_has_won(host_choice, host_mention, opponent_choice, opponent_mention, game_mode, host_id, opponent_id=814170233659981904):
    """This function return a tuple with string with the result, winner id, loser id """

    if game_mode == "vs":
        if host_choice == opponent_choice:
            return "EgalitΓ© ! la partie va recommencer...", None, None
        elif host_choice == "π€" and opponent_choice == "π":
            return f"π {host_mention} a gagnΓ© ! π", host_id, opponent_id
        elif host_choice == "π" and opponent_choice == "β":
            return f"π {host_mention} a gagnΓ© ! π", host_id, opponent_id
        elif host_choice == "β" and opponent_choice == "π€":
            return f"π {host_mention} a gagnΓ© ! π", host_id, opponent_id
        else:
            return f"π {opponent_mention} a gagnΓ© ! π", opponent_id, host_id
    elif game_mode == "solo":
        if host_choice == opponent_choice:
            return "EgalitΓ© ! la partie va recommencer...", None, None
        elif host_choice == "π€" and opponent_choice == "π":
            return f"π {host_mention} a gagnΓ© ! π", host_id, opponent_id
        elif host_choice == "π" and opponent_choice == "β":
            return f"π {host_mention} a gagnΓ© ! π", host_id, opponent_id
        elif host_choice == "β" and opponent_choice == "π€":
            return f"π^{host_mention} a gagnΓ© ! π", host_id, opponent_id
        else:
            return f"DΓ©solΓ©, j'ai gagnΓ© :)", opponent_id, host_id

def add_result_to_classement(winner_id:int, loser_id:int):
    #gagnant :
    winner = session.query(classement).filter_by(user_id=winner_id).first()
    if winner == None:
        new_user = classement(
            user_id=winner_id,
            wins=1,
            loses=0,
            winrate=100.0,
            score=10,
        )
        session.add(new_user)
    else:
        winner.winrate = round((winner.wins + 1) / (winner.loses + winner.wins + 1), 1) * 100
        winner.wins += 1
        winner.score += 10
    
    #LOSER
    loser = session.query(classement).filter_by(user_id=loser_id).first()
    if loser == None:
        new_user = classement(
            user_id=loser_id,
            wins=0, 
            loses=1,
            winrate=0.0,
            score=0,
        )
        session.add(new_user)
    else:
        loser.winrate = round(loser.wins / (loser.loses + 1), 1) * 100
        loser.loses += 1
        if loser.score != 0:
            loser.score -= 5
    session.commit()

    return



#DISCORD PART

client = discord.Client(activity=discord.Game(""))


#Statut

command1 = ["!sh : Affronte Narwing_", "!sh vs @ : Affronte ton ami", "!classement : Affiche le classement"]
command2 = ["ping", "quoi"]
async def status_task():
    while True:
        SAME_MSG = True
        try:
            oldmessage = botmessage
        except:
            oldmessage = None

        while SAME_MSG:
            richloop = random.randint(0, 1)
            print(richloop)
            if richloop == 0:
                botmessage = command1[(random.randint(0, len(command1)) - 1)]
                print(botmessage)
            else:
                botmessage = command2[(random.randint(0, len(command2)) - 1)]
                print(botmessage)

            if oldmessage == botmessage:
                SAME_MSG = True
            else:
                SAME_MSG = False

        await client.change_presence(activity=discord.Game(name=botmessage))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    client.loop.create_task(status_task())

#Statut

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    host = message.author
    host_mention = f"<@!{host.id}>"


# Fun Msg

    if message.content.startswith('ping'):
        bot_msg = await channel.send("pong")


    if message.content.endswith('quoi'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('koi'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('kuoi'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('qoi'):
        bot_msg = await channel.send("FEUR !")
 
    if message.content.endswith('quoi?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('koi?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('kuoi?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('qoi?'):
        bot_msg = await channel.send("FEUR !")

    if message.content.endswith('quoi ?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('koi ?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('kuoi ?'):
        bot_msg = await channel.send("FEUR !")
    if message.content.endswith('qoi ?'):
        bot_msg = await channel.send("FEUR !")

    if message.content.endswith('ouais'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('oue'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouΓ©'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uΓ©'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouai'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wai'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wΓ©'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uai'):
        bot_msg = await channel.send("STERN !")

    if message.content.endswith('ouais?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('oue?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouΓ©?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uΓ©?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouai?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wai?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wΓ©?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uai?'):
        bot_msg = await channel.send("STERN !")

    if message.content.endswith('ouais ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('oue ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouΓ© ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uΓ© ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('ouai ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wai ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('wΓ© ?'):
        bot_msg = await channel.send("STERN !")
    if message.content.endswith('uai ?'):
        bot_msg = await channel.send("STERN !")


    if message.content.endswith('OUI'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('oui'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ui'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wi'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wui'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouii'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouiii'):
        bot_msg = await channel.send("STITI !")

    if message.content.endswith('OUI?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('oui?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ui?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wi?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wui?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouii?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouiii?'):
        bot_msg = await channel.send("STITI !")

    if message.content.endswith('OUI ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('oui ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ui ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wi ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('wui ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouii ?'):
        bot_msg = await channel.send("STITI !")
    if message.content.endswith('ouiii ?'):
        bot_msg = await channel.send("STITI !")


    if message.content.endswith('NON'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('non'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('nn'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('NN'):
        bot_msg = await channel.send("BRIL !")

    if message.content.endswith('NON?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('non?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('nn?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('NN?'):
        bot_msg = await channel.send("BRIL !")

    if message.content.endswith('NON ?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('non ?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('nn ?'):
        bot_msg = await channel.send("BRIL !")
    if message.content.endswith('NN ?'):
        bot_msg = await channel.send("BRIL !")


# Fun Msg


# ANNONCE !

    if message.content.startswith('!annonce'):
            mcs = message.content.split(' ')[1:]
            new_mcs = ''

            for i in mcs:
                new_mcs = new_mcs + ' ' + i
            embed = discord.Embed(title="ANNONCE !", description = new_mcs, color=0x9208ea)
            embed.set_footer(text=f"Par : {host}", icon_url=host.avatar_url)
            bot_msg = await channel.send(embed=embed)

# ANNONCE !


# Bienvenu msg



# Bienvenu msg


    if message.content.startswith('!sh vs'):
        try:
            opponent = message.content.split(' ')[2]
            try:
                opponent_id = int(opponent.split("!")[1].split('>')[0])
                opponent_mention = f"<@!{opponent_id}>"
            except IndexError:
                opponent_id = int(opponent.split("@")[1].split('>')[0])
                opponent_mention = f"<@!{opponent_id}>"

        except (IndexError, ValueError):
            embed = discord.Embed(title="DΓ©solΓ©, vous devez mentionner quelqu'un.", description="**RΓ©essayez.**")
            embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
            bot_msg = await channel.send(embed=embed)

        if "@" not in opponent_mention:
            embed = discord.Embed(title="DΓ©solΓ©, ce pseudo est invalide.", description="**RΓ©essayez.**")
            embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
            bot_msg = await channel.send(embed=embed)

        elif opponent_mention == host_mention or opponent_mention == f"<@!{client.user.id}>":
            embed = discord.Embed(title="DΓ©solΓ©, vous ne pouvez pas vous battre vous-mΓͺme ou contre moi.", description="**RΓ©essayez.**")
            embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
            bot_msg = await channel.send(embed=embed)

        elif "<@" in opponent:
            timeout = 10
            timer = 0
            embed = discord.Embed(title=f"Invitation d'un match de Shifumi !", description=f"**{opponent}, accepte le match avec : β, refuse avec : β**\nVous avez encore **{timeout} secondes**.")
            embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
            bot_msg = await channel.send(embed=embed)
            for emoji in YES_NO:
                await bot_msg.add_reaction(emoji)

            def check_yes_no_opponent(reaction, user):
                return f"<@!{user.id}>" == opponent_mention and (str(reaction)in YES_NO)

            while timeout != 0:
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout=1, check=check_yes_no_opponent)
                    if reaction != None:
                        if str(reaction) == YES_NO[0]:
                            game_continue = True
                        else:
                            game_continue = False
                        break
                except asyncio.TimeoutError:
                    if timer == 20:
                        game_continue = False
                    else:
                        timer += 1
                        pass
                timeout -= 1
                if timeout == 0:
                    embed = discord.Embed(title=f"Invitation d'un match de Shifumi!", description="L'invitation Γ  expirΓ©.")
                    embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                    await bot_msg.edit(embed=embed)
                    await bot_msg.clear_reactions()
                    return
                else:
                    embed = discord.Embed(title=f"Invitation d'un match de Shifumi!", description=f"**{opponent}, accepte le match avec : β, refuse avec : β**\nIl vous reste **{timeout} secondes**.")
                    embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                    await bot_msg.edit(embed=embed)

            if game_continue is False:
                await bot_msg.clear_reactions()
                embed = discord.Embed(title=f"Invitation RefusΓ©e !")
                embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                await bot_msg.edit(embed=embed)
                return

            else:
                game_end = False
                out_of_time = False
                while not game_end:
                    await bot_msg.clear_reactions()
                    decount_until_start = 3
                    timer = 0
                    embed = discord.Embed(title=f"Invitation AcceptΓ©e !", description=f"**La partie va commencer...**")
                    embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                    await bot_msg.edit(embed=embed)
                    while decount_until_start != 0:
                        time.sleep(1)
                        decount_until_start -= 1
                        if decount_until_start > 1:
                            indications = ":yellow_circle: **READY ??**:yellow_circle:"
                        elif decount_until_start == 1:
                            indications = ":orange_circle: **SET ...** :orange_circle:"
                        elif decount_until_start == 0:
                            indications = ":red_circle: GO ! :red_circle:"
                        embed = discord.Embed(title=f"Shifumi Match !", description=f"**Choisi la rΓ©action que tu veux quand le compteur est Γ©gal Γ  0\nπ€ = Feuille\nπ = Pierre\nβ = Ciseaux\n**")
                        embed.add_field(name=f"Counter : {decount_until_start}", value=f"**{indications}**")
                        embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                        await bot_msg.edit(embed=embed)

                        if decount_until_start == 1:
                            for emoji in CHOICE:
                                await bot_msg.add_reaction(emoji)

                        elif decount_until_start == 0:
                            def check_test(reaction, user):
                                return str(reaction) in CHOICE and user.id == host.id or user.id == opponent_id

                            while not out_of_time:
                                try:
                                    reaction_1st, user_1st = await client.wait_for('reaction_add', timeout=3, check=check_test)
                                    if str(reaction_1st) in CHOICE:
                                        if user_1st.id == host.id:
                                            host_choice = str(reaction_1st)
                                        elif user_1st.id == opponent_id:
                                            opponent_choice = str(reaction_1st)
                                    try:
                                        reaction_2nd, user_2nd = await client.wait_for('reaction_add', timeout=2, check=check_test)
                                        if str(reaction_2nd) in CHOICE:
                                            if user_2nd.id == host.id:
                                                host_choice = str(reaction_2nd)
                                            elif user_2nd.id == opponent_id:
                                                opponent_choice = str(reaction_2nd)
                                            
                                            #Si EgalitΓ© : 
                                            if str(reaction_1st) != str(reaction_2nd):
                                                game_end = True
                                        break
                                    except asyncio.TimeoutError:
                                        out_of_time = True
                                except asyncio.TimeoutError:
                                    out_of_time = True


                            if out_of_time:
                                await bot_msg.clear_reactions()
                                embed = discord.Embed(title=f"Le match de Shifumi a ExpirΓ©", description=f"Vous avez mis trop de temps... RΓ©essayez.")
                                embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                                await bot_msg.edit(embed=embed)
                                return

                            else:
                                await bot_msg.clear_reactions()
                                result, winner_id, loser_id = who_has_won(host_choice, host_mention, opponent_choice, opponent_mention, "vs", int(host.id), int(opponent_id))

                                embed = discord.Embed(title=f"Les rΓ©sultats du match de Shifumi", description=f"{result}\n------------------------------\n{host_mention} : {host_choice}\n{opponent_mention} : {opponent_choice}")
                                embed.set_footer(text=f"Host : {host}", icon_url=host.avatar_url)
                                await bot_msg.edit(embed=embed)
                          
                                #On ajoute les rΓ©sutats si il n'y a pas Γ©galitΓ©
                                if winner_id != None and loser_id != None:
                                    add_result_to_classement(winner_id, loser_id)

                                if game_end:
                                    return
                                else:
                                    time.sleep(2)
                                
                        

    elif message.content.startswith("!sh"):
        timeout = 5
        while timeout >= 0:
            embed = discord.Embed(title=f"Match solo de Shifumi", description=f"{host_mention}, Etes vous prΓͺt ?\nLa partie commence dans **{timeout} secondes**")
            embed.set_footer(text=f"Player : {host}", icon_url=host.avatar_url)
            if timeout == 0:
                embed = discord.Embed(title=f"Match solo de Shifumi", description=f"{host_mention}, La partie commence MAINTENANT !")
                embed.set_footer(text=f"Player : {host}", icon_url=host.avatar_url)
            if timeout == 5:
                bot_msg = await channel.send(embed=embed)
            else:
                await bot_msg.edit(embed=embed)
            time.sleep(1)
            timeout -= 1

        game_end = False
        while not game_end:
            decount_until_start = 3
            while decount_until_start != 0:
                time.sleep(1)
                decount_until_start -= 1
                if decount_until_start > 1:
                    indications = ":yellow_circle: **READY ??**:yellow_circle:"
                elif decount_until_start == 1:
                    indications = ":orange_circle: **SET ...** :orange_circle:"
                elif decount_until_start == 0:
                    indications = ":red_circle: GO ! :red_circle:"
                embed = discord.Embed(title=f"Shifumi Match !",description=f"**Choisi la rΓ©action que tu veux quand le compteur est Γ©gal 0\nπ€ = Feuille\nπ = Pierre\nβ = Ciseaux\n**")
                embed.add_field(name=f"Counter : {decount_until_start}", value=f"**{indications}**")
                embed.set_footer(text=f"Player : {host}", icon_url=host.avatar_url)
                await bot_msg.edit(embed=embed)

                if decount_until_start == 1:
                    for emoji in CHOICE:
                        await bot_msg.add_reaction(emoji)

                elif decount_until_start == 0:
                    def check_test(reaction, user):
                        return str(reaction) in CHOICE and user.id == host.id

                    try:
                        host_choice, player = await client.wait_for('reaction_add', timeout=3.0, check=check_test)
                        

                        await bot_msg.clear_reactions()
                        bot_choice = get_random_choice()
                        if "100%winrate" in [role.name for role in player.roles]:
                            if str(host_choice) == "π€":
                                bot_choice = "π"
                            elif str(host_choice) == "π":
                                bot_choice = "β"
                            elif str(host_choice) == "β":
                                bot_choice = "π€"
                        #Si un utilisateur a un role nommΓ© "100%winrate, il gagnera Γ  chaque fois"

                        if str(host_choice) != str(bot_choice):
                            game_end = True
                        result, winner_id, loser_id = who_has_won(str(host_choice), host_mention, bot_choice, "Bot", "solo", int(host.id))

                        embed = discord.Embed(title=f"Les rΓ©sultats du match de Shifumi", description=f"{result}\n------------------------------\n{host_mention} : {host_choice}\n{client.user.mention} : {bot_choice}")
                        embed.set_footer(text=f"Player : {host}", icon_url=host.avatar_url)
                        await bot_msg.edit(embed=embed)
                        
                        #On ajoute les rΓ©sultats Γ  la database si il n'a pas Γ©galitΓ©
                        if winner_id != None and loser_id != None:
                            add_result_to_classement(winner_id, loser_id)

                        if game_end:
                            return

                    except asyncio.TimeoutError:
                        await bot_msg.clear_reactions()
                        embed = discord.Embed(title=f"Le match de Shifumi a ExpirΓ©",description=f"**Vous avez mis trop de temps... RΓ©essayez**")
                        embed.set_footer(text=f"Player : {host}", icon_url=host.avatar_url)
                        await bot_msg.edit(embed=embed)
                        return
            

    elif message.content.startswith("!classement"):
        final_str = ""
        placement = 1
        all_players = session.query(classement).order_by(desc(classement.score)).all()
        for player in all_players:
            final_str += f"{placement}. <@!{player.user_id}> : {player.score} :coin:\n"
            placement += 1
        embed = discord.Embed(title=f"Shifumi classement",description=f"**{final_str}**")
        embed.set_footer(text=f"Request by : {host}", icon_url=host.avatar_url)   
        await channel.send(embed=embed)


    elif message.content.startswith("$stats"):
        if "<@" in message.content:
            try:
                user_id = int(message.content.split("!")[1].split('>')[0])
                user_mention = f"<@!{user_id}>"
            except IndexError:
                user_id = int(message.content.split("@")[1].split('>')[0])
                user_mention = f"<@!{user_id}>"
        
        else:
            user_id = host.id
            user_mention = host_mention
        
        user_stats = session.query(classement).filter_by(user_id=user_id).first()
        if user_stats != None:
            embed = discord.Embed(title=f"Shifumi Stats",description=f"**Stats of {user_mention}**\
                \n__Matches__ : {user_stats.wins + user_stats.loses}\
                \n__Wins__ : {user_stats.wins}\
                \n__Loses__ : {user_stats.loses}\
                \n__Winrate__ : {user_stats.winrate} %\
                \n__Score__ : {user_stats.score} :coin:")
            embed.set_footer(text=f"Request by : {host}", icon_url=host.avatar_url)   
            await channel.send(embed=embed)

        else:
            embed = discord.Embed(title=f"Shifumi Stats",description=f"**L'utilisateur n'a pas de stats**")
            embed.set_footer(text=f"Request par : {host}", icon_url=host.avatar_url)
            await channel.send(embed=embed)


client.run(DISCORD_BOT_TOKEN)

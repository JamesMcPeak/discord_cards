#mao.py - mao online testing script
#
#
#woodchuck321
#woodchuck13@gmx.com
#development started OCT 25, 2020
#development "completed" NOV 27, 2020
#

import random
import discord
import time
from discord.utils import get

deck = [['2S',"<:2S:781696877124124723>"], ['7C',"<:7C:781696877678428160>"], ['KH',"<:KH:781697100848824320>"], ['AC',"<:AC:781696877833748501>"], ['4C',"<:4C:781696877397671957>"], ['JO',"<:JO:781696877828505620>"], ['6C',"<:6C:781696877622984724>"], ['10C',"<:0C:781696877501612052>"], ['10H',"<:0H:781696877527564349>"], ['AD',"<:AD:781696877350486037>"], ['9H',"<:9H:781696877707395102>"], ['JC',"<:JC:781696877740949546>"], ['AH',"<:AH:781696877791936512>"], ['10H',"<:0H:781696877527564349>"], ['6H',"<:6H:781696877648936970>"], ['6S',"<:6S:781696877799276564>"], ['8H',"<:8H:781696877724696596>"], ['JO',"<:JO:781696877828505620>"], ['8H',"<:8H:781696877724696596>"], ['AD',"<:AD:781696877350486037>"], ['4C',"<:4C:781696877397671957>"], ['9C',"<:9C:781696877976354816>"], ['9D',"<:9H:781696877757333504>"], ['9C',"<:9C:781696877976354816>"], ['JS',"<:JS:781696877396623391>"], ['QH',"<:QH:781697100919996436>"], ['4D',"<:4D:781696877640286248>"], ['3H',"<:3H:781696877561249822>"], ['QH',"<:QH:781697100919996436>"], ['6D',"<:6D:781696877614858250>"], ['10D',"<:0D:781696877506068530>"], ['2D',"<:2D:781696877547487254>"], ['9S',"<:9S:781696877707526145>"], ['4H',"<:4H:781696877615251476>"], ['9S',"<:9S:781696877707526145>"], ['5H',"<:5H:781696877292027905>"], ['6S',"<:6S:781696877799276564>"], ['6H',"<:6H:781696877648936970>"], ['3H',"<:3H:781696877561249822>"], ['JS',"<:JS:781696877396623391>"], ['9H',"<:9H:781696877707395102>"], ['QS',"<:QS:781697100969934898>"], ['AH',"<:AH:781696877791936512>"], ['QD',"<:QD:781697100760875069>"], ['AS',"<:AS:781696877690748968>"], ['3S',"<:3S:781696877565444096>"], ['3C',"<:3C:781696877557055488>"], ['QD',"<:QD:781697100760875069>"], ['JD',"<:JD:781696877728235540>"], ['10C',"<:0C:781696877501612052>"], ['5S',"<:5S:781696877665452082>"], ['KC',"<:KC:781697100513411121>"], ['10C',"<:0C:781696877501612052>"], ['10S',"<:0S:781696877518127114>"], ['9S',"<:9S:781696877707526145>"], ['QD',"<:QD:781697100760875069>"], ['JO',"<:JO:781696877828505620>"], ['QS',"<:QS:781697100969934898>"], ['4S',"<:4S:781696877640155147>"], ['JO',"<:JO:781696877828505620>"], ['10C',"<:0C:781696877501612052>"], ['AC',"<:AC:781696877833748501>"], ['4C',"<:4C:781696877397671957>"], ['2S',"<:2S:781696877124124723>"], ['2D',"<:2D:781696877547487254>"], ['3C',"<:3C:781696877557055488>"], ['2C',"<:2C:781696877225443369>"], ['6D',"<:6D:781696877614858250>"], ['8D',"<:8D:781696877690224660>"], ['5D',"<:5D:781696877678166016>"], ['KS',"<:KS:781697100647235615>"], ['9C',"<:9C:781696877976354816>"], ['9D',"<:9H:781696877757333504>"], ['8C',"<:8C:781696877766246450>"], ['10S',"<:0S:781696877518127114>"], ['8S',"<:8S:781696877565444137>"], ['8S',"<:8S:781696877565444137>"], ['7C',"<:7C:781696877678428160>"], ['7D',"<:7D:781696877648674856>"], ['7S',"<:7S:781696877656932392>"], ['7H',"<:7H:781696877871628339>"], ['7D',"<:7D:781696877648674856>"], ['JO',"<:JO:781696877828505620>"], ['10S',"<:0S:781696877518127114>"], ['5D',"<:5D:781696877678166016>"], ['6C',"<:6C:781696877622984724>"], ['KC',"<:KC:781697100513411121>"], ['5C',"<:5C:781696877610532894>"], ['JC',"<:JC:781696877740949546>"], ['5C',"<:5C:781696877610532894>"], ['CWAS',"<:CWAS:781696877489422339>"], ['AC',"<:AC:781696877833748501>"], ['4H',"<:4H:781696877615251476>"], ['JO',"<:JO:781696877828505620>"], ['KD',"<:KD:781697100752748555>"], ['8D',"<:8D:781696877690224660>"], ['QC',"<:QC:781697101058146374>"], ['QC',"<:QC:781697101058146374>"], ['6C',"<:6C:781696877622984724>"], ['8C',"<:8C:781696877766246450>"], ['2C',"<:2C:781696877225443369>"], ['2C',"<:2C:781696877225443369>"], ['2H',"<:2H:781696877258080289>"], ['9D',"<:9H:781696877757333504>"], ['7S',"<:7S:781696877656932392>"], ['7H',"<:7H:781696877871628339>"], ['7H',"<:7H:781696877871628339>"], ['4S',"<:4S:781696877640155147>"], ['5S',"<:5S:781696877665452082>"], ['3D',"<:3D:781696877346422805>"], ['4D',"<:4D:781696877640286248>"], ['JH',"<:JH:781696877766639636>"], ['2D',"<:2D:781696877547487254>"], ['JD',"<:JD:781696877728235540>"], ['KD',"<:KD:781697100752748555>"], ['4D',"<:4D:781696877640286248>"], ['3D',"<:3D:781696877346422805>"], ['5C',"<:5C:781696877610532894>"], ['CWAS',"<:CWAS:781696877489422339>"], ['3S',"<:3S:781696877565444096>"]]
#cards are K Q J 0 9 8 7 6 5 4 3 2 A
#suits are S H D C
#suitless cards are Jo (joker), CWAS (card without a suit).
#thus a 10 of spades is 0S, a king of diamonds is KD, a 9 of spades is 9S, etc.

current_deck = deck

player_id = 0

gameOpen = False
gameStarted = False
mao = None

class Game:
        def __init__(self, cards):
                global deck
                global player_id
                player_id = 0
                self.gamedeck = deck
                self.players = []
                self.discard_pile = []
                self.draw_pile = deck
                self.cards = cards
                self.isStarted = False

        def addPlayer(self, playerName, playerStrName, playerChannel):
                self.players.append(Player(playerName, playerStrName, playerChannel))

        def getPlayers(self):
                for p in self.players:
                        print(p.name + ", " + p.id)
                return

        def start(self):
                self.deal(self.cards)
                self.isStarted = True
                return

        def playerToDrawPile(self, pid, card):
                self.draw_pile.insert(0, card)
                self.players[pid].deck.remove(card)
                self.printGame()
                return

        def playerToDiscardPile(self, pid, card):
                self.discard_pile.insert(0, card)
                self.players[pid].deck.remove(card)
                self.printGame()
                return

        def drawPileToPlayer(self, pid):
                self.players[pid].deck.append(self.draw_pile[0])
                self.draw_pile.pop(0)
                self.printGame()
                return

        def discardPileToPlayer(self, pid):
                self.players[pid].deck.append(self.discard_pile[0])
                self.discard_pile.pop(0)
                self.printGame()
                return

        def deal(self, cards):
                random.shuffle(deck)
                for x in range(0, cards):
                        for n in self.players:
                                n.deck.append(self.draw_pile[0])
                                self.draw_pile.pop(0)
                self.printGame()
                self.discard_pile.insert(0,self.draw_pile[0])
                self.draw_pile.pop(0)
                return

        def reshuffle(self):
                for player in self.players:
                        player.deck.clear()
                self.draw_pile = deck
                self.deal(self.cards)
                return

        def refreshDrawPile(self):
            card_to_save = self.discard_pile[0]
            for card in self.discard_pile:
                self.draw_pile.append(card)
            self.discard_pile.clear()
            self.discard_pile.append(card_to_save)
            
        def printGame(self):
                print("Top card of draw pile:", self.draw_pile[0])
                if not len(self.discard_pile) == 0:
                        print("Top card of discard pile:", self.discard_pile[0])
                for n in self.players:
                        print(n.name, (card[0] for card in n.deck), n.id)
                print()
                return

        def getGameDebug(self):
                message = """"""
                message += "```\nMAO - "
                message += " players\n===\n```"
                message += "Top card of draw pile:"
                message += " "
                message += self.draw_pile[0]
                if not len(self.discard_pile) == 0:
                        message += "\nTop card of discard pile:"
                        message += self.discard_pile[0][1]
                for n in self.players:
                        message += "\n"
                        message += n.name
                        message += " "
                        for card in n.deck:
                                message += card[0] + " "
                        message += " "
                        message += str(n.id)
                        message += " "
                        message += "\n"
                return message

        def getGamePlayer(self, pid):
                message = """"""
                message += "```\nMAO"
                message += "\n===\n```"
                if not len(self.discard_pile) == 0:
                        message += "\nTop card of discard pile:"
                        message += self.discard_pile[0][1]
                        message += "\n"
                for n in self.players:
                        if n.id != pid:
                                message += "\n`"
                                message += n.strname
                                message += " > "
                                message += str(len(n.deck))
                                message += " cards`"
                message += "\n\n`Your Hand:`\n\n"
                for card in self.players[pid].deck:
                        message += card[1]
                        message += " "

                message += "\n```===```"

                return message

class Player:
        def __init__(self, name, strname, channel):
                global player_id
                self.name = name
                self.strname = strname
                self.id = player_id
                player_id += 1
                self.deck = []
                self.channel = channel

TOKEN = "NDk3Mzc0OTIwNjI0MzA4MjI3.DpfVbA.40ZyoKJA6_1IDNDKRXrwicjgwYw"

client = discord.Client()

@client.event
async def on_message(message):
        global gameStarted
        global gameOpen
        global mao

        #print the id
        senderid = message.author.id
        guild = message.guild

        # we do not want the bot to reply to itself
        if message.author == client.user:
                return

        elif message.author.id == 253541880229396482:
                stdin = message.content

                if ( stdin.startswith("!addplayer ") ) :
                        msg = stdin[11:].strip()
                        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False)}
                        player_channel = await guild.create_text_channel(message.mentions[0].name, overwrites = overwrites, slowmode_delay = 5)
                        await player_channel.set_permissions(message.mentions[0], read_messages = True)
                        await message.channel.send(msg)
                        given_name = message.mentions[0].name

                        new_msg = "hello and welcome to the game, {0.mention}".format(message.mentions[0])
                        await player_channel.send(new_msg)

                        mao.addPlayer(msg, message.mentions[0].name, player_channel)
                        return

                if ( stdin.strip() == "!addplayer" ) :
                        msg = "oops, please specify a playername: !addplayer <name>"
                        await message.channel.send(msg)
                        return

                if ( stdin.startswith("!start") ):
                        if gameOpen:
                                if not mao.isStarted:
                                        msg ="game started"
                                        gameStarted = True
                                        mao.start()
                                        gameOpen = False
                                        await message.channel.send(msg)
                                        for player in mao.players:
                                            await player.channel.send(mao.getGamePlayer(player.id))
                                        return

                                else:
                                        msg ="oops, there is currently a game of mao running!"
                                        await message.channel.send(msg)
                                        return

                        else:
                                msg = "oops, there isn't a game to start, please see !open"
                                await message.channel.send(msg)
                                return
                        
                if ( stdin.startswith("!open") ):
                        if not gameStarted:
                                if ( not stdin[6:].strip().isdigit() ):
                                        msg ="oops, please specify a number of cards: !open <#>"
                                        await message.channel.send(msg)
                                        return

                                elif ( int(stdin[6:].strip()) > 10 or int(stdin[6:].strip()) < 2):
                                        msg =  "oops, the number of cards must be between 2 and 10"
                                        await message.channel.send(msg)
                                        return
                                msg = "game opened with " + str(int(stdin[6:].strip())) + " cards, please input players with !addplayer <name>"
                                mao = Game(int(stdin[6:].strip()))
                                gameOpen = True
                                await message.channel.send(msg)
                                return

                        else:
                                msg = "oops, there is currently a game of mao running!"
                                await message.channel.send(msg)
                                return
                            
                if ( stdin.startswith("!reshuffle") ):
                        if gameStarted:
                                mao.reshuffle()
                                for player in mao.players:
                                    await player.channel.send("```asciidoc\n [ Deck reshuffled ]```")
                                

                if ( stdin.startswith("!refresh") ):
                        if gameStarted:
                                mao.refreshDrawPile()
                                for player in mao.players:
                                    await player.channel.send("```asciidoc\n [ Bottom of the discard pile shuffled back in ]```")

                if ( stdin.startswith("!endgame") ):
                        for player in mao.players:
                            await player.channel.send("```asciidoc\n[ Game has ended, closing in 5 seconds ]```")
                        time.sleep(5)
                        for player in mao.players:
                            await player.channel.delete()
                        mao = None
                        gameStarted = False
                        gameOpen = False


        if gameStarted:

                stdin = message.content
                        
                pid = 0
                
                stdinArr = []
                stdinParse = stdin.strip()
                stdinArr = stdinParse.split(" ")

                for player in mao.players:
                        authid = "<@!" + str(message.author.id) + ">"
                        if player.name == authid:
                                break
                        pid += 1

                ### Game Commands ###
                if stdinArr[0] == "!draw":
                        if len(mao.draw_pile) > 1:
                            mao.drawPileToPlayer(pid)
                            for player in mao.players:
                                await player.channel.send("``[ " + mao.players[pid].strname + " just drew from the draw pile. ]``")
                        else:
                            for player in mao.players:
                                await player.channel.send("```asciidoc\n [ Draw pile has only one card, please shuffle the discard pile back in ]```")

                elif stdinArr[0] == "!play":

                        cardconfirm = None


                        if len(stdinArr) == 1:
                            return
                    
                        cardtoplay = stdinArr[1].upper()

                        for card in mao.players[pid].deck:
                            if cardtoplay in card:
                                cardconfirm = card
                                break
                        if not cardconfirm == None:
                            mao.playerToDiscardPile(pid, cardconfirm)
                            for player in mao.players:
                                await player.channel.send("``[ " + mao.players[pid].strname + " just played ``" + card[1] + "`` to the discard pile. ]``")

                elif stdinArr[0] == "!penalty":

                        penalty_id = 0
                     
                        if len(stdinArr) == 1:
                            return

                        penalty_target = stdinArr[1]
                        
                        for player in mao.players:
                            testname = player.name.replace('!','')
                            penalty_target = penalty_target.replace('!','')
                            print("testname: " + testname)
                            print("target: " + penalty_target)
                                  
                            if testname == penalty_target:
                                print("found penalty target: " + str(penalty_id))
                                break
                            penalty_id += 1

                        mao.drawPileToPlayer(penalty_id)
                        for player in mao.players:
                            await player.channel.send("``[ " + mao.players[pid].strname + " just gave a penalty to " + mao.players[penalty_id].strname + ". ]``")

                elif stdinArr[0] == "!unplay":
                        for player in mao.players:
                            await player.channel.send("``[ " + mao.players[pid].strname + " just took ``" + mao.discard_pile[0][1] + "`` back from the discard pile. ]``")
                        mao.discardPileToPlayer(pid)


                elif stdinArr[0] == "!unpenalty":

                        cardconfirm = None

                        if len(stdinArr) == 1:
                            return
                    
                        cardtoplay = stdinArr[1].upper()

                        for card in mao.players[pid].deck:
                            if cardtoplay in card:
                                cardconfirm = card
                                break
                            
                        if not cardconfirm == None:
                            mao.playerToDrawPile(pid, cardconfirm)
                            for player in mao.players:
                                await player.channel.send("``[ " + mao.players[pid].strname + " just returned a card to the draw pile. ]``")

                        

                mao.printGame()

                for player in mao.players:
                        await player.channel.send(mao.getGamePlayer(player.id))





        #command prefix is ';'
        if message.content.startswith(";"):

        #very helpful help command
                if message.content.startswith(";help"):
                        msg = "The only command we can provide you is this one."
                        await message.channel.send(msg)

                elif message.content.startswith(";play"):
                        msg = "so you want to play a card eh"
                        await message.channel.send(msg)

                elif message.content.startswith(";game"):
                        msg = "printing the state of the game..."
                        await message.channel.send(mao.getGame())

                else:
                        msg = "yeah thats not a valid command"
                        await message.channel.send(msg)

        #penalizes for profanity
        if "damn" in message.content.lower() or "shit" in message.content.lower() or "wank" in message.content.lower() or "fuck" in message.content.lower() or "cock" in message.content.lower() or "dick" in message.content.lower() or "ass" in message.content.lower() or "cunt" in message.content.lower() or "bitch" in message.content.lower() or "pussy" in message.content.lower() or ("hell" in message.content.lower() and not "hello" in message.content.lower()) or ":middlefinger:" in message.content.lower():
                await message.channel.send("{}, penalty for profanity!".format(message.author.mention))
                await message.add_reaction("<:penalty:378398952296284161>")

        #penalizes for nazism
        if "nazi" in message.content.lower() or "heil" in message.content.lower() or "hail hitler" in message.content.lower():
                await message.channel.send("{}, penalty for naziism!".format(message.author.mention))
                await message.add_reaction("<:penalty:378398952296284161>")

        #penalizes for slurs
        if "gay" in message.content.lower() or "fag" in message.content.lower() or "nig" in message.content.lower():
                await message.channel.send("{}, penalty for profanity!".format(message.author.mention))
                await message.add_reaction("<:penalty:378398952296284161>")

        #original command that we use as a reference so that we don't screw anything up
        if message.content.startswith("!hello"):
                msg = "Hello {0.author.mention}".format(message)
                await message.channel.send(msg)


@client.event
async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print("------")

client.run("no")

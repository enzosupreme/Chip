import os
import discord
import random
import json
import requests
from imdb import Cinemagoer
from googlesearch import search
from keep_alive import keep_alive


ia = Cinemagoer()
client = discord.Client() #connection to discord

# ---- Data for Chat functions ------#

file = open("chat.json","r")
chatr = file.read()
file.close()
chat = json.loads(chatr)
greet = chat['g']
leave = chat['l']
gn    = chat['n']
morn  = chat['m']
ans   = chat['a']
genre = chat['gen']
decade= chat['dec']
jokes = chat['jokes']
cheery= chat['cheer']
f     = chat['food']
w     = chat['weapons']
wt    = chat['wt']
i     = chat['items']
armor = chat['Armor']
buff  = chat['Buff']
att = ''

#------------------------------------#

#------------IMDB--------------------#
FOTW = "https://www.imdb.com/title/tt0071315/?ref_=fn_al_tt_1"
movie = ('https://www.imdb.com/title/tt')
def mov():
  r = random.randint(0,1)
  roll = r
  stroll = str(roll)
  return stroll
def film():
  r = random.randint(0,9)
  roll = r
  stroll = str(roll)
  return stroll

def movie_id():
  a = mov()
  b = film()
  c = film()
  d = film()
  e = film()
  f = film()
  g = film()
  

  movieID = a + b + c + d + e + f + g

  return movieID

def imdb_name(name):
  celeb = ia.search_person(name)
  nid = celeb[0].personID
  return nid

def imdb_movie(movie):
  movies = ia.search_movie(movie)
  mid = movies[0].movieID
  return mid

#---------------QUOTE---------------#

def get_quote():
  response = requests.get("https://api.quotable.io/random")
  quote_data = response.json()
  #json_data = json.loads(quote_data)
  quote = quote_data['content'] + " \n-" + quote_data['author']
  return quote
  
#---------------JOKES---------------#
def get_joke():
  roll = random.randint(0,len(jokes))
  r = roll
  return r
  
#---------------FOOD----------------#
def hungry():
  food = random.randint(0,len(f))
  randf = f[food]
  return randf
def rando(min,max):
  roll = random.randint(min,max)
  r = roll
  return r

#---------------------------------------------------------------RPS-------------------------------------------------------#
def rock(s):
  if(s == 1):
    result = "Rock! \n\n It's a draw!"
    return result
  if(s == 2):
    result = "Paper! \n\n I Win!"
    return result
  if(s == 3):
    result = "Scissors! \n\n You Win!"
    return result
def paper(s):
  if(s == 1):
    result = "Rock! \n\n You Win!"
    return result
  if(s == 2):
    result = "Paper! \n\n It's a draw!"
    return result
  if(s == 3):
    result = "Scissors! \n\n I Win!"
    return result
def scissors(s):
  if(s == 1):
    result = "Rock! \n\n I Win!"
    return result
  if(s == 2):
    result = "Paper! \n\n You Win!"
    return result
  if(s == 3):
    result = "Scissors! \n\n It's a draw"
    return result
#------------------------------------------------------------LOOT---------------------------------------------------------#
def weapon(f,l):
  roll = random.randint(f,l)
  r = roll
  return w[r]

#----------------------------------------------------------Movie help----------------------------------------------------#
def decades():
  d = random.randint(0,9)
  dec = decade[d]
  return dec
  
def genres():
  g = random.randint(0,12)
  gen = genre[g]
  return gen
#----------------------------------------------------------chip chat-----------------------------------------------------#
def answer():
 
  a = random.randint(0,11)
  answer = ans[a]
  return answer
  
def greet_ing():
  size = 5
  roll = random.randint(0,size)
  r = roll

  greeting = greet[r]
  return greeting

def byeRoll():

  size = 6
  r = random.randint(0,size)
  byer = leave[r]
  return byer

def night():

  size = 5
  r = random.randint(0,size)
  goodnight = gn[r]
  return goodnight

def Morning():

  size = 4
  r = random.randint(0,size)
  goodmorn = morn[r]
  return goodmorn
def cheers():

  size = len(cheery)
  r = random.randint(0,size)
  c = cheery[r]
  return c

def Spam():
  
  spammer = ":laughing: "
  return spammer
  
def dice(num):
  roll = random.randint(1,num)
  return roll
def value(x):
  tot = x * 2.5
  tot += (tot % x)
  return tot
def level():
  roll = random.randint(1,20)
  return roll
def weight():
  roll = random.randint(5,40)
  r = roll
  return r

def weapon_roll():
  roll = rando(0,2)
  r = roll
  a = 0
  b = 0
  c = 0
  dt = 0
  if (r == 0):
    a = 0
    b = 5
    c = 0
  if (r == 1):
    a =6
    b = 12
    c = 1
  else:
    a = 13
    b = 23
    c = 2
  l = level()
  if (l < 6):
    dt = 4
  if (l > 5) and (l < 12):
    dt = 6
  if (l > 11) and (l < 16):
     dt = 10
  if (l > 15):
    dt = 20
  weap = weapon(a,b)
  wet = wt[c]
  worth = str(value(l))
  wait = str(weight())
  dr = str(dt)
  lvl = str(l)
  dic = rando(1,10)
      
  dicer = str(dic)
  damage = (dicer + " d" + dr)
  weapon_loot = "```\n Level " + lvl +  "\n" + weap + "\nDamage Type: " + wet + "\nWeight: " + wait + " lbs\n" + "Value: " + worth + "gp\n" + "Damage: " + damage + "\n ```"
  
  return weapon_loot
  
def item():
  roll = random.randint(0,(len(i)-1))
  r = roll

  item_roll = "```\n" + i[r] + "\n ```"

  return item_roll
  
def armor_roll():
  roll = random.randint(1,50)
  roll2 = random.randint(0,(len(armor) -1))
  roll3 = random.randint(0,(len(buff)-1))
  roll4 = random.randint(1,50)
  r = roll
  r2 = roll2
  r3 = roll3
  r4 = roll4
  st4 = str(r4)
  strr = str(r)

  arm = armor[r2]
  buf = buff[r3]
  wait = str(weight())

  result = "```\n" +buf + " " +  arm  + "\n+" + strr +" AC\n" + "+" + st4 + " " + buf + " Resistence\n" + "Weight: "+ wait + "lbs\n```"

  return result
  
  
 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  
  @client.event #register event
  async def on_message(message): #triggered when message is received.
    if message.author == client.user:
      return
    
    
    if message.content.startswith('!Rock') or message.content.startswith('!rock'):
      x = rando(1,3)
      rps = rock(x)
      await message.channel.send(rps)
    if message.content.startswith('!Paper') or message.content.startswith('!paper'):
      x = rando(1,3)
      rps = paper(x)
      await message.channel.send(rps)
    if message.content.startswith('!Scissors') or message.content.startswith('!scissors'):
      x = rando(1,3)
      rps = scissors(x)
      await message.channel.send(rps)

    if message.content.startswith('Search') or message.content.startswith('search'):
      msg = message.content
      query = msg.split("Search ",1)[0]
      for i in search(query, tld="com", num = 10, stop = 5, pause=1):
        await message.channel.send(i)
    if message.content.startswith('Why') and message.content.endswith('chip?'):
      msg = message.content
      query = msg.split("chip",1)[0]
      for i in search(query, tld="com", num = 10, stop = 5, pause=1):
        await message.channel.send(i)
    if message.content.startswith('why') and message.content.endswith('chip?'):
      msg = message.content
      query = msg.split("chip",1)[0]
      for i in search(query, tld="com", num = 10, stop = 5, pause=1):
        await message.channel.send(i)
    
        
    if message.content.startswith('What should I eat, chip') or message.content.startswith('what should I eat,chip'):
      hangry = hungry()
      await message.channel.send('You should eat ' + hangry)
  
    if message.content.startswith('What should I eat chip') or message.content.startswith('what should I eat chip'):
      hangry = hungry()
      await message.channel.send('You should eat ' + hangry)

      
   
  #------------------------------------------------GOODBYE----------------------------------------------------------#

    msg = message.content
    if message.content.startswith('Good bye chip') or message.content.startswith('good bye chip'):
      b = byeRoll()
      await message.channel.send(b)
    msg = message.content
    if message.content.startswith('bye chip') or message.content.startswith('Bye chip'):
      b = byeRoll()
      await message.channel.send(b)
    if message.content.startswith('Good morning chip') or message.content.startswith('Good Morning chip'):
      good = Morning()
      await message.channel.send(good)
    if message.content.startswith('good morning chip') or message.content.startswith('good morning, chip'):
      good = Morning()
      await message.channel.send(good)
    if message.content.startswith('Goodnight chip') or message.content.startswith('Good night chip'):
      goodn = night()
      await message.channel.send(goodn)
    if message.content.startswith('goodNight chip') or message.content.startswith('good night chip'):
      goodn = night()
      await message.channel.send(goodn)
    if message.content.startswith('GoodNight chip') or message.content.startswith('Good Night chip'):
      goodn = night()
      await message.channel.send(goodn)
    if message.content.startswith('goodnight chip'):
      goodn = night()
      await message.channel.send(goodn)

    if message.content.startswith('Thank you chip') or message.content.startswith('thank you chip'):
      await message.channel.send("You're Welcome")
    if message.content.startswith('Thank you, chip') or message.content.startswith('thank you, chip'):
      await message.channel.send("You're Welcome!")
    if message.content.startswith("thanks chip") or message.content.startswith("Thanks chip"):
      await message.channel.send("You're welcome!")
    if message.content.startswith("luck buff") or message.content.startswith("Luck buff"):
      r = rando(5,100)
      sr = str(r)
      await message.channel.send("Good Luck!")
      await message.channel.send("```\n You Received: \n+" + sr + " Luck \n ```")
    if message.content.startswith("wish me luck chip") or message.content.startswith('Wish me luck chip'):
      r = rando(5,100)
      sr = str(r)
      await message.channel.send("Good Luck!")
      await message.channel.send("```\n You Received: \n+" + sr + " Luck \n ```")
      

  #-------------------------------------------------HELLO-------------------------------------------------------------#

    
    if message.content.startswith('Hi chip') or message.content.startswith('hi chip'):
      g = greet_ing()
      await message.channel.send(g)
    if message.content.startswith('Hello chip') or message.content.startswith('hello chip'):
      g = greet_ing()
      await message.channel.send(g)
    if message.content.startswith('Howdy chip') or message.content.startswith('howdy chip'):
      g = greet_ing()
      await message.channel.send(g)
    if message.content.startswith('Hola chip') or message.content.startswith('hola chip'):
     g = greet_ing()
     await message.channel.send(g)
    if message.content.startswith('Hey chip') or message.content.startswith('hey chip'):
      g = greet_ing()
      await message.channel.send(g)
    if message.content.startswith('Whats up chip') or message.content.startswith('whats up chip'):
      g = greet_ing()
      await message.channel.send(g)
    if message.content.startswith('Sup chip') or message.content.startswith('sup'):
      g = greet_ing()
      await message.channel.send(g)
  #------------------------------------------------------DICE-------------------------------------------------------#
      
    if message.content.startswith('D20') or message.content.startswith('d20'):
      die = dice(20)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)
      if(die == 20):
        await message.channel.send('Nat TWENTY!!!')
    if message.content.startswith('D10') or message.content.startswith('d10'):
      die = dice(10)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)
    if message.content.startswith('D12') or message.content.startswith('d12'):
      die = dice(12)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)
    if message.content.startswith('D8') or message.content.startswith('d8'):
      die = dice(8)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)
    if message.content.startswith('D6') or message.content.startswith('d6'):
      die = dice(6)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)
    if message.content.startswith('D4') or message.content.startswith('d4'):
      die = dice(4)
      await message.channel.send('You rolled a: ')
      await message.channel.send(die)

    if message.content.startswith('Loot!'):
      roll = rando(0,2)
      r = roll
      response = ' '
      if (r == 0):
        response = weapon_roll()
      if (r == 1):
        response = item()
      if(r == 2):
        response = armor_roll()
      await message.channel.send("You open a chest and receive a.....")
      await message.channel.send(response)
      


    # -------------------------------------------------MOVIE -----------------------------------------------------------#
    if message.content.startswith('!Movie'):
      genrer = genres()
      await message.channel.send('You should watch a ')
      await message.channel.send(genrer + ' film')
      
    if message.content.startswith('What should I watch, chip') or message.content.startswith('what should I watch,chip'):
      film = movie + movie_id()
      await message.channel.send('You should watch  \n')
      await message.channel.send(film)
    if message.content.startswith('What should I watch chip') or message.content.startswith('what should I watch chip'):
      film = movie + movie_id()
      await message.channel.send('You should watch  \n')
      await message.channel.send(film)

    if message.content.startswith('!Celeb'):
      msg = message.content
      query = msg.split("Celeb",1)[1]
      ns = imdb_name(query)
      await message.channel.send('https://www.imdb.com/name/nm'+ ns)
      
    if message.content.startswith('!celeb'):
      msg = message.content
      query = msg.split("celeb",1)[1]
      ns = imdb_name(query)
      await message.channel.send('https://www.imdb.com/name/nm'+ ns)

    if message.content.startswith('!IMDB'):
      msg = message.content
      query = msg.split("!IMDB",1)[1]
      ms = imdb_movie(query)
      await message.channel.send('https://www.imdb.com/title/tt'+ ms)

    if message.content.startswith('!imdb'):
      msg = message.content
      query = msg.split("imdb",1)[1]
      ms = imdb_movie(query)
      await message.channel.send('https://www.imdb.com/title/tt'+ ms)
    if message.content.startswith('!imdb'):
      msg = message.content
      query = msg.split("imdb",1)[1]
      ms = imdb_movie(query)
      await message.channel.send('https://www.imdb.com/title/tt'+ ms)

    if message.content.startswith('FOTW') or message.content.startswith('fotw'):
      await message.channel.send("The film of the week is: \n" + FOTW)

    if message.content.startswith('Fotw'):
      await message.channel.send("The film of the week is: \n" + FOTW)
    
    #--------------------------------------------------YES OR NO -------------------------------------------------------#
    if message.content.startswith('Should') or message.content.startswith('should'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('will') and message.content.endswith('?'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('Will') and message.content.endswith('?'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('am') or message.content.startswith('Am'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('Is') or message.content.startswith('is'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('Are') or message.content.startswith('are'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('Do') and message.content.endswith('?'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('do') and message.content.endswith('?'):
      answers = answer()
      await message.channel.send(answers)
    if message.content.startswith('Does') or message.content.startswith('does'):
      answers = answer()
      await message.channel.send(answers)

    #-------------------------------------------------------INSPIRE-------------------------------------------------------#

    if message.content.startswith('Cheer me up chip') or message.content.startswith('cheer me up chip'):
      cmu = cheers()
      await message.channel.send(cmu)
    if message.content.startswith('Cheer me up, chip') or message.content.startswith('cheer me up, chip'):
      cmu = cheers()
      await message.channel.send(cmu)
    if message.content.startswith("I'm sad") or message.content.startswith('I am sad'):
      cmu = cheers()
      await message.channel.send(cmu)
    if message.content.startswith("I'm depressed") or message.content.startswith('I am depressed'):
      cmu = cheers()
      
      await message.channel.send(cmu)
      
   
   #---------------------------------------------------------JOKE-------------------------------------------------------# 

    if message.content.startswith('tell me a joke chip') or message.content.startswith('Tell me a joke chip'):
      r = get_joke()
      j = jokes[r]
      await message.channel.send(j)
    if message.content.startswith('Chip, who is your father') or message.content.startswith('chip, who is your father'):
      await message.channel.send('I was created in Circuit Bored Lab on 8/8/2022 \n by Shaun(enzosupreme)\n He is my father.')

    if message.content.startswith('Happy Two Weeks chip') or message.content.startswith('happy two weeks chip'):
      await message.channel.send(':partying_face: \n')
      await message.channel.send('Getting older and Wiser!')

    if message.content.startswith('What should I read chip?') or message.content.startswith('what should I read chip?'):
      await message.channel.send('The Lord of The Rings by J.R.R.Tolkien')


    #-------------------------------------------------------------------------------------------------------------------#

      
    if message.content.startswith('Thank you,chip') or message.content.startswith('thank you, chip'):
      await message.channel.send("You're Welcome!")
    """if message.content.startswith('$PAM'):
      s = Spam()
      for i in range(100):
        await message.channel.send(s)"""
      
    
      

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)


    

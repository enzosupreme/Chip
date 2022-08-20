import discord
import os
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
cheery = chat['cheer']

#------------------------------------#

#------------IMDB--------------------#
FOTW = "https://www.imdb.com/title/tt0088680/?ref_=fn_al_tt_1"
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
  #nate = nathan + ' \n' + nid
  return nid

def imdb_movie(movie):
  movies = ia.search_movie(movie)
  mid = movies[0].movieID
  #nate = nathan + ' \n' + nid
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
  
  
def rando(min,max):
  roll = random.randint(min,max)
  r = roll
  return r

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

def decades():
  d = random.randint(0,9)
  dec = decade[d]
  return dec
  
def genres():
  g = random.randint(0,12)
  gen = genre[g]
  return gen
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

  size = 7
  r = random.randint(0,size)
  c = cheery[r]
  return c

def Spam():
  
  spammer = ":laughing: "
  return spammer
  
def dice(num):
  roll = random.randint(1,num)
  return roll


 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  
  @client.event #register event
  async def on_message(message): #triggered when message is received.
    if message.author == client.user:
      return
    msg = message.content
    if message.content.startswith('Bye chip') or message.content.startswith('bye chip'):
      b = byeRoll()
      await message.channel.send(b)
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
      query = msg.split("Search ",1)[1]
      for i in search(query, tld="com", num = 10, stop = 5, pause=1):
        await message.channel.send(i)
  
      
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
  #------------------------------------------------GOODBYE----------------------------------------------------------#

      
    if message.content.startswith('Good morning chip') or message.content.startswith('Good Morning chip'):
      good = Morning()
      await message.channel.send(good)
    if message.content.startswith('good morning chip') or message.content.startswith('good morning, chip'):
      good = Morning()
      await message.channel.send(good)

    if message.content.startswith('Thank you chip') or message.content.startswith('thank you chip'):
      await message.channel.send("You're Welcome")
    if message.content.startswith('Thank you, chip') or message.content.startswith('thank you, chip'):
      await message.channel.send("You're Welcome!")
    if message.content.startswith("thanks chip") or message.content.startswith("Thanks chip"):
      await message.channel.send("You're welcome!")

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

    # -------------------------------------------------MOVIE -----------------------------------------------------------#
    if message.content.startswith('!Movie'):
      decader = decades()
      genrer = genres()
      mov = (decader + ' ' + genrer)
      await message.channel.send('You should watch a ')
      await message.channel.send(mov + ' Film')
      
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
    if message.content.startswith('Are') or message.content.startswith('a'):
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
    if message.content.startswith('Give me a quote, chip') or message.content.startswith('give me a quote, chip'):
      q = get_quote()
      await message.channel.send("```\n" + q + "\n```")
    if message.content.startswith('Give me a quote') or message.content.startswith('give me a quote'):
      q = get_quote()
      await message.channel.send("```\n" + q + "\n```")
  
   #---------------------------------------------------------JOKE-------------------------------------------------------# 

    if message.content.startswith('tell me a joke chip') or message.content.startswith('Tell me a joke chip'):
      r = get_joke()
      j = jokes[r]
      await message.channel.send(j)
    if message.content.startswith('Chip, who is your father') or message.content.startswith('chip, who is your father'):
      answers = answer()


    #-------------------------------------------------------------------------------------------------------------------#

      
      await message.channel.send('I was created in Circuit Bored Lab on 8/8/2022 \n by Shaun(enzosupreme)\n He is my father.')
    if message.content.startswith('Thank you,chip') or message.content.startswith('thank you, chip'):
      await message.channel.send("You're Welcome!")
    """if message.content.startswith('$PAM'):
      s = Spam()
      for i in range(100):
        await message.channel.send(s)"""
      
    
      

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
    

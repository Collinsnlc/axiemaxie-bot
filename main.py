import discord
import os
import requests
import json
import random




client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

@client.event
async def on_message(message):
  if message.content == "?help":
        embed = discord.Embed(title="Bot commands", description="Some useful commands")
        embed.add_field(name="?scholarship", value="Scholarship info (english)")
        embed.add_field(name="?ph scholarship", value="Scholarship info (filipino)")
        embed.add_field(name="?sp scholarship", value="Scholarship info (spanish)")
        embed.add_field(name="?social media", value="Paladin Digital social media")
        embed.add_field(name="?event", value="Lists the current event")
        embed.add_field(name="?secret", value="Axie maxies secret commands")
        await message.channel.send(content=None, embed=embed)


  
  


  myList = ["https://imgur.com/a/Vx8Qqtw", "https://imgur.com/a/OVGuFKd", "https://imgur.com/a/ZecBRzv","https://imgur.com/a/F4SEncd", "https://imgur.com/a/iQzTnJd", "https://imgur.com/a/OgqLGyk", "https://imgur.com/a/qLlXOmy", "https://imgur.com/a/onuhFVr", "https://imgur.com/a/shXPgfx"]

  if message.content.startswith('?hashira me'):
    await message.channel.send(random.choice(myList))

  thanos = ["You Died", "You Lived"]

  if message.content.startswith('-thanos snap-'):
    await message.channel.send(random.choice(thanos))
  
  if message.content.startswith('?ban'):
    await message.channel.send("this user has been banned")

  Demonwaifu = ["https://imgur.com/rBOwwdN", "https://imgur.com/K91fqiO",  "https://imgur.com/OXw9jYn", "https://imgur.com/j2Qr4H8", "https://imgur.com/dsVXIih", "https://imgur.com/MU4OzIR", "https://imgur.com/78Bex0W", "https://imgur.com/kRaXzDR", "https://imgur.com/3X2YFA7", "https://imgur.com/2MV59jR", "https://imgur.com/bsoY5jU", "https://imgur.com/XKlps6C", "https://imgur.com/DHfFwyf", "https://imgur.com/1zwmvm6", "https://imgur.com/fyGlJlt", "https://imgur.com/qzRDGrZ", "https://imgur.com/lJLQQXf", "https://imgur.com/kvB8fVh", "https://imgur.com/ryVph3r", "https://imgur.com/DmomXrv", "https://imgur.com/Om5WPil", "https://imgur.com/DdpNovv"]

  if message.content.startswith('?ds waifu'):
    await message.channel.send(random.choice(Demonwaifu))

  
  myListgenshin = ["https://imgur.com/uFXMNZ7", "https://imgur.com/mKADDnh", "https://imgur.com/VK2yBpB", "https://imgur.com/ed7Ow5V", "https://imgur.com/AkHTjwi", "https://imgur.com/FsJ4qyC", "https://imgur.com/EIwRU94", "https://imgur.com/KFMm4K7", "https://imgur.com/YWnQTcQ", "https://imgur.com/TdROGAb", "https://imgur.com/3WHWXS0", "https://imgur.com/XeLaBMo", "https://imgur.com/tgKc4dy", "https://imgur.com/Uc1seDy", "https://imgur.com/sibxa3x", "https://imgur.com/FiVmJLk", "https://imgur.com/vTc3kTb", "https://imgur.com/rLdqrha", "https://imgur.com/EVDu4nY", "https://imgur.com/hOxgiGV", "https://imgur.com/CsAnycz", "https://imgur.com/RWQSxVu", "https://imgur.com/3s8IB4t", "https://imgur.com/YC9OwLt", "https://imgur.com/DFLQ2RH", "https://imgur.com/SDr5HUN", "https://imgur.com/Ry2K5KA", "hhttps://imgur.com/AABnHqq", "https://imgur.com/J4MiWLN", "https://imgur.com/l3f7nQn", "https://imgur.com/aKmr5e4", "https://imgur.com/PnjoZX9", "https://imgur.com/57RwAD9", "https://imgur.com/75Lkbbg", "https://imgur.com/6GliRSB", "https://imgur.com/FxmMA1X", "https://imgur.com/mAbyh9o", "https://imgur.com/8dweVtz"]


  if message.content.startswith('?genshin waifu'):
    await message.channel.send(random.choice(myListgenshin))

  #info
  if message.content.startswith('?scholarship'):
    await message.channel.send("Hello first of all welcome to PDG :D, there are many types of scholarships here. the first one is temporary 1 week long pegaxy scholarships these can be obtained in 2 ways if you are part of the 'legendary paladin' role there is a weekly raffle for you and also there is another weekly raffle for everyone in the server both are twenty percent. Permanent scholarships are given out 2 times a month for active server members and through events. We want our permanent scholars to be active in helping us build our community.")

    
  if message.content.startswith('?social media'):
    await message.channel.send("https://twitter.com/Paladindigitalx https://www.youtube.com/channel/UCk_lGqzuppdAO5LK_53fhZw")

  if message.content.startswith('?ph scholarship'):
    await message.channel.send("Kamusta? Una sa lahat, ikinagagalak naming kayong makita dito sa Paladin Digital Guild! Maraming klase ng ‘scholarships’ na pwedeng ialok ang aming guild 1. Ang unang klase ay yung tinatawag na ‘Temporary 1 Week Long Pegaxy Scholarship’ at ito ay maaaring makuha sa pamamahitan ng dalawang paraan:A.) Una ay kung ikaw ay kabilang sa ‘Legendary Paladin’ na role, meron tayong ‘weekly raffle’ B.) Meron ding ‘weekly raffle’ para sa lahat ng kabilang sa server(pero hindi na kasali yung mga may pega na siyempre) at yung ‘temporary 1 week long pegaxy scholarship’ ay may 20% na hatian. 2. Para sa pangalawang paraan, namimili kami ng dalawang isko dalawang beses sa isang buwan base sa kung gaano sila kaaktibo dito sa server at siyempre, meron ding mga events. Gusto namin na maging aktibo ang mga permanent scholars para mas maitaguyod pa ang guild na ito.")


  if message.content.startswith('?sp scholarship'):
    await message.channel.send("Hola, antes que nada, bienvenido a PDG: D, hay muchos tipos de becas aquí. la primera es una beca pegaxy temporal de 1 semana de duración, se puede obtener de 2 maneras si eres parte del rol de 'paladín legendario' hay una rifa semanal para ti y también hay otra rifa semanal para todos en el servidor ambos son veinte por ciento. Las becas permanentes se otorgan 2 veces al mes para miembros activos del servidor y a través de eventos. Queremos que nuestros becarios permanentes sean activos para ayudarnos a construir nuestra comunidad.")


  if message.content.startswith('?event'):
    await message.channel.send("sorry there are no events right now Q.Q")

  if message.content.startswith('?secret'):
    await message.channel.send(" bwaha you found my secret commands please note the commands are case sensitive:\ncan i refer someone? \naxie maxie is he doing bad? \naxie maxie tell me a joke \naxie maxie how do you get a watermellon pregnant? \naxie maxie nasan si marites? \nhow long till payday? \nhow long has shoto slept in voice chat? \naxie maxie do you think im cute? \ngood morning axie maxie \ncan the ronin manager? \naxie maxie am i cute? \ni love this bot \nima kill this bot \n-stab axie maxie- \n -thanos snap- \n?hashira me \n?ds waifu \n?genshin waifu")

  


  #rps
  if message.content.startswith('!rps'):
    await message.channel.send("https://imgur.com/qatDDLU")

  
  #rps
  if message.content.startswith('⎅⏃⋏☊⟒ ⎎⍜⍀ ⋔⟒ ⊬⍜⎍ ⌇⟒⌖⊬ ⏃⌰⟟⟒⋏ ⋔⏃⋔⏃'):
    await message.channel.send("https://media.giphy.com/media/1xG52NA07e7KbqQMSS/giphy.gif")


  

  #slp guide
  if message.content.startswith('!slpguide'):
    await message.channel.send("https://imgur.com/XG2Ip2e")
  
  if message.content.startswith("Banal na baka"):
    await message.channel.send("You dare summon me?" + "https://imgur.com/a/kzC0pgI")
  
  if message.content.startswith("Where is Neal?"):
    await message.channel.send("He left earth to live on mars, bwahaha have fun staying on earth noob")

  #expguide
  if message.content.startswith('!expguide'):
    await message.channel.send("https://imgur.com/YUkbko1")

  #mmrslpguide
  if message.content.startswith('!mmrslp'):
    await message.channel.send('https://imgur.com/a/IgEGWiB')


  #scholarstatspage

  if message.content.startswith('$nealstats'):
    await message.channel.send("https://tracker.axie.management/ronin:49ae92228644a371dffc1a9142082187d472d371")
  
  if message.content.startswith('$lukastats'):
    await message.channel.send("https://tracker.axie.management/ronin:6bd85c781b17f8e1e9962d7acac1c807af97c8e3")

  if message.content.startswith('$miguelstats'):
    await message.channel.send("https://tracker.axie.management/ronin:ab9c706b9541b5699951f2d57ea5abbf870428d1")
  
  if message.content.startswith('$felixstats'):
    await message.channel.send("https://tracker.axie.management/ronin:38d64d12a09054493fd791ae6e4f8b0d3cec2b41")

  if message.content.startswith('$squidwardstats'):
    await message.channel.send("https://tracker.axie.management/ronin:ae04ccb54cb0cc8de06d91622107c9273edb4dc5")

  if message.content.startswith('$alienstats'):
    await message.channel.send("https://tracker.axie.management/ronin:1b2c6ce2fe7b1251572b36f62c5104f7a2d9ccdd")

  if message.content.startswith('$raccoonstats'):
    await message.channel.send("https://tracker.axie.management/ronin:448138203ee0b943c85272e0f4488a257940e82e")

  if message.content.startswith('$csingstats'):
    await message.channel.send("https://tracker.axie.management/ronin:a7055760327593a9f4c640bc0362cdb8bea5b39e")

  if message.content.startswith('$aiyastats'):
    await message.channel.send("https://tracker.axie.management/ronin:5665ce8492963f52d223b2cc39cac58dd44c4adc")

  if message.content.startswith('$ishidastats'):
    await message.channel.send("https://tracker.axie.management/ronin:5e7d73fdf72f8f3731ab72c47a93761d0afbe158")

  if message.content.startswith('$lopezstats'):
    await message.channel.send("https://tracker.axie.management/ronin:bbc0d30ab92a9160ed937eb5181666739caff7a1")

  if message.content.startswith('$benjistats'):
    await message.channel.send("https://tracker.axie.management/ronin:3d7cd12cbd5e9c7c56321802c847026ddc373404")

  if message.content.startswith('$elluhstats'):
    await message.channel.send("https://tracker.axie.management/ronin:31ccbf99fd7ad69c65a4696cb11c194427bd1a29")

  if message.content.startswith('$paegestats'):
    await message.channel.send("https://tracker.axie.management/ronin:8165a451c3dcfb150040429b29cf178c849abb73")

  if message.content.startswith('$nairobistats'):
    await message.channel.send("https://tracker.axie.management/ronin:c09fe1e85a1613e8da31a4a0a2a1910abc9601e5")

  if message.content.startswith('$alesonstats'):
    await message.channel.send("https://tracker.axie.management/ronin:097da15cbddb612af29b5e7870d723fcba2dd2f4")

  if message.content.startswith('$leestats'):
    await message.channel.send("https://tracker.axie.management/ronin:162b9698a5cd23b22ad33683a7c7e5a78a49e093")

  if message.content.startswith('$aaaAaaAstats'):
    await message.channel.send("https://tracker.axie.management/ronin:b6c5411c5a15863e4e5b2d61ac5f9144498434f7")

  if message.content.startswith('$ierstats'):
    await message.channel.send("https://tracker.axie.management/ronin:8c9c2b112c85ae3626115bfa55e163027fec1b64")

  if message.content.startswith('$pogistats'):
    await message.channel.send("https://tracker.axie.management/ronin:cda4ae99c27294716d424f208532ac22a7a60719")

  if message.content.startswith('$aicesstats'):
    await message.channel.send("https://tracker.axie.management/ronin:8677dc33129557d48465e5585593f0d56c21f975")

  if message.content.startswith('$aeonstats'):
    await message.channel.send("https://tracker.axie.management/ronin:904a76827ddc8f45926e686af29fdac50a783335")

  if message.content.startswith('$lynstats'):
    await message.channel.send("https://tracker.axie.management/ronin:8f208b8f1ac99564d9b28801eeea4c52b9856a40")

  if message.content.startswith('$daengstats'):
    await message.channel.send("https://tracker.axie.management/ronin:4ef5607ada10b8aa401515e3c1dea8c5b5a8c1d1")

  if message.content.startswith('$jamilstats'):
    await message.channel.send("https://tracker.axie.management/ronin:55a4e9ead58da2f87a9dad706b501b0a923588cb")

  if message.content.startswith('$shotostats'):
    await message.channel.send("https://tracker.axie.management/ronin:6835129e36929d4ba6a6f30131200b935b040eed")

  if message.content.startswith('$blankostats'):
    await message.channel.send("https://tracker.axie.management/ronin:4b021c7e8f309a51bbfa0c03c636190f92a87e7b")

  if message.content.startswith('$francesstats'):
    await message.channel.send("https://tracker.axie.management/ronin:1eb2ad8e50b76b717c83882a98d08b0949344b54")

  if message.content.startswith('$tootsstats'):
    await message.channel.send("https://tracker.axie.management/ronin:d470391361afbfce81e9c81c8060434af94a9635")

  if message.content.startswith('$reginastats'):
    await message.channel.send("https://tracker.axie.management/ronin:1bca51ec418ddb7d98d5bf1a138c51b8dc8ae42d")

  if message.content.startswith('$markrysstats'):
    await message.channel.send("https://tracker.axie.management/ronin:b8b01679501b2b499dd708a7d62dbd490282a201")

  if message.content.startswith('$lindsaystats'):
    await message.channel.send("https://tracker.axie.management/ronin:f0f2df4c7a6fab8b6970acfbdce801281ef4150b")

  if message.content.startswith('$peanutstats'):
    await message.channel.send("https://tracker.axie.management/ronin:be7c0aecfb2453bafaa697054384464d90b057bf")

  if message.content.startswith('$sunayorustats'):
    await message.channel.send("https://tracker.axie.management/ronin:fd2f823a5a42477f0cb03fb98f8d063c2214aab3")

  if message.content.startswith('$mhiemhiestats'):
    await message.channel.send("https://tracker.axie.management/ronin:55e9552607faf3b7ac0a941357a131f8e4219298")

  if message.content.startswith('$arimastats'):
    await message.channel.send("https://tracker.axie.management/ronin:9337d0ce171ca57d5648de1e1ca1477b520e4383")

  if message.content.startswith('$chuayacostats'):
    await message.channel.send("https://tracker.axie.management/ronin:66c66e30fbfd7417da5a799f6afc2909ea7a22d3")

  if message.content.startswith('$joeystats'):
    await message.channel.send("https://tracker.axie.management/ronin:8e63d8e791dafc035ae610db09778f42be8e1557")
    
  if message.content.startswith('$unchainedstats'):
    await message.channel.send("https://tracker.axie.management/ronin:d1f9bb6045d0e6f7252d080f4b453436197084ef")

  if message.content.startswith('when upgrade?'):
    await message.channel.send("Wait lang")

  if message.content.startswith('$unchainedstats'):
    await message.channel.send("https://tracker.axie.management/ronin:d1f9bb6045d0e6f7252d080f4b453436197084ef")

  if message.content.startswith('$harvsstats'):
    await message.channel.send("https://tracker.axie.management/ronin:1bbe6052704750e16539051334ff49952942a24d")

  if message.content.startswith('$larstats'):
    await message.channel.send("https://tracker.axie.management/ronin:c58a00e7a7a681b9438d8d75d5fc1a1c310e693c")



    

  #secret commands

  drink = ["wine","beer","coffee","water","hot chocolate", "soda","tea"]
  if message.content.startswith('axie maxie give me a drink'):
    await message.channel.send("here you go a nice " + random.choice(drink))

  if message.content.startswith('can i refer someone?'):
    await message.channel.send("Wait lang")

  if message.content.startswith('axie maxie is he doing bad?'):
    await message.channel.send("yeah hes a noob")

  if message.content.startswith('axie maxie tell me a joke'):
    await message.channel.send("your mmr")

  if message.content.startswith('axie maxie how do you get a watermellon pregnant?'):
    await message.channel.send("you pakwan XD")

  if message.content.startswith('axie maxie nasan si marites?'):
    await message.channel.send("nasa puso mo")

  if message.content.startswith('how long till payday?'):
    await message.channel.send("Wait lang")
     
  if message.content.startswith('how long has shoto slept in voice chat?'):
    await message.channel.send("1 year 150 days 18 hours and 26 seconds")

  if message.content.startswith('axie maxie do you think im cute?'):
    await message.channel.send("ew no humans are gross, i only date other axies")
  
  if message.content.startswith('good morning axie maxie'):
    await message.channel.send("magandang umaga! ^3^ have a good day")
    
  if message.content.startswith('can the ronin manager?'):
    await message.channel.send("your fired")
  
  if message.content.startswith('axie maxie am i cute?'):
    await message.channel.send("yes of course senpai")
  
  if message.content.startswith('i love this bot'):
    await message.channel.send("https://imgur.com/a/6nrMVAV")

  if message.content.startswith('ima kill this bot'):
    await message.channel.send("NOOOO PLEASE NOOO I HAVE A FAMILYYY")
  
  if message.content.startswith("-stab axie maxie-"):
    await message.channel.send("-falls to the floor and lets out one last gasp crying for help")

  if message.content.startswith("ang pangit talaga ni axie maxie"):
    await message.channel.send("Pakyu putangina mo D:<")




client.run('ODc4NDMzMTMwMjcxMzcxMjc0.YSBGmg.C2l-j-TYMNuJ0RXUXNYw-CmLDDA')
  

  

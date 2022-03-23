@bot.command()
async def embed(ctx):
  def check(m):
    return m.author.id == ctx.author.id
  await ctx.channel.send("**Are you sure in creating an embed ? (Yes/No)**")
  val = await bot.wait_for('message', check=check)

  if val.content == 'No':
    await ctx.channel.send("**You really want to waste my time do you !!! 😑**")

  elif val.content == 'Yes':
    
    
   await ctx.channel.send("**What's the title of your custom embed ?**")
   title = await bot.wait_for('message', check=check)
   await ctx.channel.send("**What's the icon_url of the above author ?**")
   title_url = await bot.wait_for('message', check=check)
   await ctx.channel.send("**What's the url of the image of the embed ?**")
   image_url = await bot.wait_for('message', check=check)
   await ctx.channel.send("**What's the url of the thumbnail of the embed ?**")
   thumbnail_url = await bot.wait_for('message', check=check)
   await ctx.channel.send("**What's the footer text of your custom embed ?**")
   footer = await bot.wait_for('message', check=check)
   await ctx.channel.send("**What's the icon_url of the above footer ?**")
   footer_url = await bot.wait_for('message', check=check)
   await ctx.channel.send('**How many field lines you want in your embed ?**')
   field_no = await bot.wait_for('message', check=check) 

    
   if (field_no.content == '5') :
     await ctx.channel.send("**What is the field_1 title ?**")
     f1_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_1 description ?**")
     f1_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 title ?**")
     f2_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 description ?**")
     f2_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 title ?**")
     f3_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 description ?**")
     f3_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_4 title ?**")
     f4_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_4 description ?**")
     f4_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_5 title ?**")
     f5_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_5 description ?**")
     f5_desc = await bot.wait_for('message', check=check)
  
     embed = discord.Embed(colour=0xFFFFFF)
     embed.set_author(name = title.content, icon_url = title_url.content)
     embed.set_footer(text = footer.content, icon_url = footer_url.content)
     embed.set_image(url = image_url.content)
     embed.set_thumbnail(url = thumbnail_url.content)
     embed.add_field(name = f1_title.content, value = f1_desc.content, inline = False)
     embed.add_field(name = f2_title.content, value = f2_desc.content, inline = False)
     embed.add_field(name = f3_title.content, value = f3_desc.content, inline = False)
     embed.add_field(name = f4_title.content, value = f4_desc.content, inline = False)
     embed.add_field(name = f5_title.content, value = f5_desc.content, inline = False)

     await ctx.channel.purge(limit = 38)
     await ctx.channel.send("**CREATING EMBED .... ⌛ **")
     await asyncio.sleep(3)
     await ctx.channel.send("**EMBED CREATED ✅  **")
     await asyncio.sleep(1)
     await ctx.channel.send(embed=embed)


   elif (field_no.content == '4') : 
     
     await ctx.channel.send("**What is the field_1 title ?**")
     f1_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_1 description ?**")
     f1_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 title ?**")
     f2_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 description ?**")
     f2_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 title ?**")
     f3_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 description ?**")
     f3_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_4 title ?**")
     f4_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_4 description ?**")
     f4_desc = await bot.wait_for('message', check=check)

     embed = discord.Embed(colour=0xFFFFFF)
     embed.set_author(name = title.content, icon_url = title_url.content)
     embed.set_footer(text = footer.content, icon_url = footer_url.content)
     embed.set_image(url = image_url.content)
     embed.set_thumbnail(url = thumbnail_url.content)
     embed.add_field(name = f1_title.content, value = f1_desc.content, inline = False)
     embed.add_field(name = f2_title.content, value = f2_desc.content, inline = False)
     embed.add_field(name = f3_title.content, value = f3_desc.content, inline = False)
     embed.add_field(name = f4_title.content, value = f4_desc.content, inline = False)

     await ctx.channel.purge(limit = 34)
     await ctx.channel.send("**CREATING EMBED .... ⌛ **")
     await asyncio.sleep(3)
     await ctx.channel.send("**EMBED CREATED ✅  **")
     await asyncio.sleep(1)
     await ctx.channel.send(embed=embed)


   elif (field_no.content == '3') :
     await ctx.channel.send("**What is the field_1 title ?**")
     f1_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_1 description ?**")
     f1_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 title ?**")
     f2_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 description ?**")
     f2_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 title ?**")
     f3_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_3 description ?**")
     f3_desc = await bot.wait_for('message', check=check)

     embed = discord.Embed(colour=0xFFFFFF)
     embed.set_author(name = title.content, icon_url = title_url.content)
     embed.set_footer(text = footer.content, icon_url = footer_url.content)
     embed.set_image(url = image_url.content)
     embed.set_thumbnail(url = thumbnail_url.content)
     embed.add_field(name = f1_title.content, value = f1_desc.content, inline = False)
     embed.add_field(name = f2_title.content, value = f2_desc.content, inline = False)
     embed.add_field(name = f3_title.content, value = f3_desc.content, inline = False)

     await ctx.channel.purge(limit = 30 )
     await ctx.channel.send("**CREATING EMBED .... ⌛ **")
     await asyncio.sleep(3) 
     await ctx.channel.send("**EMBED CREATED ✅  **")
     await asyncio.sleep(1)
     await ctx.channel.send(embed=embed)

      

   elif (field_no.content == '2') : 
     await ctx.channel.send("**What is the field_1 title ?**")
     f1_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_1 description ?**")
     f1_desc = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 title ?**")
     f2_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_2 description ?**")
     f2_desc = await bot.wait_for('message', check=check)

     embed = discord.Embed(colour=0xFFFFFF)
     embed.set_author(name = title.content, icon_url = title_url.content)
     embed.set_footer(text = footer.content, icon_url = footer_url.content)
     embed.set_image(url = image_url.content)
     embed.set_thumbnail(url = thumbnail_url.content)
     embed.add_field(name = f1_title.content, value = f1_desc.content, inline = False)
     embed.add_field(name = f2_title.content, value = f2_desc.content, inline = False)

     await ctx.channel.purge(limit = 26)
     await ctx.channel.send("**CREATING EMBED .... ⌛ **")
     await asyncio.sleep(3)
     await ctx.channel.send("**EMBED CREATED ✅  **")
     await asyncio.sleep(1)
     await ctx.channel.send(embed=embed)

   

   elif (field_no.content == '1') : 
     await ctx.channel.send("**What is the field_1 title ?**")
     f1_title = await bot.wait_for('message', check=check)
     await ctx.channel.send("**What is the field_1 description ?**")
     f1_desc = await bot.wait_for('message', check=check)

     embed = discord.Embed(colour=0xFFFFFF)
     embed.set_author(name = title.content, icon_url = title_url.content)
     embed.set_footer(text = footer.content, icon_url = footer_url.content)
     embed.set_image(url = image_url.content)
     embed.set_thumbnail(url = thumbnail_url.content)
     embed.add_field(name = f1_title.content, value = f1_desc.content, inline = False)

     await ctx.channel.purge(limit = 22)
     await ctx.channel.send("**CREATING EMBED .... ⌛ **")
     await asyncio.sleep(3)
     await ctx.channel.send("**EMBED CREATED ✅  **")
     await asyncio.sleep(2)
     await ctx.channel.send(embed=embed)
    
    
   else:
     await ctx.channel.send("**⚠️ ERROR , Make sure the no of fields dont exceed five or dont go in Negatives . Make sure you give an integral value for the question number of fields **")
       
    

  else :
    await ctx.channel.send("**The reply should be in Yes or No Dumbo !! 😶**")

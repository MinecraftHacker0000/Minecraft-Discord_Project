import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def Bot creater(ctx):
    await ctx.send('wow!')

@client.event
async def on_ready():
    
    print('ログインしました')
    
   @client.event
async def on_message(message):
    if client.user in message.mentions: 
        reply = f'{message.author.mention} 誰？'
        await message.channel.send(reply) 
        
        @client.event
async def on_message(message):
    
    if message.content == '/members':
        print(message.guild.members)
    
    if message.content == '/roles':
        print(message.guild.roles)
    
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    
    if message.content == '/category_channels':
        print(message.guild.categories)
        
bot.run(token)

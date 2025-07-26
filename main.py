import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='+', intents=intents)

ALLOWED_ROLE_ID = 1391811944721289298

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def come(ctx, member: discord.Member, *, reason: str = "لا يوجد سبب"):
    author = ctx.author

    # Check for Administrator or specific role
    has_permission = author.guild_permissions.administrator or any(role.id == ALLOWED_ROLE_ID for role in author.roles)

    if not has_permission:
        await ctx.send("❌ لا تملك صلاحية استخدام هذا الأمر.")
        return

    try:
        await member.send(
            f"تم إستدعاؤك الى {ctx.channel.mention}\n**Reason:** {reason}"
        )
        await ctx.send(f"📨 تم إرسال دعوة إلى {member.mention}.")
    except discord.Forbidden:
        await ctx.send("❌ لا يمكنني إرسال رسالة خاصة لهذا المستخدم.")

# Run the bot
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
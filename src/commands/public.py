from discord import PermissionOverwrite, utils
from discord.ext import commands
from discord.ext.commands import has_permissions


def set_permissions():
	perms = PermissionOverwrite()
	perms.connect = False
	return perms


class PublicVocalCommand( commands.Cog ):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name= 'public')
	@has_permissions(manage_channels=True, manage_roles=True, connect=True)
	async def make_public_vocal(self, ctx):
		vocal_channel = ctx.author.voice

		if vocal_channel is not None:
			vocal_channel = ctx.author.voice.channel
			excludes_channel = [self.bot.ids[ctx.author.guild.id]["id_vocal_channel_inactive"], self.bot.ids[ctx.author.guild.id]["id_vocal_channel_create"]]

			if vocal_channel.id not in excludes_channel:
				everyone = utils.get(ctx.author.guild.roles, id= self.bot.ids[ctx.author.guild.id]["id_role_everyone"])

				await vocal_channel.set_permissions(everyone, overwrite= set_permissions())

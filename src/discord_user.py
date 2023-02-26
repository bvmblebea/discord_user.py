import requests
from time import time

class DiscordUser:
	def __init__(self) -> None:
		self.api = "https://discord.com/api/v9"
		self.headers = {
			"content-type": "application/json",
			"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
		}
		
	def login(
			self,
			login: str,
			password: str,
			login_source: str = None,
			gift_code_sku_id: str = None) -> dict:
		data = {
			"login": login,
			"password": password,
			"undelete": False,
			"captcha_key": None,
			"login_source": login_source,
			"gift_code_sku_id": gift_code_sku_id
		}
		response = requests.post(
			f"{self.api}/auth/login",
			json=data,
			headers=self.headers).json()
		if "token" in response:
			self.token = response["token"]
			self.headers["authorization"] = self.token
		return response

	def affinities_users(self) -> dict:
		return requests.get(
			f"{self.api}/users/@me/affinities/users",
			headers=self.headers).json()

	def get_guilds(self) -> dict:
		return requests.get(
			f"{self.api}/users/@me/guilds",
			headers=self.headers).json()

	def get_guild_info(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}",
			headers=self.headers).json()

	def get_guild_channels(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}/channels",
			headers=self.headers).json()
	
	def get_account_channels(self) -> dict:
		return requests.get(
			f"{self.api}/users/@me/channels",
			headers=self.headers).json()

	def leave_guild(self, guild_id: int) -> dict:
		return requests.delete(
			f"{self.api}/users/@me/guilds/{guild_id}",
			headers=self.headers).json()

	def leave_channel(self, channel_id: int) -> dict:
		return requests.delete(
			f"{self.api}/users/@me/channels/{channel_id}",
			headers=self.headers).json()

	def discoverable_guilds(
			self,
			offset: int = 0,
			limit: int = 24) -> dict:
		return requests.get(
			f"{self.api}/discoverable-guilds?offset={offset}&limit={limit}",
			headers=self.headers).json()

	def get_relationships(self) -> dict:
		return requests.get(
			f"{self.api}/users/@me/relationships",
			headers=self.headers).json()

	def get_user_info(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/users/{user_id}/profile",
			headers=self.headers).json()

	def delete_friend(self, user_id: int) -> dict:
		return requests.delete(
			f"{self.api}/users/@me/relationships/{user_id}",
			headers=self.headers).json()

	def typing_active(self, channel_id: int) -> dict:
		return requests.get(
			f"{self.api}/channels/{channel_id}/typing",
			headers=self.headers).json()

	def change_username(
			self,
			password: str,
			username: str) -> dict:
		data = {
			"password": password,
			"username": username
		}
		return requests.patch(
			f"{self.api}/users/@me",
			json=data,
			headers=self.headers).json()

	def change_status(
			self,
			emoji_name: str = None,
			text: str = None) -> dict:
		data = {
			"custom_status": {
				"emoji_name": emoji_name,
				"text": text
			}
		}
		return requests.patch(
			f"{self.api}/users/@me/settings",
			json=data,
			headers=self.headers).json()

	def send_message(
			self,
			content: str,
			channel_id: int) -> dict:
		data = {
			"content": content
		}
		return requests.post(
			f"{self.api}/channels/{channel_id}/messages",
			json=data,
			headers=self.headers).json()

	def delete_message(
			self,
			message_id: int,
			channel_id: int) -> dict:
		return requests.delete(
			f"{self.api}/channels/{channel_id}/messages/{message_id}",
			headers=self.headers).json()

	def get_channel_messages(
			self,
			channel_id: int,
			limit: int = 100) -> dict:
		return requests.get(
			f"{self.api}/channels/{channel_id}/messages?limit={limit}",
			headers=self.headers).json()

	def get_voice_regions(self) -> dict:
		return requests.get(
			f"{self.api}/voice/regions",
			headers=self.headers).text

	def get_guild_bans(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}/bans",
			headers=self.headers).json()

	def get_guild_users(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}/members",
			headers=self.headers).json()

	def delete_channel(self, channel_id: int) -> dict:
		return requests.delete(
			f"{self.api}/channels/{channel_id}",
			headers=self.headers).json()
	
	def edit_message(
			self,
			channel_id: int,
			message_id: int,
			content: str) -> dict:
		data = {
			"content": content
		}
		return requests.patch(
			f"{self.api}/channels/{channel_id}/messages/{message_id}",
			json=data,
			headers=self.headers).json()

	def ban_user_from_guild(
			self,
			guild_id: int,
			user_id: int) -> dict:
		return requests.put(
			f"{self.api}/guilds/{guild_id}/bans/{user_id}",
			headers=self.headers).json()

	def kick_user_from_guild(
			self,
			guild_id: int,
			user_id: int) -> dict:
		return requests.delete(
			f"{self.api}/guilds/{guild_id}/members/{user_id}",
			headers=self.headers).json()

	def create_role(
			self,
			name: str,
			guild_id: int,
			type: int = 0) -> dict:
		data = {
			"name": name,
			"type": type
		}
		return requests.post(
			f"{self.api}/guilds/{guild_id}/roles",
			json=data,
			headers=self.headers).json()

	def join_guild(self, invite: str) -> dict:
		return requests.post(
			f"{self.api}/invites/{invite}",
			headers=self.headers).json()

	def get_guild_invites(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}/invites",
			headers=self.headers).json()

	def get_guild_roles(self, guild_id: int) -> dict:
		return requests.get(
			f"{self.api}/guilds/{guild_id}/roles",
			headers=self.headers).json()

	def change_avatar(self, avatar_id: str) -> dict:
		data = {
			"avatar": avatar_id
		}
		return requests.patch(
			f"{self.api}/users/@me",
			json=data,
			headers=self.headers).json()

	def change_password(
			self,
			old_password: str,
			new_password: str) -> dict:
		data = {
			"new_password": new_password,
			"password": old_password
		}
		return requests.patch(
			f"{self.api}/users/@me",
			json=data,
			headers=self.headers).json()

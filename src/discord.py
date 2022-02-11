import requests
from time import time
from json import dumps


class Client():
    def __init__(self):
        self.api = "https://discord.com/api/v9"
        self.headers = {
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
        }

    # authorization
    def login(self, email: str, password: str):
        data = dumps({
            "login": email,
            "password": password,
            "undelete": False,
            "captcha_key": None,
            "login_source": None,
            "gift_code_sku_id": None
        })
        response = requests.post(
            f"{self.api}/auth/login",
            headers=self.headers,
            data=data).json()
        try:
            self.email = email
            self.password = password
            self.token = response["token"]
            self.headers["Authorization"] = self.token
        except BaseException:
            exit(response)
        return response

    # logout
    def logout(self):
        data = dumps({"provider": None, "voip_provider": None})
        return requests.post(
            f"{self.api}/auth/logout",
            data=data,
            headers=self.headers).json()

    # affinities users
    def affinities_users(self):
        return requests.get(
            f"{self.api}/users/@me/affinities/users",
            headers=self.headers).json()

    # return your guilds(servers) list
    def list_guilds(self):
        return requests.get(
            f"{self.api}/users/@me/guilds",
            headers=self.headers).json()

    # return info about guild(server)
    def guild_info(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}",
            headers=self.headers).json()

    # return list channels from guild(server)
    def guild_channels(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}/channels",
            headers=self.headers).json()

    # return your dialogs
    def my_channels(self):
        return requests.get(
            f"{self.api}/users/@me/channels",
            headers=self.headers).json()

    # leave guild
    def leave_guild(self, guild_id: int):
        return requests.delete(
            f"{self.api}/users/@me/guilds/{guild_id}",
            headers=self.headers).json()

    # leave channel
    def leave_channel(self, channel_id: int):
        return requests.delete(
            f"{self.api}/users/@me/channels/{channel_id}",
            headers=self.headers).json()

    # discoverable guilds
    def discoverable_guilds(self, offset: int = 0, limit: int = 24):
        return requests.get(
            f"{self.api}/discoverable-guilds?offset={offset}&limit={limit}",
            headers=self.headers).json()

    # get relationships
    def get_relationships(self):
        return requests.get(
            f"{self.api}/users/@me/relationships",
            headers=self.headers).json()

    # get user info
    def get_user_info(self, user_id: int):
        return requests.get(
            f"{self.api}/users/{user_id}/profile",
            headers=self.headers).json()

    # delete friend
    def delete_friend(self, user_id: int):
        return requests.delete(
            f"{self.api}/users/@me/relationships/{user_id}",
            headers=self.headers).json()

    # typing active
    def typing_active(self, channel_id: int):
        return requests.get(
            f"{self.api}/channels/{channel_id}/typing",
            headers=self.headers).json()

    # change username
    def change_username(self, username: str):
        data = dumps({"password": self.password, "username": username})
        return requests.patch(
            f"{self.api}/users/@me",
            headers=self.headers,
            data=data).json()

    # change status
    def change_status(self, emoji_name: str = None, text: str = None):
        data = dumps({
            "custom_status":
            {"emoji_name": emoji, "text": text}
        })
        return requests.patch(
            f"{self.api}/users/@me/settings",
            headers=self.headers,
            data=data).json()

    # send message
    def send_message(self, content: str = None, channel_id: int = None):
        data = dumps({"content": content})
        return requests.post(
            f"{self.api}/channels/{channel_id}/messages",
            headers=self.headers,
            data=data).json()

    # delete message
    def delete_message(self, message_id: int, channel_id: int):
        return requests.delete(
            f"{self.api}/channels/{channel_id}/messages/{message_id}",
            headers=self.headers).json()

    # get_channel messages
    def get_channel_messages(self, channel_id: int, limit: int = 100):
        return requests.get(
            f"{self.api}/channels/{channel_id}/messages?limit={limit}",
            headers=self.headers).json()

    # def get regions id
    def get_regions(self):
        return requests.get(
            f"{self.api}/voice/regions",
            headers=self.headers).text

    # get guild banned users
    def get_guild_bans(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}/bans",
            headers=self.headers).json()

    # get guild users list
    def get_guild_users(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}/members",
            headers=self.headers).json()

    # delete channel
    def delete_channel(self, channel_id: int):
        return requests.delete(
            f"{self.api}/channels/{channel_id}",
            headers=self.headers).json()

    # edit message
    def edit_message(self, channel_id: int, message_id: int, content: str):
        data = {"content": content}
        return requests.patch(
            f"{self.api}/channels/{channel_id}/messages/{message_id}",
            headers=self.headers,
            json=data).json()

    # ban user from guild
    def ban_user_from_guild(self, guild_id: int, user_id: int):
        return requests.put(
            f"{self.api}/guilds/{guild_id}/bans/{user_id}",
            headers=self.headers).json()

    # kick user from guild
    def kick_user_from_guild(self, guild_id: int, user_id: int):
        return requests.delete(
            f"{self.api}/guilds/{guild_id}/members/{user_id}",
            headers=self.headers).json()

    # create role
    def create_role(self, guild_id: int, role_name: str, type: int = 0):
        data = {"name": role_name, "type": type}
        return requests.post(
            f"{self.api}/guilds/{guild_id}/roles",
            headers=self.headers,
            data=data).json()

    # join guild
    def join_guild(self, invite: str):
        return requests.post(
            f"{self.api}/invites/{invite}",
            headers=self.headers).json()

    # get guild invites
    def get_guild_invites(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}/invites",
            headers=self.headers).json()

    # get roles
    def get_roles(self, guild_id: int):
        return requests.get(
            f"{self.api}/guilds/{guild_id}/roles",
            headers=self.headers).json()

    # change avatar
    def change_avatar(self, avatar_id: str):
        data = {"avatar": avatar_id}
        return requests.patch(
            f"{self.api}/users/@me",
            headers=self.headers,
            data=data).json()

    # change password
    def change_password(self, new_password: str):
        data = {
            "new_password": new_password,
            "password": self.password
        }
        return requests.patch(
            f"{self.api}/users/@me",
            headers=self.headers,
            data=data)

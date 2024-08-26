from io import IOBase
from typing import Any
from dataclasses import dataclass

import slack_sdk

@dataclass
class SlackClient():
    bot_token: str

    def _client(self):
        return slack_sdk.WebClient(self.bot_token)

    def post_message_block(self, channel_id: str, blocks: Any | None, text: str = ""):
        self._client().chat_postMessage(channel=channel_id, text=text, blocks=blocks ) # type: ignore

    def upload(self, file: str | bytes | IOBase | None): # type: ignore
        return self._client().files_upload_v2(file=file) # type: ignore
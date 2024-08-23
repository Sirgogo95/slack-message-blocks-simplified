import os
from io import IOBase

import slack_sdk
from dotenv import load_dotenv

class SlackClient():
    load_dotenv(override=True)
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    client = slack_sdk.WebClient(bot_token)
    channel = os.environ.get("SLACK_CHANNEL")

    @classmethod
    def post_message_block(cls, channel_id: str, blocks: str | None, text: str = ""):
        cls.client.chat_postMessage(channel=channel_id, text=text, blocks=blocks ) # type: ignore

    @classmethod
    def upload(cls, file: str | bytes | IOBase | None):
        return cls.client.files_upload(file=file) # type: ignore
# import mcs_config
import os
from slack_sdk import WebClient


slack_token = os.environ.get("SLACK_BOT_TOKEN")
slack_app_token = os.environ.get("SLACK_APP_TOKEN")
slack_bot_handle = WebClient(token=slack_token)

slack_bot_handle.chat_postMessage(
    channel='C03BRB95HQQ',
    text='slack_msg'
)
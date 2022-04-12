import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"),name = 'eas-viktor-app')

@app.message("h")
def message_hello(message, say):
    print(message)
    dm_channel = message['channel']
    say(f"Welcome to the channel, <@{message['user']}>!", channel=dm_channel)

@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
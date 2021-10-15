from src.discord import Discord

# Initialize Discord object with your discord token
TOKEN = "Your Discord token here"
client = Discord(TOKEN)

# Send message to a channel
# The client will also send a typing request for one second before sending the message
client.send_message("channelID", "Hello, World!")

# Get messages from a channel, default limit is 50.
# Returns a response json
messages = client.get_messages("channelID", limit=10)
print(messages)

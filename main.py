#!/bin/usr/env python

"""Stabble Diffusion + telegram chatbot
"""
import telegram
import logging
import replicate
import threading
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

# Enter Telegram below
telegram_bot_token = '6074700225:AAFh8jdU8w5Xl2RSVJb6w6ho36Q-SrAfZ0c'
bot = telegram.Bot(telegram_bot_token)
# print(bot.get_me())

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

model = replicate.models.get("stability-ai/stable-diffusion")



#Start Command
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to the StableDiffusionBot. "
                                  "\n\nHere you can let your creativity run wild! "
                                  "\n\nUse the /generate <Text> command to generate images using StableDiffusion")

# Help Command
def helpCommand(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="You can generate images with the following command: \"/generate <Text>\". \n\nFor example: \n/generate A dog flying in space")


# Generate Command
def generate(update: Update, context: CallbackContext):
    prompted_text = str(update.message.text)
    # Remove the "/generate " word from the string
    try:
        prompted_text = prompted_text.split(' ', 1)[1]
    except IndexError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a description of what you want to get generated after the /generate command. Don't forget too leave a space in between the command and the text ;)")
        return

    # Send additional Informations
    context.bot.send_message(chat_id=update.effective_chat.id, text="Generating image: " + prompted_text)
    # Generate an Image using Stable Diffusion with the text entered from the user. Returns a List of URLs to pictures
    try:
        output_url = model.predict(prompt=prompted_text)[0]
    except replicate.exceptions.ModelError:
        logging.info('ModelError occured with prompt: ' + str(prompted_text) + " from User: " + update.effective_chat.username)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Generation failed - NSFW Content Detected")
        return

    # Print the link to the generate Picture
    # print(output_url)
    # Send the Image to the Chat user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=output_url)

# Should stop the Bot
#def shutdown():
#    updater.stop()
#    updater.is_idle = False

# Should stop the bot
#def stop(update: Update, context: CallbackContext):
#    context.bot.send_message(chat_id=update.effective_chat.id, text="StableDiffusionBot Shutting Down :( \nSee ya soon!")
    #threading.Thread(target=shutdown()).start()

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=telegram_bot_token, use_context=True)

    """Run the bot."""
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('generate', generate))
    updater.dispatcher.add_handler(CommandHandler('help', helpCommand))
    #updater.dispatcher.add_handler(CommandHandler('stop', stop))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

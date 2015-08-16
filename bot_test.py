__author__ = 'mahdi'
import requests
import telegram


def setServer(bot):
    bot.setWebhook('https://helli5.herokuapp.com/bot/')


def offServer(bot):
    bot.setWebhook('')


if __name__ == '__main__':
    bot = telegram.Bot(token='120382199:AAFasWEvkSBsRwQLnDbXOyFytS7SHo0PBiQ')
    setServer(bot)
    # updates = bot.getUpdates()
    # r = requests.post('https://helli5.herokuapp.com/bot/', {'Update': updates[-1].message.chat_id})
    # with open("~/Desktop/test.html", "wt") as out_file:
    #     out_file.write(r.text)

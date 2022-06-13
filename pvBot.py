import pytz
from telegram import *
from telegram.ext import *
from datetime import datetime
from tracker import get_prices
import jdatetime

list = {
    'channelID': 'YOUR_CHANNEL_ID',
    'botID': '\n\nYOUR_BOT_ID\n',
    'info1': '🌐 آدرس سایت: https://pouyaarz.com\n\n\n',
    'info2': '🛑 برای خرید و فروش تتر و سایر ارزها لطفا به شماره زیر در واتس آپ یا آیدی زیر در تلگرام پیام دهید.\n',
    'info3': 'https://wa.me/YOUR_NUMBER\n\n@PouyAarzEX',
    'info4': '☎️ شماره تماس: 3445-051 (داخلی5)\n',
    'info5': '📞همراه: YOUR_NUMBER',
    'separateLine': '\nــــــــــــــــــــــــــــــــــــــــــــــــ\n',
    'ads': 'پویا ارز' + '\n✅ خرید و فروش ارزهای دیجیتال',
}
strr = list['ads']
strr += list['separateLine']
strr += list['info1']
strr += list['info2']
strr += list['info3']
strr += list['separateLine']
strr += list['channelID']
strr += list['botID']

updater = Updater(token='YOUR_BOT_TOCKEN')
dispatcher = updater.dispatcher

showPrice = 'قیمت لحظه ای'
aboutUs = 'ارتباط با ما'
aboutUsStr = list['ads']
aboutUsStr += list['separateLine']
aboutUsStr += list['info1']
aboutUsStr += list['info4']
aboutUsStr += list['info5']
aboutUsStr += list['separateLine']
aboutUsStr += list['channelID']
aboutUsStr += list['botID']

jdatetime.set_locale('fa_IR')
jdatetime.datetime.now().strftime('%A %B')
list = {
    'botToken': 'YOUR_BOT_TOCKEN',
    'channelID': 'YOUR_CHANNEL_ID',
    'botID': '\nYOUR_BOT_ID\n',
    'info': '🌐 آدرس سایت: https://pouyaarz.com\n📞 شماره تماس: 38466514-051\nآدرس: مشهد بین سناباد ۴۴ و ۴۶ پلاک ۴۶۸ طبقه دوم',
    'separateLine': '\nــــــــــــــــــــــــــــــــــــــــــــــــ\n',
    'ads': 'پویا ارز' + '\n✅ خرید و فروش ارزهای دیجیتال',
}


def func():
    dateStr = str(jdatetime.date.today())
    time = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
    message = "قیمت لحظه ای ارزهای برتر (USD):"
    message += '\n🗓' + dateStr + '\n🕐' + time
    message += list['separateLine']
    crypto_data = get_prices()
    print(crypto_data)
    count = 1
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        if (count == 1):
            c = '🟠'
        elif (count == 2):
            c = '🔵'
        elif (count == 3):
            c = '🟡'
        elif (count == 4):
            c = '🟣'
        elif (count == 5):
            c = '⚫️'
        elif (count == 6):
            c = '🟡'
        elif (count == 7):
            c = '🔵'
        elif (count == 8):
            c = '🟠'
        elif (count == 9):
            c = '🔴'
        elif (count == 10):
            c = '🟣'
        elif (count == 11):
            c = '🟠'
        elif (count == 12):
            c = '🟣'
        elif (count == 13):
            c = '🔵'
        else:
            c = '🔴'

        if (change_day > 0):
            d = '🔺'
        elif (change_day < 0):
            d = '🔻'

        if (change_hour > 0):
            x = '🔺'
        elif (change_hour < 0):
            x = '🔻'

        if (coin == 'XRP' or coin == 'ADA' or coin == 'DOGE' or coin == 'MATIC' or coin == 'TRX'):
            message += f"{c}{coin}\nPrice: $ {price:,.4f}\nHourly Change: {x}{change_hour:.3f}%\nDaily Change: {d}{change_day:.3f}%\n\n"
        elif (coin == 'SHIB'):
            message += f"{c}{coin}\nPrice: $ {price:,.8f}\nHourly Change: {x}{change_hour:.3f}%\nDaily Change: {d}{change_day:.3f}%\n\n"
        else:
            message += f"{c}{coin}\nPrice: $ {price:,.2f}\nHourly Change: {x}{change_hour:.3f}%\nDaily Change: {d}{change_day:.3f}%\n\n"
        count += 1
    message += strr
    return message


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(showPrice), KeyboardButton(aboutUs)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text='به ربات صرافی پویا ارز خوش آمدید',
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def messageHandler(update: Update, context: CallbackContext):
    if (showPrice == update.message.text):
        priceStr = func()
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=priceStr)
    elif (aboutUs == update.message.text):
        context.bot.sendMessage(chat_id=update.effective_chat.id, text=aboutUsStr)


dispatcher.add_handler(CommandHandler('start', startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.start_polling()
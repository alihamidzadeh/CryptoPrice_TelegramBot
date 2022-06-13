from datetime import datetime
import jdatetime
import time
import pytz

from tracker import get_prices
import requests

jdatetime.set_locale('fa_IR')
jdatetime.datetime.now().strftime('%A %B')

list = {
    'botToken': 'YOUR_BOT_TOCKEN',
    'channelID': 'YOUR_CHANNEL_ID',
    'botID': '\n\nYOUR_BOT_ID\n',
    # 'info': '🌐 آدرس سایت: https://pouyaarz.com\n📞 شماره تماس: 34456514-051\nآدرس: مشهد بین سناباد ۴۴ و ۴۶ پلاک ۴۶۸ طبقه دوم',
    'info1': '🌐 آدرس سایت: https://pouyaarz.com\n\n\n',
    'info2': '🛑 برای خرید و فروش تتر و سایر ارزها لطفا به شماره زیر در واتس آپ یا آیدی زیر در تلگرام پیام دهید.\n',
    'info3': 'https://wa.me/YOUR_PHONE_NUMBER\n\nYOUR_TELEGRAM_ID',
    'info4': '📞 شماره تماس: 34456514-051',
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


while True:
    priceStr = func()
    requests.post(
        'https://api.telegram.org/{}/sendMessage?chat_id={}&text={}'.format(list['botToken'], list['channelID'],
                                                                            priceStr))
    time.sleep(10)
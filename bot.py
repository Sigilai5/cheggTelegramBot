from bs4 import BeautifulSoup
import cloudscraper
import requests


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    # User object
    user = update.message.from_user
    get_user_firstname = user['first_name']

    update.message.reply_text('Hi there! ' + get_user_firstname)
    print(get_user_firstname)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def id(update, context):
    """Send user id when the command /id is issued."""
    get_user_id = str(update.message.chat_id)

    update.message.reply_text(get_user_id)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('Loading...Please wait⏳')

    scraper = cloudscraper.CloudScraper(interpreter='nodejs')
    # header = {'x-requested-with': 'XMLHttpRequest'}
    #
    # profile = scraper.post('https://auth.chegg.com/auth/_ajax/auth/v1/login?clientId=CHGG', data={'email':'briansigilai@gmail.com','password':'Madagascar2021!'}, headers=header)

    cookies = {
        'NID': '219=BGRmy4Gipqej5Zdupdtv6oMmKGe84-Qgu7sgrI4P2TaQYAG-5cdH1ewM4ZDeAt4QNzWbp6GfwtIm5bsVsqXuqJSbGQgylNGsPtS1ntl-5ORhIvN0xrq9hsEzLROD8eS72P5091ULk4D1M94EyjqlgHv6AMglDdErPgPChi1Z4pI',
        'UULE': 'a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjI2OTc2MzE2NTQ2MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDQ2NTMwNTYKICBsb25naXR1ZGVfZTc6IDM1NzcyODI1Ngp9CnJhZGl1czogNTY0MjAwCnByb3ZlbmFuY2U6IDYK',
        'NID': '219=v9fRgA7A5_KbNyc23ula-Y9nfYDUp4o2bt7J2ZjEJ8fMAPbezxjlqezXCoRsTnQwZAjlErs9Tps_0HAl8BauJ1b4AUmAh0A6J4dhh8-ghgq99M4HZbZ8NjUtcmYAZkKgKRYV5kIQrbu3iisvqSZov4zHNGf9Eudlpaj8t6ZIEnQ',
        '1P_JAR': '2021-07-22-17',
        'sa-user-id': 's%3A0-6beaf630-8ff4-44bf-79a9-14f3b207428e.TzTQg%2BqTVPlL%2Fo061ENESCuEv6KASwF4TuktTj9W4mU',
        'fr': '036giCLhdtwH9WecJ..Bg-a8C...1.0.Bg-a8C.',
        'personalization_id': '"v1_i/RVOTsFJVEB23/dN6p8Cw=="',
        'MUID': '104DFB8B2AD36B4C3103EBF72B516A5A',
        'sp_adid': '31e60865-a00d-4743-8a98-732f07b0b913',
        'TDID': 'aa04f46d-9400-4948-b61a-c3dc9c3d3d9f',
        'UID': '1KZ04REHI6JZNAIG9ZRG8Xg1626975989',
        '_px3': '2ad690fd6ff82073d4ef231607b34b0ed8fdcf6d0f6e835bb870106b4296c194:c+VLzSeLv/0K4pmmsS16TaFAdI5zKSlO4F2zK2SzOCUs99aM/U1kAG8SmgVXznQA5mvtzyZQG0Fh87sUv54UYg==:1000:UIimKFWddeC9QdSZYYNjcYJunwTCsXcTavXIMG8Uf7SucgF4P2Rn2s1BSUk4C02Fuk4qNFY/AJjBRpcyFVKU3Vda6QvZqO1CD0zG0AZF+sa60/Y5pGgOlQu+NVi8YGqTjpQLP8gt2yWWIv6NWHOI/vv/DZhRHCGiyMPTBy09ZyxVVzbBwIfbPvcYH0gRD+gjtwiS2PoIMlh+tMWexXJJyg==',
        'C': '0',
        '_ym_d': '1626975998',
        'wcs_bt': 's_4544d378d9e5:1626976580',
        '_omappvs': '1626976576865',
        'NWB': '869ffdcc5035d44df8afc392b8a76e0e.1626976002312',
        '_uetsid': 'bd618460ea0111eb879c63b8ae945de1',
        's_pers': '%20buFirstVisit%3Dcore%7C1784742379319%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Cmyaccount%257Cprofile%2520view%7C1626978376046%3B',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Jul+22+2021+20%3A56%3A19+GMT%2B0300+(East+Africa+Time)&version=6.10.0&hosts=&consentId=d2d128da-1e83-4156-8e32-8636ec87ef9a&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false',
        'expkey': '93A843B26D2748FF32EE120C0F142E6B',
        'AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg': '1',
        'exp': 'A311C%7CA803B%7CC024B%7CA209A%7CA212A%7CA448A%7CA890H',
        '_sdsat_authState': 'Hard%20Logged%20In',
        'U': 'c116fc120e9eecab4da15ab627de8553',
        'PHPSESSID': 'dvuv1pscsohk8t913lrgo2eg4a',
        'refresh_token': 'ext.a0.t00.v1.MSwZramn0pzK3qp9QzUPPF7LqRsVqVUdbCI1zPWFnNQP8LMgbm5Mi2ISVl0Cx5XFNAvd6JC4p4kIuBS1W2ZwWFM',
        '_ga': 'GA1.2.1704681889.1626975987',
        'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8ZDUyNjMzZTktMmEwYy00ZjVlLThlYjItMzNmOWVlN2NlOTBmIiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyNjk3NjA2MywiZXhwIjoxNjI2OTc3NTAzLCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.Vcy0cs8hPvmgk0yp52e19-n4KdQA0pGO8KNWLDEWpHE8q9KScwNy8TxigA78AmRkllmkDRMMoC_RPNC9njmDSVtVuZkAHOuWO5JyVSSV63oPJfJpvk2_GJXVTrIpK0o1tVgFDuBwZLKKyOYZ8jipYIFSNWoubqxtWG0m06YTZpfX8gMcBj-PDOk4r8QUSJpRUuaaBCCI2VA8wihTJyy_I96etJpWH5sRFVTiEUzUYdsRcQdE8MmET7vvXEtBZcSwWRMvZixmQOP29_Z0739wuErpJXO8cPYvGqsQ9Rb1skNq-vMwDWdrfdxAIY1Gi0pl3291-jksJhrXoktYfAUKRg',
        '_px3': 'a5b0704fcdbe2b0a57063338aef9f750251c7a8d89f70170eaeafb868050e440:w5RZa5reWCRxkSm1tEoeON5B3ghb60l/s7bGPW9HlgGyL9nHL6cyxJi84zxkXLwhEl+/OrUq1ldubhV9vIY7Ig==:1000:LDSHXAn3W8aox88B8YCR7640pCLpD3DvII4EGjZoU6s7WUDtAcCTQoCilnULPq43X2S5Lo7A9wenhkFzWPwkGze3x10Ia21lLW7xWiuLGAjUsUijES99UjoYDbGBTjZv+EBDn7kgdc3pu91ECqgBnIa7OzOH4qngk4uqGD2zGcJPyiou4Zg0Y9rJUFjzlgiSJlnhYtdwc1WvWML7vgyX5Q==',
        'forterToken': 'b8d9cd5d5f4f4a5a8c5ccd7c63b13073_1626976043654__UDF43-mnf_13ck',
        'usprivacy': '1YNY',
        '_ym_isad': '1',
        '_fbp': 'fb.1.1626975999361.1889121883',
        'user_geo_location': '%7B%22country_iso_code%22%3A%22KE%22%2C%22country_name%22%3A%22Kenya%22%2C%22region%22%3A%2230%22%2C%22region_full%22%3A%22Nairobi+Province%22%2C%22city_name%22%3A%22Nairobi%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22sw-KE%22%5D%7D%7D',
        'optimizelyEndUserId': 'oeu1626975976762r0.33333323844543084',
        '_gcl_au': '1.1.668831552.1626975987',
        'sa-user-id-v2': 's%3A0-6beaf630-8ff4-44bf-79a9-14f3b207428e%24ip%2441.90.250.60.kuEAz96JA2F0haLy%2BGO9U3H9QUGrOd%2F0SoCixdrmnU8',
        '_sdsat_cheggUserUUID': 'd52633e9-2a0c-4f5e-8eb2-33f9ee7ce90f',
        '__gads': 'ID=83682b707acf0284:T=1626976045:S=ALNI_MZdpXOSnqaEfr37lRaXEzFQsVzg7Q',
        '_ym_uid': '1626080555970279077',
        'CSessionID': '91a84824-f879-4117-a83f-933a3e6b6bd7',
        'IDE': 'AHWqTUnMqsvczUWWlLkRgxRKpCTj2LAwL0HOlGPOw6PpP2O_Xs3m26rG8CecBDmfiHs',
        'CVID': '60750327677920277222135795013470136607',
        'adobeujs-optin': '%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D',
        '_omappvp': '8TfbmDXtrWOBOWvMGPA8GmW394GAyB35hs5DjqBH5F2L5yIG1X9fR3cn3LdbvaKApijq6RWD3mRHqgAy76AbOl3f3P0RffpS',
        'id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkNTI2MzNlOS0yYTBjLTRmNWUtOGViMi0zM2Y5ZWU3Y2U5MGYiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTY0Mjc0NjA2MywiaWF0IjoxNjI2OTc2MDYzLCJlbWFpbCI6ImJyaWFuc2lnaWxhaUBnbWFpbC5jb20ifQ.GE06AAKIGjczMQAzy44hHUNr66LU9otIlbnMY0kcyHf-jdO88AM3-jsLwh31m_xXR7SjKEhpUhQkCu9gzFnG7GJqeUTGR5ZGPtb7iKBoQ1xhVf-hXsUdk-Nb0d22s6vnpNVZszT-0kBHN7kNQHHocZy5gc6GyVqqhH291Bzd-6g5v9xMEVyoYrbX0-fEfNfsJHTBxHVAn2za6QpZ0WN5tRDbbHAaxTFHjzGR3ckC27DOi5gCW-h929fqYab6uPS2ZrwNfv6GdmpR_IgqoRIi8cPJoIz_6KzQWa8tm0Fg5--NCVqAlT2jSqcTCFbZaQeY2ZHfwA17AaDbYVxKtKmqHw',
        'schoolapi': '0d70f953-752d-4269-9595-051a894a87a2|0.962962963',
        'AMCV_3FE7CBC1556605A77F000101%40AdobeOrg': '-408604571%7CMCIDTS%7C18831%7CMCMID%7C60750327677920277222135795013470136607%7CMCAAMLH-1627580779%7C6%7CMCAAMB-1627580779%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C776897612%7CMCOPTOUT-1626983179s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18838%7CvVersion%7C4.6.0',
        'CSID': '1626974209327',
        'TDCPM': 'CAESEgoDYWFtEgsI9Pvo2dbQ5jkQBRIZCgpyaWdodG1lZGlhEgsI9Pvo2dbQ5jkQBRIXCghhcHBuZXh1cxILCPLs5efW0OY5EAUYBSABKAMyCwj08-uG7dDmORAFOAFCBCICCAFaB2VuNGdrNXFgAQ..',
        '_uetvid': '4a5bcec0bc8f11eba51331f7f26b7503',
        's_ecid': 'MCMID%7C60750327677920277222135795013470136607',
        'mcid': '60750327677920277222135795013470136607',
        '_rdt_uuid': '1626975988347.202bd7cf-371e-4ff8-bfb0-af6ea8348596',
        '_gid': 'GA1.2.1365037583.1626975988',
        'V': '83a468d02d01cc9361a91048b2a65ba360f9aee7bcab58.11808165',
        's_sess': '%20buVisited%3Dcore%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Chome%25252520page%252526pidt%25253D1%252526oid%25253Dhttps%2525253A%2525252F%2525252Fwww.chegg.com%2525252Fmy%2525252Fprofile%252526ot%25253DA%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D0399432032308349-53C9369E27FD83B5%3B%20s_ptc%3D0.00%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E1.48%255E%255E0.22%255E%255E4.53%255E%255E0.21%255E%255E6.29%3B',
        'SU': 'Xwlz3xzA6SEDOBmoyVq3p4-WhHtBTwGFi4Gvq00kl13MZtbmjMWQPtNln2XbRFrXHdLjIyzwvSIZETcd6v2a3mQV9LqwJ2Hzv14DaYJ9TQpODvGHpoFAWuYw8Gz3ZUM0',
        'O': '0'

    }

    url = update.message.text

    s = scraper.get(url, cookies=cookies)

    soup = BeautifulSoup(s.text, 'html.parser')
    div_answer_wrap = soup.find('div', {'class': 'answer-given-body ugc-base'})



    # #Find Question
    div_question_wrap = soup.find('div', {'class': 'ugc-base question-body-text'})
    div_answer_wrap = soup.find('div',{'class':'answer-given-body ugc-base'})
    generated_file = open("Answer2.html", "w")
    with generated_file as contents:
        contents.write(str('<h1>Question</h1>'))
        contents.write(str(div_question_wrap))
        contents.write((str('<div style="background-color: lightyellow;">')))
        contents.write(str('<h1 style="color:blue">Expert Answer </h1>'))
        contents.write(str(div_answer_wrap))
        contents.write((str('</div>')))

    #User object
    user = update.message.from_user

    get_chat_id = str(update.message.chat_id) #Alternatively str(user['id'])
    get_user_firstname= user['first_name']

    files = {'document': open('Answer2.html')}
    resp = requests.post('https://api.telegram.org/bot1908002304:AAHUiPQIJRurvu4IPogHOI3OkYSwxpovIaU/sendDocument?chat_id='+get_chat_id+'&caption=Here is your answer, ' + get_user_firstname + '😃',files=files)
    for src in div_answer_wrap.find_all('img'):
        update.message.reply_text('Here is an image related to answer that might have failed to load 👇')
        update.message.reply_text(src['src'])


    # print(resp.status_code)
    #
    # update.message.reply_text(update.message.chat_id)






def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    TOKEN = "1908002304:AAHUiPQIJRurvu4IPogHOI3OkYSwxpovIaU"
    APP_NAME = "cheggbot254"

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("id", id))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
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

PORT = int(os.environ.get('PORT', 5000))
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


def account(update, context):
    """Send user id when the command /id is issued."""
    get_user_id = str(update.message.chat_id)

    update.message.reply_text("Your account number is: " + get_user_id)


def echo(update, context):
    """Echo the user message."""

    # "Sigilai Brian": 63710714,
    paid_users = {
        "Sigi Brian": 1672275813,
        "Japhet Moturi": 1788310499,
        "Sigilai Brian": 63710714,
        "Elkana Chegg": 761114919,
        "Tomno Kipsortich": 483654132,
         "Pete Gichana": 1022164467
    }

    paid_users_chat_id = paid_users.values()

    paid_users_list = list(paid_users_chat_id)

    if update.message.chat_id in paid_users_list:

        update.message.reply_text('Fetching answer...please wait⏳')

        scraper = cloudscraper.CloudScraper(interpreter='nodejs')
        # header = {'x-requested-with': 'XMLHttpRequest'}
        #
        # profile = scraper.post('https://auth.chegg.com/auth/_ajax/auth/v1/login?clientId=CHGG', data={'email':'briansigilai@gmail.com','password':'Madagascar2021!'}, headers=header)

        cookies = {
            'MUID': '171B1082BC4B657C3C580062BDB76474',
            'NA_SAC': 'dT1odHRwcyUzQSUyRiUyRnd3dy5jaGVnZy5jb20lMkZvcmRlcmNvbmZpcm1waXhlbCUyRiUzRnRva2VuJTNEUnJ2OUdjWkVXYVhVWE1SNXBqQXRJTUx0V25BZXprN1BZV3hUeVNGa2ZLUEx5MmdTVG9ISm9vNlRTSUcwSXNsWFBjSEtjZ09CbnN1cU1scG43Umo3ZlZfVHd0Q08zV0czX2ZyaUxaY1hvQ1hJOVppMGIweC1HRk84ekQ4Yi1CeHUlMjZjaGVja291dEZsb3dUeXBlJTNEU0lOR0xFX0lURU1fUFVSQ0hBU0V8cj1odHRwcyUzQSUyRiUyRnd3dy5jaGVnZy5jb20lMkZjc29yZGVyY29uZmlybSUzRnRva2VuJTNEUnJ2OUdjWkVXYVhVWE1SNXBqQXRJTUx0V25BZXprN1BZV3hUeVNGa2ZLUEx5MmdTVG9ISm9vNlRTSUcwSXNsWFBjSEtjZ09CbnN1cU1scG43Umo3ZlZfVHd0Q08zV0czX2ZyaUxaY1hvQ1hJOVppMGIweC1HRk84ekQ4Yi1CeHU=',
            'userData': '%7B%22authStatus%22%3A%22Hard%20Logged%20In%22%2C%22email%22%3A%22briankiprono54%40yahoo.com%22%2C%22attributes%22%3A%7B%22cheggUserUUID%22%3A%226783ff58-3d63-437d-9ef5-2a0207944b69%22%2C%22uvn%22%3A%22bfd2f92244f1f48613b0833e04e3533f617cf1f723d70c.60370105%22%7D%7D',
            '_sdsat_authState': 'Hard%20Logged%20In',
            'DFID': 'web|vWa6m3WAxOr88bjpJu4L',
            'optimizelyEndUserId': 'oeu1635578355823r0.21503341687149446',
            'mcid': '53244361067834326603350799501172673242',
            '_omappvp': '4fSbbs1DPqmfppvZckPqfvYjFl1ARTtXfwCTduw85PfUt1eX3jKds854EanDH7fM4teV463DAFY3d8kVY3Bghwenyouzfour',
            '_px3': 'f7e56cdbf83019a153053964b2fb92c485fe9e27135dd34a697f0c127c1f1098:N2mtDAAJ7YBxxkEuZsfJPO2CdQF3kDhLQL9h0viDIvTa0e9JLaSnwusJJd8JY6gqTMXE8pjuYrnFDnhEfqL+nA==:1000:8wNgykyBTr5toFzcJx6erjbSB0d8bkA68zWqWLDgq0BdYmp2HdVwkynTsXgDVBHAvLHjSjKVOx9wOA6JUqSKI0+AuZUfun90Dq79GyO9cK6vDCGR0iZ2/ovaDvkahu23VByInI/YXS+edguKpoyjBlb/VB2VKWF+nAa/MhJV+nJHrcpwv1/5uB33VTqDT9gsSoFJmuppkoOOXHOoMcM4KQ==',
            's_sess': '%20buVisited%3Dcs%252Ccore%252Ccw%252Ctb%3B%20s_sq%3D%3B%20s_cc%3Dtrue%3B%20s_ptc%3D0.00%255E%255E0.03%255E%255E0.16%255E%255E0.40%255E%255E0.79%255E%255E0.08%255E%255E9.68%255E%255E0.08%255E%255E11.87%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D594E785FF730B498-02DA5F83F3DF9C98%3B',
            's_pers': '%20buFirstVisit%3Dcs%252Ccore%252Ccw%252Ctb%7C1793634858287%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Chome%2520page%7C1635933199410%3B',
            'IR_PI': '714d413d-3bf4-11ec-a8ee-c7b0a603b188%7C1636017744434',
            'sa-user-id': 's%3A0-8d4e4b9b-5797-4c83-46ab-51d1f6f9dae1.robjeV7aUd1oLJWxwk5IfG%2F3V%2B7nO6pZ66iaAyVtFZs',
            'IR_14422': '1635931344434%7C0%7C1635931344434%7Cy1Vww9zKYxyIWrPQHcWEzT3UUkG0FY11v0w9Xc0%7C',
            '_tq_id.TV-8145726354-1.ad8a': '4c0af3c9c1f67059.1635578400.0.1635931346..',
            'usprivacy': '1YNY',
            'ab.storage.sessionId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1': '%7B%22g%22%3A%22b2b201c0-a337-a19b-e00e-dde30990b095%22%2C%22e%22%3A1635933142661%2C%22c%22%3A1635931336772%2C%22l%22%3A1635931342661%7D',
            '_uetvid': '4a5bcec0bc8f11eba51331f7f26b7503',
            '_uetsid': '0195eca03b6711ec8b045d0a7b56d9c5',
            'ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1': '%7B%22g%22%3A%226783ff58-3d63-437d-9ef5-2a0207944b69%22%2C%22c%22%3A1635868350283%2C%22l%22%3A1635931336780%7D',
            'aamsc': 'aam%3D2053348%2Caam%3D2756555%2Caam%3D5674360',
            '_gcl_dc': 'GCL.1635870323.Cj0KCQjww4OMBhCUARIsAILndv5O_ih7c3mKKX8Rw5p1IeBNfaUNzotrisD0CWLmiwyb7b_9bgGbf88aArJFEALw_wcB',
            'aam_uuid': '53261213119524546383354745304178185952',
            '_sdsat_irclickid': 'y1Vww9zKYxyIWrPQHcWEzT3UUkG0FY11v0w9Xc0',
            'expkey': '6A9EB425E3CDF622ABA17473F175324D',
            'AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg': '1',
            'exp': 'A803B%7CC024A%7CA560B%7CA259B%7CA209A%7CA212A%7CA263B%7CA264B%7CA270C%7CA127H%7CA289D%7CA448A',
            'forterToken': '104172e3c7064f3fb3195290fb9d0b5d_1635871946588__UDF43-mnf-anf_13ck',
            'ab.storage.deviceId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1': '%7B%22g%22%3A%22ddf8d7bc-ad4e-5dbb-1ffe-18dea0460625%22%2C%22c%22%3A1627566710313%2C%22l%22%3A1635931336778%7D',
            '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Name%22%2C%22home%20page%22%5D%2C%222%22%3A%5B%22Experience%22%2C%22desktop%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22checkout%22%5D%2C%224%22%3A%5B%22Auth%20Status%22%2C%22Logged%20Out%22%5D%7D',
            '_ym_isad': '1',
            'wcs_bt': 's_4544d378d9e5:1635931342',
            'C': '0',
            '_ym_d': '1635870198',
            'CSessionID': '3ef10493-45d9-486d-be1a-81377067791b',
            '_ym_uid': '1626080555970279077',
            'U': '88fce73af420420c95a5ee1472149667',
            'PHPSESSID': 'b7cd3e66bbf5ada0e90570f276ffce2c',
            'refresh_token': 'ext.a0.t00.v1.MR_l6hmiw989quXPMr15mpaRdEazsJaczLSiasdl2FE0FOPR7y8hJSH84fvt5LyNmK0JAVtzGy6RA-tWvNwx5Kk',
            'CVID': '53244361067834326603350799501172673242',
            'adobeujs-optin': '%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D',
            '__gads': 'ID=a6c1ddef2088d432:T=1635868310:S=ALNI_MaN8n2upt0ULJ61sXkjqen2D5A0SQ',
            'SU': 'jrl92xvW9Do4qISapklMnviJ3PmI750MtCZH1dqvmeAW4dkvyOJjx9GS0S3eHcRQhROLoUHR5bnQTW1oAR8R5LWPketRAqm9lBq2Oros121hYo1c8-ybPVlB0zj-7mkY',
            'O': '0',
            'sa-user-id-v2': 's%3A0-8d4e4b9b-5797-4c83-46ab-51d1f6f9dae1%24cell.Yc3snQ5ZTwU1jCqkaGvI7B01Xbsn6AHEWi%2Fa%2B8uot%2FI',
            '_sdsat_cheggUserUUID': '6783ff58-3d63-437d-9ef5-2a0207944b69',
            '_cs_c': '0',
            'IR_gbd': 'chegg.com',
            '_fbp': 'fb.1.1635578397798.1195868742',
            'cb_prompt_message': 'Yes',
            'chegg_web_cbr_id': 'a',
            'opt-user-profile': '6783ff58-3d63-437d-9ef5-2a0207944b69%252C20770133538%253A20764501213',
            'aam_tnt': 'aam%3D2053348',
            '_sdsat_highestContentConfidence': '{%22course_uuid%22:%2214e46fb9-e09e-406c-ac7d-3e332a35052f%22%2C%22course_name%22:%22heat-transfer-thermodynamics%22%2C%22confidence%22:0.9394%2C%22year_in_school%22:%22college-year-3%22%2C%22subject%22:[{%22uuid%22:%22ed065c84-79f2-4813-bbcf-13b75dda2abc%22%2C%22name%22:%22mechanical-engineering%22}]}',
            '_gid': 'GA1.2.967579208.1635807413',
            '_rdt_uuid': '1635578397602.0c5d0079-9cbe-4e29-98ae-3ff2189f7b48',
            'user_geo_location': '%7B%22country_iso_code%22%3A%22KE%22%2C%22country_name%22%3A%22Kenya%22%2C%22region%22%3A%2214%22%2C%22region_full%22%3A%22Kilifi+District%22%2C%22city_name%22%3A%22Kilifi%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22sw-KE%22%5D%7D%7D',
            '_ga': 'GA1.2.1250209600.1635578397',
            'intlPaQExitIntentModal': 'hide',
            's_ecid': 'MCMID%7C53244361067834326603350799501172673242',
            '_px': 'uB7fm7G+a39WGQy9yDaMrweuTzUZYyj7Ky1WwTgnUF/K6cqHwozyzFXN/GTShIU8ucvtHKFMyWziG3mwp16+Tg==:1000:fhzfV8kadYEsyQJocqERi7ChxM0f0aLZE/yyJLnKyFyyhNpd4m5kMWgAoSeGwQ355xuuz2dsQxTWJBb/6QFPfQK3GVplmE5UM21kyJPtM9BOeeSRXHR6p0SOX2n39IKTskYGp+WZIzjN4o4t1xd37M0BLZy+/GSyaShai/efEDEqRxZCr8P4cFJy4TnKHcc6sTTkhd835eqC9ssM7Dc6anoFwAALO6jY9TL5EmM7cPtTicDpjqyhCP/2b2mTzZ1s+htPZRbyWDbB84okmC3LWg==',
            '_pxvid': 'b1ccb96d-3951-11ec-82ce-584b76494850',
            'sourceTracking': 'google',
            'optimizelyEndUserId': 'oeu1635578355823r0.21503341687149446',
            '_gcl_au': '1.1.2093134104.1635578397',
            '_scid': '851e0e58-acb7-42cd-9ffe-93e172cdf6f7',
            '_sctr': '1|1635541200000',
            'AMCV_3FE7CBC1556605A77F000101%40AdobeOrg': '-408604571%7CMCIDTS%7C18935%7CMCMID%7C53244361067834326603350799501172673242%7CMCAAMLH-1636531384%7C6%7CMCAAMB-1636531384%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1635933784s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18938%7CvVersion%7C4.6.0%7CMCCIDH%7C1923490845',
            'id_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImJyaWFua2lwcm9ubzU0QHlhaG9vLmNvbSIsImlzcyI6Imh1Yi5jaGVnZy5jb20iLCJzdWIiOiI2NzgzZmY1OC0zZDYzLTQzN2QtOWVmNS0yYTAyMDc5NDRiNjkiLCJhdWQiOiJDSEdHIiwiaWF0IjoxNjM1ODY4MzI3LCJleHAiOjE2MzkwMTQ3MTksInJlcGFja2VyX2lkIjoiYXB3In0.NnGuBZL8e4M4-xrnaz4fZBvvlV7oSUr4fejVleihzotCwP1p0guTwGcdY0amCP4cdR1QhNL891BySpGDeKajb3HiFNxf3VsTrmVwtQ7oV7AE33aY0Dt9MISRnDS3a1RS2IagesM5QFQUnVdyiJWOC_iIabCFcTvx1bQcQBQJWp55rkigK7R5LY9Jmm6V_wnVN-Aq6Grc9JOjbj5SJyM76q1ykQ63wuohHvJY1RmEfBQabNRzXJSm-s2fWx5RX-DRGY7MfN-WIziZN8jhZnHeX5o_sXGXQqmE5Q-6593XUGZOuvUkd_iDKWlfqHpAOW3waxakrx0V7Ti2inc4wDWH5g',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Wed+Nov+03+2021+12%3A22%3A19+GMT%2B0300+(East+Africa+Time)&version=6.18.0&hosts=&consentId=b6729213-4bc3-4f8c-bd38-cca4b09db4cb&interactionCount=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1',
            '_gcl_aw': 'GCL.1635870323.Cj0KCQjww4OMBhCUARIsAILndv5O_ih7c3mKKX8Rw5p1IeBNfaUNzotrisD0CWLmiwyb7b_9bgGbf88aArJFEALw_wcB',
            '_gac_UA-499838-3': '1.1635870322.Cj0KCQjww4OMBhCUARIsAILndv5O_ih7c3mKKX8Rw5p1IeBNfaUNzotrisD0CWLmiwyb7b_9bgGbf88aArJFEALw_wcB',
            'V': 'bfd2f92244f1f48613b0833e04e3533f617cf1f723d70c.60370105',
        }

        url = update.message.text

        s = scraper.get(url, cookies=cookies)

        soup = BeautifulSoup(s.text, 'html.parser')

        div_question_wrap = soup.find('div', {'class': 'ugc-base question-body-text'})
        div_answer_wrap = soup.find('div', {'class': 'answer-given-body ugc-base'})
        # not_answered_yet = soup.find('div', {'class': 'hangTight'}).text
        # upvotes = soup.find('div',{'class':'feedback-rating content-feedback'})
        # downvotes = soup.find('div',{'class':'negative-rating rating-block'})
        generated_file = open("dynamic_files/"+str(update.message.chat_id)+".html", "w")
        with generated_file as contents:
            contents.write(
                str('<meta charset="UTF-8">'))
            contents.write(
                str('<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" / >'))
            contents.write(
                str('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>'))
            contents.write(
                str("<script>(function($) { $(document).ready(function() { $('img').each(function() {   var $el = $(this), s = $el.attr('src'), sRx = /^[\/data\/]+/igm; if (s.startsWith('data:image/')) {$el.attr('src', s);} else {if (sRx.test(s)) {s = 'http:' + s;$el.attr('src', s);}}});});})(jQuery);</script>"))
            contents.write(
                '<center><img src="https://prnewswire2-a.akamaihd.net/p/1893751/sp/189375100/thumbnail/entry_id/0_tywxthw7/def_height/2700/def_width/2700/version/100012/type/1" width="600px" height="200px"></center>'
            )
            contents.write(str('<h1>Question</h1>'))
            contents.write(str('<style>.hidden{display:none;}</style>'))
            contents.write(str(div_question_wrap))
            contents.write((str('<div style="background-color: lightyellow;">')))
            contents.write(str('<h1 style="color:orange">Expert Answer </h1>'))
            contents.write(str(div_answer_wrap))
            contents.write((str('</div>')))

        # User object
        user = update.message.from_user

        get_chat_id = str(update.message.chat_id)  # Alternatively str(user['id'])
        get_user_firstname = user['first_name']

        files = {'document': open("dynamic_files/" + str(update.message.chat_id) + ".html")}
        resp = requests.post(
            'https://api.telegram.org/bot2064320160:AAH00PsltMPt30gXdxl3dUjLtjpbCiLI6kk/sendDocument?chat_id=' + get_chat_id + '&caption=Here is your answer, ' + get_user_firstname + '😃',
            files=files)

    else:
        # User object
        user = update.message.chat.username
        get_username = str(user)

        update.message.reply_text('Please contact 0792071275 on Whatsapp  for unlocks.')




def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    TOKEN = "2064320160:AAH00PsltMPt30gXdxl3dUjLtjpbCiLI6kk"

#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

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
    dp.add_handler(CommandHandler("account", account))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()




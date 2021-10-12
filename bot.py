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
            'SAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            'APISID':'ED3QnFAIw3lheBos/ASw10Lbh41SLEEcia',
            'SSID':'AvvaR08JYaOBZ2U_l',
            'HSID':'A8A6rmoeAaxClt_eN',
            '__Secure-1PSID':'BAjz3cSYRZFIVm5BspKpaIygxS9WVhNHtjIvFIHRvRN8zCcuDY5LVXzp3kt7rrpGWpJ4_Q.',
            'SID':'BAjz3cSYRZFIVm5BspKpaIygxS9WVhNHtjIvFIHRvRN8zCcuk_dqhP1gRUgk9SFXxULAiA.',
            '__Secure-3PSIDCC':'AJi4QfH_En9maTW8G6h2gyGo0czrlOqwEx0NYEaeytAW_EGUg2Yp3tVgP6gE9wIk_AmM2y-p-4c',
            'SIDCC':'AJi4QfH2Q8w2rNRQwpIJX9KX3_DvXDBbOmqJ1yYSe_ZmogYLVxNG54PPCZDLp9VZRoq8KXrK_sCI',
            '__Secure-1PSIDCC':'AJi4QfFpByq8smzIYMb3RYomOdPhiOIGetJYgs_DlP37ScKe2WlzOvyconVWhWv-CXJJn1sP8w',
            '__Secure-1PSID':'BQjz3XGfWeSPWVJz_0TjS61GCbBoEKkyc0e36mwKnFcPF0CMTjBDal7PZ8d22PAmDpAeFQ.',
            'SID':'BQjz3XGfWeSPWVJz_0TjS61GCbBoEKkyc0e36mwKnFcPF0CMTjBDal7PZ8d22PAmDpAeFQ.',
            '__Secure-3PAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            '__Secure-1PAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            'HSID':'AdJv02w6vWg6RZZY-',
            '__Secure-3PAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            '__Secure-3PSID':'BQjz3XGfWeSPWVJz_0TjS61GCbBoEKkyc0e36mwKnFcPF0CMvUIjlBJKbaBansR0aBvcug.',
            '__Secure-3PSID':'BAjz3cSYRZFIVm5BspKpaIygxS9WVhNHtjIvFIHRvRN8zCcu_Kgm7e8ZdL5wiLuRT3Qc0Q.',
            '__Secure-1PAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            'SSID':'AcXUOhKFsYzuXU6bH',
            'SAPISID':'OIPHewjdJVdrllQ7/AHiVe2JdqlmSBLRau',
            'APISID':'ED3QnFAIw3lheBos/ASw10Lbh41SLEEcia',
            'NID':'221=U-0ktwHZhq5yGwplaQtAvk8XdPOrD1lK0zjUiigiDl_1qOdug3TXfxeXwXTZZXXyZKrvs5TOJQ-aho-il_f2f8rjFkpRUwZ6wdknNcB4TCUS7P5dptVq5tbUvoLtfDxcVvFLHs9lMOK0GJsWcEp04TyVY1vB2auZh3wlsaKbLGZuNF4b-woQfvBtHvpdYx8dXYTadkvRXHsjXWxbNV2b1iKc49YTcGAQXOY48gyC7TMArOU1om0',
            'OTZ':'6136180_44_44__44_',
            'SEARCH_SAMESITE':'CgQIt5MB',
            'OGPC':'19022622-1:',
            'spin':'r.1004353979_b.trunk_t.1630910225_s.1_v.2_',
            'AMCV_3FE7CBC1556605A77F000101%40AdobeOrg':'-408604571%7CMCIDTS%7C18877%7CMCMID%7C60750327677920277222135795013470136607%7CMCAAMLH-1631560871%7C6%7CMCAAMB-1631560871%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1630963271s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0%7CMCCIDH%7C776897612',
            'DSID':'AAO-7r79OFPXnoZzjqlwfKP0vKQlCLl-FfswC5zpSSvDIgfe812aipSni6ZeqridSlFMpMzfWSXOCRNw7_w9O0vDVc0vM_1-kvcmOtiyg9HeSp97ArcXAzw',
            'forterToken':'104172e3c7064f3fb3195290fb9d0b5d_1630955998293__UDF43_13ck',
            'i':'CkS7msdhU5GwBt542rJSlrcYnRktcsQk/F3HS5I2sCEC84UdA+Z+oczEFlE/P6S3alp+cpt4dJHzB2ulYmI11s6cgP0=',
            'token_v2':'CkS7msdhU5GwBt542rJSlrcYnRktcsQk/F3HS5I2sCEC84UdA+Z+oczEFlE/P6S3alp+cpt4dJHzB2ulYmI11s6cgP0=',
            'CSID':'1630961018556',
            'edgebucket':'kL0vacftZg07ke9L24',
            'm-sa':'1',
            'ymex':'1942335999.yrts.1626975999#1942335999.yrtsi.1626975999',
            'csv':'1',
            'ttwid':'1%7Cj-PzqTEHGqPlpoXWHcgWLDpRN64OBvUtZyGd1tKfFTI%7C1629789040%7C6aa1042d87055d4d4c735c9cbf5cb5a3ebe3d7cfe1de480d9079eba1583b5338',
            'tt_webid':'6995265091709257221',
            'UULE':'a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjMwOTU5NTM3ODExMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDQ5MDEwNzAKICBsb25naXR1ZGVfZTc6IDM1NzQzNDE4MAp9CnJhZGl1czogNjg4MDQ5LjEyMzE0ODI3OTUKcHJvdmVuYW5jZTogNgo=',
            'm-b': 'DLRwzEwJw-93XAVNmgiB2w==',
            'tt_webid_v2': '6995265091709257221',
            'sa-user-id': 's%3A0-6beaf630-8ff4-44bf-79a9-14f3b207428e.TzTQg%2BqTVPlL%2Fo061ENESCuEv6KASwF4TuktTj9W4mU',
            'wcs_bt': 's_4544d378d9e5:1630956080',
            'ab.storage.sessionId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1': '%7B%22g%22%3A%22b67c4e35-71d2-93cd-beca-3ef2337ec5f8%22%2C%22e%22%3A1630962819841%2C%22c%22%3A1630961019781%2C%22l%22%3A1630961019841%7D',
            '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Name%22%2C%22home%20page%22%5D%7D',
            'UID': '1KZ04REHI6JZNAIG9ZRG8Xg1626975989',
            'm-theme':'light',
            'DFID': 'web|vWa6m3WAxOr88bjpJu4L',
            'm-s': 'DHqrMJuhhZwHcRE0p8aDyA==',
            'datr': 'k8_5YIXGw51slcymiyZVSZE5',
            'm-b_strict': 'DLRwzEwJw-93XAVNmgiB2w==',
            '1P_JAR': '2021-09-06-20',
            '_sdsat_authState': 'Hard%20Logged%20In',
            'sp_adid': '31e60865-a00d-4743-8a98-732f07b0b913',
            '__gads': 'ID=b4ef282dcf9898d2:T=1630926184:S=ALNI_Ma5ADin2SG0ckI29DBEvBkA2e6Q_w',
            'schoolapi': '0d70f953-752d-4269-9595-051a894a87a2|0.962962963',
            '_gcl_au': '1.1.1093129716.1630955963',
            'recent_srs': 't5_2s5or%2Ct5_2rzac%2Ct5_33o0p%2Ct5_2qs0q%2Ct5_2sh0b%2C',
            'm-ans_frontend_early_version': 'c61d66ddc0dbe89c',
            'C': '0',
            'mcid': '60750327677920277222135795013470136607',
            'sb': 'k8_5YOpEt0zS-wbt9_fSR4KB',
            '_omappvp': 'oRfK98kKg4C1YX6w2XVwzPVtLs3t8ifOFkiiib1q5cpLoRr6lAxzt1sQC7zkBU0rp3sQSLmCDtvCyGaHR4IaueIFrBAzBn03',
            'CSessionID':'7d8258ab-4773-4851-9f8a-462168695772',
            'ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1':'ab.storage.userId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1',
            'c_user': '100003314546308',
            'reddit_session': '267079372343%2C2021-08-09T06%3A05%3A28%2C7b9a3e90aaa81ef490eef65aea66d485ed3bc9c0',
            's_pers': '%20buFirstVisit%3Dcore%7C1788722359824%3B%20gpv_v6%3Dchegg%257Cweb%257Ccore%257Chome%2520page%7C1630962818697%3B',
            'NWB': '869ffdcc5035d44df8afc392b8a76e0e.1626976002312',
            '_uetsid': '56c6ce400e3211ecb5b595448f1075ea',
            'personalization_id': '"v1_i/RVOTsFJVEB23/dN6p8Cw=="',
            'ab.storage.deviceId.b283d3f6-78a7-451c-8b93-d98cdb32f9f1': '%7B%22g%22%3A%22ddf8d7bc-ad4e-5dbb-1ffe-18dea0460625%22%2C%22c%22%3A1627566710313%2C%22l%22%3A1630961019787%7D',
            'sa-user-id-v2': 's%3A0-e94c7afb-3208-4d37-525d-2e20a38c568f%24ip%2441.90.250.60.8HHoR5yjCecbbvmYnKt5%2FCa0j0CFVOZkZG9yXiHhNk0',
            'fr': '1kaSev0CHBRNTnTX3.AWVF5jr7I4P-K4kJ02-m3jNhuVM.BhKWCX.d1.GE1.0.0.BhM9yW.',
            '_sdsat_cheggUserUUID': 'd52633e9-2a0c-4f5e-8eb2-33f9ee7ce90f',
            '_cs_c': '1',
            'everest_g_v2': 'g_surferid~YQQKCgAAARpjXRWb',
            '_ym_isad': '2',
            'chgmfatoken': '%5B%20%22account_sharing_mfa%22%20%3D%3E%201%2C%20%22user_uuid%22%20%3D%3E%20d52633e9-2a0c-4f5e-8eb2-33f9ee7ce90f%2C%20%22created_date%22%20%3D%3E%202021-09-06T19%3A20%3A11.696Z%20%5D',
            'chegg_web_cbr_id': 'a',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Sep+06+2021+23%3A43%3A40+GMT%2B0300+(East+Africa+Time)&version=6.18.0&hosts=&consentId=f8922505-d1f2-43d9-9a14-47d8a08dc8c4&interactionCount=1&landingPath=NotLandingPage&groups=snc%3A1%2Cfnc%3A1%2Cprf%3A1%2CSPD_BG%3A1%2Ctrg%3A1&AwaitingReconsent=false',
            'id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkNTI2MzNlOS0yYTBjLTRmNWUtOGViMi0zM2Y5ZWU3Y2U5MGYiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTY0NjcyNjAzOCwiaWF0IjoxNjMwOTU2MDM4LCJlbWFpbCI6ImJyaWFuc2lnaWxhaUBnbWFpbC5jb20ifQ.z1Uoub3gvoooK78WPOZl6CroJFqdOzCkJXZw7LffFp2khFX2JjyQhCCY3FO2R5KbKM30ZsX5yHO29qO7DTh9N_ZPNQGkiPJZviGnoM5ypFu4kll7pKPSPN8fpUx5NJuPfo9BcZA-5moMlwS3LAYeYNodFHjRetZbPJLRWliEh98lggFGU_eA55DcMJrUKD2CVoOSrOUA9K1tUP0eWt0scEMLs7GTT4sr8hpIOs9aRVQ37kzQkfZfb-SyslBhVEAj82_fNnJm6FJl1OHS3xowyyDEODOngFTgd3KwLWb7FGV1xW0CXHy8-kKbDN6Ah71k8WuAhkJ2zBfsAJtRurFcKA',
            'expkey': 'B247F8F59FD98EB0C310CCED4781D646',
            'AMCVS_3FE7CBC1556605A77F000101%40AdobeOrg': '1',
            'exp': 'A311C%7CA803B%7CC024A%7CA110B%7CA270C%7CA278C%7CA289D%7CA448A%7CA890H',
            'U': 'c116fc120e9eecab4da15ab627de8553',
            'PHPSESSID': 'l5ikkutofs49v8kit8b6aopc0c',
            'refresh_token': 'ext.a0.t00.v1.MQZ7E-6Gaf2nehGYE-M4sX1Sj9ut1hOYRL4V6Ev-6hE8VatIl1LQp5Objf-Iz4kSXm4lLG3zawCm7dwQdo5Q8y4',
            '_cs_s': '1.1.0.1630964632325',
            '_tq_id.TV-8145726354-1.ad8a':'201211a4f3ec55bd.1630955962.0.1630956084..',
            'usprivacy':'1YNY',
            '__ssid':'af98ff86002ce3c1065723c935e5b98',
            '_px3':'7089b2b3842cd4bd8eadaf9f17ac4914107a032108a33b52b20c8559302a7979:IsO9fOx7CHwiY0Ea8ytVnuIrBUJGT8OKQFOlJfFDY0CLmIGU6PgVQygy68WPt03uvx/BmNuc4cjhJAp87Ex/GA==:1000:7mCxcm8jB6nIUlo4Ha4YYSwZes0oZxUHCInG2874kR5gBBbc/uY+h8drr2+BvuCZjPhmfgF1H6SQUHVvP2vgV0wZy/vdeqA/Bb6cuvyszvpXKAj3BR/2MhaHpwFp2TFQmRI/sniumTq1lBt6S8KLRA5hozBZ0mJCP8Wzy9q6xZlKs57HZhaJ6LnqpQBgOITwKp/aGa+dVWkygJ5A8i1f+w==',
            'yuidss':'830883171626975999',
            '_ym_uid':'1626080555970279077',
            'V':'45580ada43818d616cdbfd1ac318c95d613669b3b9ee34.49011426',
            'IDE':'AHWqTUkVIObMudMaq7r5vzhkP4jcted8p-I0Y2kRQQxsL66kEmTyP7mRRTTvmWU2DKE',
            'CVID':'5720e230-a067-4bc2-8907-dd765f25cb1b',
            'adobeujs-optin':'%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Atrue%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Atrue%2C%22target%22%3Atrue%2C%22mediaaa%22%3Atrue%7D',
            'm-uid':'257543491',
            'CVID':'5720e230-a067-4bc2-8907-dd765f25cb1b',
            '__gads': 'ID=139c64bdfe0ff9a0:T=1630955999:S=ALNI_Maddb5ltvxxdJXiYkUxy2IeuZ3kBg',
            'm-dynamicFontSize': 'regular',
            '__CT_Data': 'gpv=2&ckp=tld&dm=chegg.com&apv_79_www33=2&cpv_79_www33=2',
            'yabs-sid': '959877401630955029',
            '_fbp': 'fb.1.1630955962519.110116082',
            'user_geo_location': '%7B%22country_iso_code%22%3A%22KE%22%2C%22country_name%22%3A%22Kenya%22%2C%22region%22%3A%2230%22%2C%22region_full%22%3A%22Nairobi+Province%22%2C%22city_name%22%3A%22Nairobi%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22sw-KE%22%5D%7D%7D',
            '_ga': 'GA1.2.1527159165.1630955962',
            'MUID': '104DFB8B2AD36B4C3103EBF72B516A5A',
            '_cs_id': '30806ee3-4b35-a5b9-b9f9-86f0dbe70958.1630956050.4.1630962832.1630962832.1.1665120050586',
            '_uetvid': '4a5bcec0bc8f11eba51331f7f26b7503',
            's_ecid':'MCMID%7C60750327677920277222135795013470136607',
            'yandexuid': '830883171626975999',
            's_sess': '%20buVisited%3Dcore%3B%20s_sq%3Dcheggincriovalidation%253D%252526pid%25253Dchegg%2525257Cweb%2525257Ccore%2525257Cauth%25252520page%252526pidt%25253D1%252526oid%25253Dfunctionlt%25252528%25252529%2525257B%2525257D%252526oidt%25253D2%252526ot%25253DBUTTON%3B%20cheggCTALink%3Dfalse%3B%20SDID%3D701E5C19597A8191-74648540C01E89DA%3B%20s_ptc%3D0.01%255E%255E0.00%255E%255E0.00%255E%255E0.00%255E%255E2.23%255E%255E0.21%255E%255E5.08%255E%255E0.11%255E%255E7.48%3B',
            '_rdt_uuid': '1630955962545.c2f746d2-5575-403a-a869-5e12134eb69a',
            '_gid': 'GA1.2.1647471338.1630955962',
            '_ym_d': '1630955962',
            'loid': '0000000000dgmlco22.2.1626982558000.Z0FBQUFBQmctY2llMmNFWEE2aDFGUW1PWVgtbTBmNnh3RnJrdFd5OXZMM0Fqd3JDUzlZbFFuS0ZuY0R6QXpwdkZJN2JrZnUwVkZCSlhVRHNDNy1VQy1NSC04akpPQk5GdGRXSzR5a0VUZExJek5EdEFNS0lUbkE3UFZtT1VTVzNZeWtSUHRxcU9BQWQ',
            'SU': 'CVB1P38f0_x7w-ThsBPFgt1XSKZXGKOh-vkoUHrtMT9vNnAzp9EVICAiAIhxWksUTUdDX7J6HpThatW-iCtk5ULvmWx0_Llv2WX9SE9bwtkywjHpCPPFbVz_tu5iTboH',
            'xs': '45%3AbZSowjfhp0oSag%3A2%3A1627394718%3A-1%3A13563%3A%3AAcW4DzZzCGzJkM0KHat6ZIN75KBDUoelz_MmH6gOHg',
            'O': '0',

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
            'https://api.telegram.org//sendDocument?chat_id=' + get_chat_id + '&caption=Here is your answer, ' + get_user_firstname + '😃',
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

    TOKEN = ""



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




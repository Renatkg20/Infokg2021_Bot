  
"""
This is a bot to show the usage of the builtin Text filter
Instead of a list, a single element can be passed to any filter, it will be treated as list with an element
"""
import sqlite3
import requests
from bs4 import BeautifulSoup
import logging
from beautifultable import BeautifulTable
from aiogram import Bot, Dispatcher, executor, types
import re


API_TOKEN = '1693059053:AAGI_mgOiIWDcV1aTzbMXU32rHN1AUSmO3M'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




def aki():
  resp = requests.get("http://www.akipress.kg")
  data = resp.text
  soup = BeautifulSoup(data, "html.parser")
  resl = soup.find('div', attrs = {"id": "covid-block"})
  resl2 = soup.find('div', attrs = {"class": "nowr_all_textbig"})
  resl1 = soup.find('div', attrs = {'class': "nowr_all_cnt"})
  return f"{resl2.text} {resl1.text} \n {resl.text.strip()}"

t = aki()
# def update_aki(user):
#     while True:
#         #user = (input("Shell we go or stop ? ")).lower()
#         if user == "go":
#             total = aki()
#         elif user == "stop":
#             break
#         else: 
#             print("Input Go or Stop")
#     return total 
# if the text from user in the list
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


res = requests.get('https://api.telegram.org/bot/sendMessage'.format(API_TOKEN), params=dict(chat_id='@Infokg2021_bot', text='Hello World!'))


# from beautifultable import BeautifulTable


def valuta_kg():
  url = "https://valuta.kg/"
  user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
  source = requests.get(url, headers=user_agent, timeout= 2.50)
  html_doc = source.text
  soup = BeautifulSoup (html_doc,'html.parser')
  soup = soup.find("div", {"class": "container"})
  t = re.sub(r'\s+', ' ', soup.get_text())
  fin4 = t.split(" ")
  tes = " ".join(fin4[7:17])
  h0=["Валюта"]
  h1=[fin4[1],fin4[17], fin4[18]]
  h2=[fin4[2],fin4[19], fin4[20]]
  h3=[fin4[3],fin4[21], fin4[22]]
  h4=[fin4[4],fin4[23], fin4[24]]
  h5=[fin4[5],fin4[25], fin4[26]]
  h6=[fin4[6],fin4[27], fin4[28]]
 
  h0.append("Покупка")
  h0.append("Продажа")

  table = BeautifulTable()
  table.column_headers = h0
  table.column_headers = h0
  table.append_row(h1)
  table.append_row(h2)
  table.append_row(h3)
  table.append_row(h4)
  table.append_row(h5)
  table.append_row(h6)
  return f"{tes} \n {table}"

print (res)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['1'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(t)

@dp.message_handler(commands=['3'])
async def send_welcome(message: types.Message):
    await message.reply(valuta_kg())


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')

def sherlock(v):
  if v == "S":
      return "He is alive!!!"
  else:
    return "fuck"

answ = "He is alive!!!"

b = sherlock("S")
#@dp.message_handler()
#async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    #await message.answer(message.text)

@dp.message_handler()
async def echo_message(msg: types.Message):
    if f"{msg.text}" == "shelock":
        await msg.reply(sherlock(msg.text()))
    else: 
        await bot.send_message(msg.from_user.id, msg.text)
    
print(valuta_kg())




def telegram_bot_sendtext(bot_message):

   bot_token = '1693059053:AAGI_mgOiIWDcV1aTzbMXU32rHN1AUSmO3M'
   bot_chatID = '535448074'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


# test = telegram_bot_sendtext("Testing Telegram bot")
for i in range(1000): 
    if i == 999:
       print(telegram_bot_sendtext("it is done"))
 

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
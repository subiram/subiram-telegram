from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import os
aio = Client('subhasree',os.getenv('subhasree'))
def turn_on_light(bot,update):
    aio.send('bedroom-light',1)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://pyxis.nymag.com/v1/imgs/fb7/8dd/9749b217b7af5e39e3e10afefeee39ab69-Lede-.rhorizontal.w700.jpg'
    bot.message.reply_text('light is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_light(bot,update):
    aio.send('bedroom-light',0)
    data = aio.receive('bedroom-light')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg'
    bot.message.reply_text('light is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_on_fan(bot,update):
    aio.send('bedroom-fan',1)
    data = aio.receive('bedroom-fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://2m23hzgu65wvnskp2u9u0f18fx-wpengine.netdna-ssl.com/power-to-help/wp-content/uploads/sites/5/2015/06/fan.jpg'
    bot.message.reply_text('fan is turned on')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def turn_off_fan(bot,update):
    aio.send('bedroom-fan',0)
    data = aio.receive('bedroom-fan')
    print(f'Received value:{data.value}')
    chat_id=bot.message.chat_id
    path='https://www.destinationlighting.com/fliptheswitch/wp-content/uploads/sites/2/2018/05/zudio-casablanca.jpg'
    bot.message.reply_text('fan is turned off')
    update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
      a = bot.message.text
      print(a)

      if a=="turn on light":
        turn_on_light(bot,update)
      elif a=="turn off light" or a=="light off":
          turn_off_light(bot,update)
      elif a=="turn on fan":
          turn_on_fan(bot,update)
      elif a=="turn off fan" or a=="fan off":
          turn_off_fan(bot,update)
      else:
            bot.message.reply_text('invalid')

BOT_TOKEN = os.getenv('BOT_TOKEN')  
u = Updater(BOT_TOKEN,use_context = True) 
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main)) 
u.start_polling()
u.idle()

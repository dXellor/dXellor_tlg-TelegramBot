import telepot
from telepot.loop import MessageLoop
import dx_tlg_module
import time

#Response_Function
def action(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	#Start
	if command == '/start':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Start())

	#Help
	if command == '/help':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Help())

	#Greetings message
	if command == '/hi':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Greetings())

	#Current time
	if command == '/time':
		telegram_bot.sendMessage(chat_id, str(dx_tlg_module.CurrentTime().hour).zfill(2)+str(":")+str(dx_tlg_module.CurrentTime().minute).zfill(2))

	#Random quote from chosen file
	if command[:6] == '/quote':
		telegram_bot.sendMessage(chat_id, str(dx_tlg_module.Quote(command[7:].upper())))

	#Insert new quote into chosen file
	if command[:9] == '/addquote':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.AddQuote(command[10:12].upper(), command[13:]))

	#Weather data for chosen city
	if command[:8] == '/weather':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Weather(command[9:]))

	#Top 5 Crypto currencies by market cap position
	if command == '/crypto':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Crypto())

	#First 2 buses that go to or from city of Novi Sad
	if command[:4] == '/bus':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Bus(command[5:].upper()))
		
	#Contact
	if command == '/contact':
		telegram_bot.sendMessage(chat_id, dx_tlg_module.Contact())

#Bot_Loop
telegram_bot = telepot.Bot('telegram_bot_api')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Running....')

while True:
	time.sleep(10)

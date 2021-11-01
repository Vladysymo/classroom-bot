from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import json

from main import get_groups

from auth_data import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
	start_buttons = ["Группы", "Видеокарты", "Гречка"]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer("Приветствуем тебя, странник. Хочешь поботать?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Группы"))
async def get_discount_sneakers(message: types.Message):
	await message.answer("Please waiting...")

	groups = get_groups(url="https://miet.ru/schedule/groups")
	card = ""
	for index, group in enumerate(groups):
		if index % 6 != 0 :
			card = card + f"{group} | "
		else:
			card = card + f"{group} \n"

	
	await message.answer(card)



@dp.message_handler()
async def echo(message: types.Message):

	await message.answer(message.text)



def main():
	print("Started bot...")
	executor.start_polling(dp)









if __name__ == '__main__':
	main()
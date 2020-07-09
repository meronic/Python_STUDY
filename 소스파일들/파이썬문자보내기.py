from twilio.rest import Client
from datetime import datetime



now = datetime.now()



account_sid = 'AC07ef7876422fa63731a175d628b7951d'
auth_token: str = '97b019f1dee46c977128c24d89b2bdf4'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="open " + str(now),
                     from_='+12073673774',
                     to='+821074857201'
                 )

print("컴퓨터의 정보를 01074857201 문자로 전송했습니다.")
print(message.sid)


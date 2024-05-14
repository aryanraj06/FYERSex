#credentials
import pyotp as tp

redirect_uri= "https://www.google.com/"  ## redircet_uri you entered while creating APP.
client_id = "QG80ZE9RYE-100"                       ## Client_id here refers to APP_ID of the created app
secret_key = "UU9VDD6SYH"
pin1 =2
pin2 = 1
pin3 = 0
pin4 = 6
user_name="XA06653"
totp_key='ECQPMB7DYPZKA4BFEQUJQQSAPXKD5JMB'
k=tp.TOTP(totp_key).now()
print(k)
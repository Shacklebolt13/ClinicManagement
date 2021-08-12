from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
def sendotp(email,otp):
    # send_mail(
    #     'Otp Verification for MyClinic',
    #     f'HI, {otp} is the OTP for your MyClinic Account.',
    #     'MyClinic@gmail.com',
    #     [email],
    #     False,
    # )
    pass


def sendConfirmation(email,text):
    # send_mail(
    #     'Otp Verification for MyClinic',
    #     f'HI, {otp} is the OTP for your MyClinic Account.',
    #     'MyClinic@gmail.com',
    #     [email],
    #     False,
    # )
    pass

def sendSMS(number,text):
    # Your Account Sid and Auth Token from twilio.com/user/account
    # account_sid = ""
    # auth_token  = ""
    # client = TwilioRestClient(account_sid, auth_token)

    # message = client.messages.create(
    #     body=text,
    #     to=str(number),
    #     from_='+919876543210',
    # )
    pass
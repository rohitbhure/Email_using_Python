import smtplib, ssl



smtp_server = "smtp.gmail.com"
port = 587
sender_email = ""
password = ""
receiver_email = ""

message= "hello"
context = ssl.create_default_context()

try:
    TIE_server = smtplib.SMTP(smtp_server, port)
    #TIE_server.ehlo()
    TIE_server.starttls(context=context)
    #server.ehlo()
    TIE_server.login(sender_email, password)
    print(f"Email sending to- {receiver_email}")
    TIE_server.sendmail(sender_email, receiver_email, message)
    print(f"Email successfully sent to- {receiver_email}")
except Exception as e:
    print(e)
finally:
    TIE_server.quit()
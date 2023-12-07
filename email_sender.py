from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'xandermaharjan@gmail.com'
email_password = 'trpxzepialvlvjay'

email_receiver = 'snehashrestha019@gmail.com'

subject = "Please comeon"
body = """If mail recieve make a program using python which sends the mail just like this!!! got it """


em = EmailMessage()
em['From'] =email_sender
em['To'] = email_receiver
em['subject'] = email_receiver
em.set_content(body)

context = ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string)


import smtplib

sender = 'your mail'
addressee = 'other mail'
msg = 'Correo enviado usando Python'

username = 'your mail'
password = '*****'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(sender, addressee msg)
server.quit()
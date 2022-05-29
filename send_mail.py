import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add="shirsatrohini66@gmail.com"
    to_add="shirsatrohi@gmail.com"
    subject="MAIL FROM PYTHON SCRIPT !"

    msg=MIMEMultipart()
    msg['from']=from_add
    msg['to']=to_add
    msg['subject']=subject

    body="<b> Hey There Sending Mail Through Python</b>"
    msg.attach(MIMEText(body,'html'))

    my_file=open(filename,'rb')
    part=MIMEBase('application','octet stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition','attachment;filename='+filename)
    msg.attach(part)
    message=msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, 'nflhxhhecdbxxcvs')
    server.sendmail(from_add, to_add, message)



    server.quit()



    #server.login(from_add,"Rohini@6698")

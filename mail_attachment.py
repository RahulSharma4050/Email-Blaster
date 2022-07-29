
from fileinput import filename
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage


e= pd.read_excel("Book2.xlsx")
emails= e['EMAIL'].values
print(emails)

try:
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("wilsonsam1458@gmail.com","sales@123")
    em= 'Paypal <ppaypal1458@gmail.com>'
    from_ = em
    to_ = emails
    message=MIMEMultipart("alternative")

    message['subject']="Payment Received!"

    
    html = '''
    
    <html>
     <head>
     <body>
     <img src ="cid : img1">

     <p>Greetings,
<br>
You have used PayPal to complete this purchase of $449.99 on CoinBase
Global for purchasing 0.0146 BTC. This transaction will reflect in your PayPal account within 48 hours.
As per your request,We are sending an invoice of $49.9 for buying more 0.00010 BTC as requested by you.
Please dial at :<a href="tel:+18018035184">+1-801-803-5184</a> for further assistance regarding this purchase. 
     <br>
     </body>
     </head>
    </html>

    '''

    fp = open ("paypalbg.jpg","rb")
    msgImage= MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID','<img1>')
    message.attach(msgImage)


    part2=MIMEText(html,"html")
    message.attach(part2)

    # filename = "img1.jpg"
    # attachment = open(filename,"rb")

    # p = MIMEBase('application','octet-stream')

    # p.set_payload((attachment).read())

    # encoders.encode_base64(p)
    # p.add_header('content-Disposition',"attachment; filename= %s" % filename) 

    # message.attach(p)
    # with open("img1.jpg","rb") as f :

    #     file_data = f.read()
    #     print("File data in binary",file_data)
    #     file_name = f.name
    #     print("File name is ",file_name)
    #     message.add_attachment(file_data,maintype="image",subtype="jpg",filename=file_name)
   
  
    server.sendmail(from_ ,to_ ,message.as_string())

    print("Message sent")
except Exception as e:
    print(e)
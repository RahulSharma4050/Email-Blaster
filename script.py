import pandas as pd
import smtplib

e= pd.read_excel("Book2.xlsx")
emails= e['EMAIL'].values


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("rs8281958@gmail.com","Rs@altaccount1234")
msg="hi"

subject="Work done hi"
body="Subject:{} \n\n {}".format(subject,msg)

for email in emails:
    server.sendmail("rs8281958@gmail.com",email,body)
    print("Sending email")
server.quit()
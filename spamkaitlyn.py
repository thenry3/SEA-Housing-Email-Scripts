import smtplib

sendTo = []
sender = "htrinh@media.ucla.edu"
password = "Trinh81439"

messageK = """Subject: hi catelin!
To: {Emailees}

hi catelin this is not henry. in fact, this email is being sent by john. u know that one guy in your fisiskz class.

also u didnt know i had this email lmaoo

much wuv,
henr- i mean jon- i mean john

PS. i hate my life ty for listening to my teD taLk

"""

sendTo.append("kaitlyn.vu07@gmail.com")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.sendmail(sender, sendTo, messageK.format(Emailees=", ".join(sendTo)))
server.quit()

import pymysql, smtplib

sendTo = []
sender = "housing.seaadmit@gmail.com"
password = "SEAhousing19"

message = """Subject: SEA Admit Host Update
To: {Emailees}
CC: seaadmit@gmail.com

Hello SEA Admit Hosts!

To start off, the SEA Admit Housing coordinators would like to personally thank each and every one of you for volunteering to host a potential Bruin for the 11th Annual SEA Admit Weekend. Without your contribution, this upcoming weekend would not have been a possibility.

We appreciate your help towards making this program a reality and would like to ask you all to consider accommodating more students during the weekend of SEA Admit. SEA Admit Housing has a shortage on the number of hosts we have so far, and consequently, limits the amount of attendees that are able to come to SEA Admit. It would be greatly appreciated if you all are able to house more students or reach out to other people who you know that can volunteer to be a host.

If you are able to host more students, please respond to this email with your name, UID number, Residential building and room number, and the total number of students you are willing to host.

Thank you all for your help!

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Trinh81439',
                             db='SEA Admit Housing',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT `Email` FROM `hosts`"
    cursor.execute(sql)
    for email in cursor.fetchall():
        sendTo.append(email['Email'])

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.sendmail(sender, sendTo, message.format(Emailees=", ".join(sendTo)))
server.quit()









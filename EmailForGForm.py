import csv, smtplib, ssl

message = """Subject: SEA ADMIT HOUSING ALERT
To: {Emailee}
CC: seaadmit@gmail.com

Hi Host UID {ID}, 

SEA Admit's Housing database has detected that you have registered to host a prospective freshman on UCLA's Reslife official host sign up form. However, you have not filled out SEA Admit Housing's Host/Hostee matching form. Please continue to do so as soon as possible by clicking on this link:
https://goo.gl/89W547  
 
Thank you

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

from_address = "housing.seaadmit@gmail.com"
password = "SEAhousing19"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(from_address, password)
with open("/Users/henrytrinh/Downloads/EmailForGForm.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for ID, email in reader:
        server.sendmail(from_address, email, message.format(ID=ID, Emailee=email))
server.quit()
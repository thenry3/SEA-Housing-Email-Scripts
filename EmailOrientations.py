import pymysql
import smtplib

sendTo = []
sender = "housing.seaadmit@gmail.com"
password = "SEAhousing19"

# THE FOLLOWING MESSAGE STRINGS ARE EMAILS FOR SPECIFIC DAYS ------------------------------------------

# Orientation Dates-----------------
mondayDate = """ResLife Orientation
When: Monday, April 8, 6:30-7:45pm
Where: Northwest Auditorium

SEA Admit Orientation
When: Monday April 8, 7:45-8:15pm
Where: Carnesale Hermosa B"""

tuesdayDate = """ResLife Orientation
When: Tuesday, April 9, 6:30-7:45pm
Where: Northwest Auditorium

SEA Admit Orientation
When: Tuesday April 9, 7:45-8:15pm
Where: Covel Westcoast"""

thursdayDate = """ResLife Orientation
When: Thursday, April 4, 6:30-7:45pm
Where: Northwest Auditorium

SEA Admit Orientation
When: Thursday April 4, 7:45-8:15pm
Where: De Neve Sycamore"""

emergencyDate = """Bruin Overnight Training
When: Wednesday April 10, 7:00-8:00pm
Where: Carnesale Hermosa AB"""

#----------------------------------------------------------------

messageConfirmation = """Subject:   
To : {Emailees}
CC: seaadmit@gmail.com

Hello,

Thank you so much for signing up to be a host for Southeast Asian Admit Weekend! This is just a reminder that you have signed up to attend a ResLife host orientation to go over safety, rules, your responsibilities, and general information regarding the weekend. SEA Admit will present a brief and REQUIRED orientation immediately afterwards. You, as a host, must attend both the orientation sessions but your roommates do not need to. ResLife will not allow you to host a student if you do not attend the meeting. Also note that you must check in with both SEA Admit and Reslife at the orientation. 

{Date}

Please let us know if you have any questions or concerns, and we will see you at the meeting. Thank you so much for hosting!

Best,

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

messageExtraOrientation = """Subject: [SEA ADMIT HOUSING] Make-up Orientation
To: {Emailees}
CC: seaadmit@gmail.com

Hello, 

Thank you so much for signing up to be a host for Southeast Asian Admit Weekend. You are receiving this email because you have indicated that you are absolutely not able to make any of the regular orientation times. As per Reslife's regulations, you would not be able to host without attending a hosting orientation. Luckily however, you are able to attend a make-up orientation to host a new Bruin:

{Date}

Please let us know if you have any questions or concerns. We hope you are able to make it to this make-up orientation.

Best,

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

# ----------------------------------------------------------------------------------------------------

messageOrientationReminder = """Subject: [SEA ADMIT HOUSING] Reminder: Host Orientation TOMORROW
To: {Emailees}
CC: seaadmit@gmail.com

Hello amazing hosts!

SEA Admit Housing would like to thank you all for signing up to be a host for the Southeast Asian Admit Weekend. We are sending this email to remind to you all that the orientation you have signed up for is tomorrow:

{Date}

Be sure to come to orientation- Reslife will not allow anyone to host any students without coming to orientation.  At orientation, Reslife will be going over safety, rules, your responsibilities, and general information on hosting. SEA Admit Housing will also have another brief orientation pertaining to the specific schedule of SEA Admit. 

Please do not hesitate to let us know of any questions or concerns you might have relating to host orientations or leading up to SEA Admit Weekend. We will see you all at orientation tomorrow, and once again, SEA Admit Housing is grateful for your contributions as a host.

Best, 


-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

messagePostOrientation = """Subject: [SEA ADMIT HOUSING] Housing Orientation Recap
To: {Emailees}
CC: seaadmit@gmail.com

Hello everyone!

Thank you so much for attending our host orientations! If you have not yet attended an orientation, you should have already received an email from us. If you have not attended a host orientation yet and have not received an email from us, please reply to this email and let us know. As a reminder, ResLife will NOT allow you to host a student if you have not attended one of the host orientations. 

Below is a link to a document that details the SEA Admit weekend hosting agenda. Thank you once again for hosting for SEA Admit, and we look forward to a great weekend! As always, please send us an email if you have any questions or concerns! 

IMPORTANT: If you are receiving this email, but you are unable to host, please reply to us and let us know, even if you had previously already contacted us about it. 

Link to the weekend agenda document:
https://docs.google.com/document/d/1w5-3zrWC7B2vHE6YAfUgLdZ_JhSTbk0TZDOghIAk89o/edit?usp=sharing

Best,

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

messageAlumniChange = """Subject: [SEA ADMIT HOUSING] Host Reminder
To: {Emailees}
CC: seaadmit@gmail.com

Hello amazing hosts!

We are emailing you this, as well as reminding you all on Groupme, to remind you all that you must be available at 6:00 pm today, 4/12, to let your hostees in your dorms to change for about half an hour. Thank you all so much for your contributions to SEA Admit, and have a great afternoon!

Best,

-- 
SEA Admit Housing Coordinators | Henry Trinh, Anthony Le, Jannelle Dang
Southeast Asian Admit Weekend 2019
University of California, Los Angeles
Website: www.seaadmit.com"""

# -----------------------------------------------------------------------------------

connection = pymysql.connect(host="localhost",
                             user="root",
                             password="Trinh81439",
                             db="SEA Admit Housing",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT Email FROM `hosts`"
    cursor.execute(sql)
    for email in cursor.fetchall():
        sendTo.append(email['Email'])

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.sendmail(sender, sendTo, messageAlumniChang\.format(Emailees=", ".join(sendTo)))
server.quit()

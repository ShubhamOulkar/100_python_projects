# import smtplib
#
# my_email = 
# password = 
#
# import datetime as dt
#
# current_date_time = dt.datetime.now()
# # print(current_date_time)
# # year = current_date_time.year
# # print(year)
# # month = current_date_time.month
# # print(month)
# day = current_date_time.day
# #print(day)
# # day_in_week = current_date_time.weekday()
# # print(day_in_week)
# #
# # date_of_birth = dt.datetime(year=1995 , month=12 , day= 15, hour=4, minute=50, second=15)
# # print(date_of_birth)
#
# date = 12
#
# if  day == date:
#     with smtplib.SMTP('smtp.gmail.com') as new_connections:
#         new_connections.starttls()
#         new_connections.login(user=my_email, password=password)
#         new_connections.sendmail(from_addr=my_email,
#                                  to_addrs='oulkarsukhada@gmail.com',
#                                  msg='Subject:hi\n\n System send this mail.')
#
#

##################### Extra Hard Starting Project ######################
import pandas as pd
import  datetime as dt
import random
import smtplib
# 2. Check if today matches a birthday in the birthdays.

my_email = 'oulkarshubhu@gmail.com'
password = 'userAPPpasswordfromEmaliHost'


birthday = pd.read_csv('birthdays.csv')
birthday = birthday.to_dict(orient='records')
current_datetime = dt.datetime.now()
month = current_datetime.month
day = current_datetime.day

for dict in birthday:
    if month == dict['month'] and day == dict['day']:
        name = dict['name']
        letter_no = random.randint(1,3)

        with open(f"letter_templates/letter_{letter_no}.txt", "r") as file:
            msg = file.read()

            msg = msg.replace('[NAME]', name)

        with open(f'send_msg_{name}.txt', 'w') as file:
            file.write(msg)

        with smtplib.SMTP('smtp.gmail.com') as new_connections:
             new_connections.starttls()
             new_connections.login(user=my_email, password=password)
             new_connections.sendmail(from_addr=my_email,
                                      to_addrs=dict['email'],
                                      msg= f"Subject: Birthday wish\n\n{msg}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email addres

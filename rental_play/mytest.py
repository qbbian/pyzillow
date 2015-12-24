from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
import datetime
import numpy as np
import pandas as pd

# Gmail module courtesy of Kutuma's blog
# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "john.doe@gmail.com"
gmail_pwd = "justletmein"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

filename = 'zillow_rent_estimate.csv'
col_names = ['Date', 'Property', 'Rent Estimate']
todays_date = datetime.datetime.now().date()

try:
    rent_estimate_pd = pd.read_csv(filename)
except:
    rent_estimate_pd = pd.DataFrame(columns = col_names)

MY_ZILLOW_API_KEY = 'X1-ZWz1ezldubt8uj_376md'

addressList = [('14825 NW Fawnlily Dr', '97229'),
    ('606 NW Naito Parkway, Unit A8', '97209'),
    ('11080 SW Oneida Street', '97062')]

zillow_data = ZillowWrapper(MY_ZILLOW_API_KEY)
for address in addressList:
    street = address[0]
    zipcode = address[1]
    deep_search_response = zillow_data.get_deep_search_results(street, zipcode, True)
    result = GetDeepSearchResults(deep_search_response)
    print "Estimated monthy rent for %s is $%s" % (address, result.rentzestimate_amount)
    rent_estimate_pd.loc[len(rent_estimate_pd) + 1] = np.array([todays_date, address, result.rentzestimate_amount])

rent_estimate_pd.to_csv(filename, index=False)
mail("qbbian@gmail.com",
    "Hello from python!",
    "This is a email sent with python",
    filename)

from django.contrib.auth.decorators import login_required
import pandas as pd
from django.core.mail import send_mail
from rest_framework.response import Response



location = "D:\document\email_sample.csv"


# @login_required
def email_sender(request):
    email_from = request.user
    df = pd.read_csv(location)

    for index, row in df.iterrows():
        try:
            email = row['email']
            subject = row['subject']
            message = row['message']
            send_mail(subject, message, email_from, email)
        except KeyError as e:
            return Response("Missing expected column in CSV file: %s", e)
        except Exception as e:
            return Response("Error sending email to %s: %s", email, e)

    return Response("Emails have been sent successfully.")



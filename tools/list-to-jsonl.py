import json
import random

def main():
    lists = open('input.txt', 'r')
    jsonl = open('emails.jsonl', 'w')
    json_string = ""

    for jlist in lists:
        jlist = jlist.strip('\n')
        json_string = json_string + "{\"id\":\"" + str(random.randint(300, 1000000)) + "\",\"email\":\"" + str(jlist) + "\",\" name\":\"<Victim Organisation [Optional]>\",\"person\":\"{\\\"lastName\\\": \\\"[Optional]\\\", \\\"firstName\\\": \\\"[Optional]\\\", \\\"middleName\\\": \\\"[Optional]\\\"}\"}"
        json_string = json_string + "\n"
    jsonl.write(json_string)

if __name__ == "__main__":
    main()
import seoultech_notice_crawler as snc
import csv

with open("notices.csv", "w") as file:
    notices = snc.seoultech_notice_crawling()
    for notice in notices:
        title, date = notice
        file.write("%s, %s\n % (title, date, ))

with open("notices.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
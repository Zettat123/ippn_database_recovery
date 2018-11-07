import re
import os

# [Jan 07 2016 02:51:00]
time_pattern = '\[[A-Za-z]{3}\s[0-9]{2}\s[0-9]{4}\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]'

with open('./recovery_tbl_patients_peritonitis.sql', mode='w+', encoding='utf-8') as sql_file:
    log_files = os.listdir('./logs')
    for lf in log_files:
        with open('./logs/'+lf, mode='r', encoding='utf-8') as log_file:
            print("current log is: "+lf)
            current_line = log_file.readline()
            while True:
                next_line = log_file.readline()
                while re.match(time_pattern, next_line[:22]) is None:
                    current_line = current_line + next_line
                    next_line = log_file.readline()
                    if next_line == '':
                        break
                # print(re.sub(time_pattern, "", current_line))
                if re.search('tbl_patients_peritonitis', current_line) is not None \
                        and re.search("INSERT INTO",current_line) is None \
                        and re.search("cdate=''", current_line) is None:
                    current_line = re.sub(time_pattern, "", current_line)
                    current_line = re.sub(";[0-9]*;", "", current_line, 1)
                    sql_file.write(current_line + ';')
                if next_line == '':
                    break
                current_line = next_line







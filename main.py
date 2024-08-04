import os
from getDataFrame import getData
from utilityFunction import getFileName
from htmlTemplate import pre,post,my_frnd_msg,my_msg

chat_file_name = getFileName()
if chat_file_name == "end":
    exit()

df = getData(chat_file_name)
user_list = list(df['user'].unique())
user_list.remove('group_notification')

html_code = ''
html_code +=pre


for row in df.itertuples():
    if row.user == 'group_notification':
        continue
    if row.user==user_list[0]:
        html_code += my_msg(row.message, row.user, row.date)
    else:
        html_code += my_frnd_msg(row.message, row.user, row.date)

html_code += post

file_path = f"./output/{user_list[0]}_and_{user_list[1]}.html"

# Open the file in write mode and write the HTML code
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_code)

print(f"HTML code has been saved to '{file_path}'")

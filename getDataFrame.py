import pandas as pd
import re

def getData(file_path):

    # Read the text file in binary mode
    with open(file_path, 'rb') as file:
        byte_data = file.read() # Read the contents of the file into a bytes object

    # Now byte_data contains the contents of the text file in bytes format
    # Convert bytes data to string using UTF-8 decoding
    data = byte_data.decode('utf-8')

    pattern = r"\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}\s(?:am|pm)"
    messages = re.split(pattern, data)[1:]

    # if data in 24 format
    if not messages:
        pattern = r"\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}"
        messages = re.split(pattern, data)[1:]
        dates = re.findall(pattern, data)
        df = pd.DataFrame({'user_msg': messages, 'msg_dates': dates})
        df['msg_dates'] = pd.to_datetime(df['msg_dates'], format='%m/%d/%y, %H:%M')
    else:
        dates = re.findall(pattern, data)
        df = pd.DataFrame({'user_msg': messages, 'msg_dates': dates})
        df['msg_dates'] = pd.to_datetime(df['msg_dates'], format='%d/%m/%Y, %I:%M %p').dt.strftime('%d-%m-%Y %H:%M:%S')
        df['msg_dates'] = pd.to_datetime(df['msg_dates'], format='%d-%m-%Y %H:%M:%S')
    df.rename(columns={'msg_dates': 'date'}, inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    users = []
    messages = []
    for i in df['user_msg']:
        entry = re.split('([\w\W]+?):\s', i[3:])  # [3:] is for removing ' - '
        if (len(entry) > 1):
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_msg'], inplace=True)

    return df
# Dealing with nested dictionaries

number_of_sessions = 0
total_session_time = 0
avg_session_time = 0

total_dict = {}

user_dict = {}

stream_dict = {'session1': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 24, 'session_end': 44}},
'session2': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'session_start': 30, 'session_end': 70}},
'session3': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'session_start': 4, 'session_end': 9}},
'session4': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 40, 'session_end': 45}},
'session5': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session6': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'session_start': 11, 'session_end': 13}},
'session7': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 28, 'session_end': 40}},
'session8': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session9': {'name': 'Ian Peck', 'userid':'apeck14', 'sessioninfo': {'session_start': 20, 'session_end': 23}},
'session10': {'name': 'Ethan Peck', 'userid':'ethpeck','sessioninfo': {'session_start': 20, 'session_end': 40}},
'session11': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session12': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session13': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 80, 'session_end': 100}},
'session14': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 11, 'session_end': 12}},
'session15': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session16': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 13, 'session_end': 17}},
'session17': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 30}},
'session18': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'session_start': 10, 'session_end': 15}},
'session19': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 9, 'session_end': 42}},
'session20': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'session_start': 16, 'session_end': 40}},
'session21': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session22': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'session_start': 240, 'session_end': 400}},
'session23': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'session_start': 12, 'session_end': 90}},
'session24': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session25': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'session_start': 1, 'session_end': 12}},
'session26': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 20, 'session_end': 40}},
'session27': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'session_start': 5, 'session_end': 7}},
'session28': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'session_start': 12, 'session_end': 40}},
'session29': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'session_start': 100, 'session_end': 300}}}


def find_summed_info(dict):
    global number_of_sessions
    global total_session_time
    global avg_session_time
    number_of_sessions = len(list(dict.keys()))
    for v in dict.values():
        indv_session_time = v['sessioninfo']['session_end'] - v['sessioninfo']['session_start']
        total_session_time += indv_session_time
    avg_session_time = total_session_time / number_of_sessions

def create_nested_dict(dict):
    global user_dict
    user_list = []
    for v in dict.values():
        if v['userid'] not in user_list:
            user_list.append(v['userid'])
    for user in user_list:
        user_dict[user] = {}
        user_dict[user]['numberofsessions'] = 0
        user_dict[user]['totalsessiontime'] = 0
        user_dict[user]['avgsessiontime'] = 0

def user_stats(dict):
    global user_dict
    for v in stream_dict.values():
        user_dict[v['userid']]['numberofsessions'] += 1
        indv_session_time = v['sessioninfo']['session_end'] - v['sessioninfo']['session_start']
        user_dict[v['userid']]['totalsessiontime'] += indv_session_time
    
    for v in user_dict.values():
        v['avgsessiontime'] = v['totalsessiontime'] / v['numberofsessions']



find_summed_info(stream_dict)

print(number_of_sessions)

print(total_session_time)

print(avg_session_time)

total_dict['avg_session_time'] = avg_session_time
total_dict['number_of_sessions'] = number_of_sessions
total_dict['total_session_time'] = total_session_time

print(total_dict)

create_nested_dict(stream_dict)

user_stats(stream_dict)

print(user_dict)



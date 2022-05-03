session_data = {
'session1': {
    'name': 'Ian Peck', 'userid':'ianpeck22',
    'sessioninfo': {'step': 1, 'timestamp': '2020-01-01 00:00:00'}
    },
'session2': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'step': 1, 'timestamp': '2020-01-01 00:00:00'}},
'session3': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'step': 1, 'timestamp': '2020-01-01 00:00:10'}},
'session7': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'step': 4, 'timestamp': '2020-01-01 00:00:58'}},
'session4': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'step': 2, 'timestamp': '2020-01-01 00:00:20'}},
'session5': {'name': 'Ian Peck', 'userid':'ianpeck22', 'sessioninfo': {'step': 3, 'timestamp': '2020-01-01 00:00:30'}},
'session6': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'step': 1, 'timestamp': '2020-01-01 00:00:40'}},
'session8': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'step': 2, 'timestamp': '2020-01-01 00:01:58'}},
'session9': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'step': 3, 'timestamp': '2020-01-01 00:02:00'}},
'session10': {'name': 'Ethan Peck', 'userid':'ethpeck','sessioninfo': {'step': 2, 'timestamp': '2020-01-01 00:02:20'}},
'session11': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'step': 3, 'timestamp': '2020-01-01 00:02:30'}},
'session12': {'name': 'Tina Peck', 'userid':'tpeck13', 'sessioninfo': {'step': 4, 'timestamp': '2020-01-01 00:02:35'}},
'session13': {'name': 'Ethan Peck', 'userid':'ethpeck', 'sessioninfo': {'step': 4, 'timestamp': '2020-01-01 00:02:40'}},
'session14': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'step': 2, 'timestamp': '2020-01-01 00:02:40'}},
'session15': {'name': 'Aaron Peck', 'userid':'apeck14', 'sessioninfo': {'step': 3, 'timestamp': '2020-01-01 00:02:55'}}
}

# Loop through the dictionary and 

agg_dict = {}
final_dict = {}

def agg_data(my_dict):
    global agg_dict
    global final_dict
    # Loop through dictionary for data
    for v in my_dict.values():
        if v['userid'] not in agg_dict:
            agg_dict[v['userid']] = []
        agg_dict[v['userid']].append((v['sessioninfo']['timestamp'],v['sessioninfo']['step']))

    final_dict = {1: [], 2: [], 3: []}

    for v in agg_dict.values():
        v.sort(key=lambda tup: tup[1])
        for i in range(len(v)):
            if i != len(v)-1:
                final_dict[i+1].append(v[i+1][1]-v[i][1])


    return final_dict
        

print(agg_data(session_data))

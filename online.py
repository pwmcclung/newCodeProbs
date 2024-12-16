def who_is_online(friends):
    online = []
    away = []
    offline = []

    if not friends:
        return {}

    for friend in friends:
        if friend['status'] == 'online':
            if friend['last_activity'] <= 10:
                online.append(friend['username'])
            else:
                away.append(friend['username'])
        else:
            offline.append(friend['username'])

    result = {}
    if online:
        result['online'] = online
    if away:
        result['away'] = away
    if offline:
        result['offline'] = offline

    return result
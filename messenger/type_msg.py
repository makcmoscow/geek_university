from time import ctime


def f_presence():
    presence = {
        'action': 'presence',
        'time': ctime(),
        'type': 'status',
        'user': {
            'account_name': 'CodeMaverick',
            'status': 'Да, я здесь!'
        }
    }
    return presence

def f_auth():
    auth_message = {
        'action': 'authenticate',
        'time': ctime(),
        'user': {
            'account_name': 'CodeMaverick',
            'password': 'CorrectHorseBatteryStaple'
        }
    }
    return auth_message

def f_msg():
    msg = {
        'action': 'msg',
        'time': ctime(),
        'to': 'account_name',
        'from': 'account_name',
        'encoding': 'utf-8',
        'message': 'message'
    }
    return msg

def f_join():
    join_chat = {
        'action': 'join',
        'time': ctime(),
        'room': '#room_name'
    }
    return join_chat

def f_leave():
    leave_chat = {
        'action': 'leave',
        'time': ctime(),
        'room': '#room_name'
    }
    return leave_chat

def f_quit():
    quit = {
        'action': 'quit'
    }
    return quit

def f_probe():
    probe = {
        'action': 'probe',
        'time': ctime()
    }
    return probe

def f_alert(number, text):
    alert = {
        'response': number,
        'time': ctime(),
        'alert': text
    }
    return alert

def f_error(number, text):
    error = {
        'response': number,
        'time': ctime(),
        'error': text
    }
    return error


code = {
    '100': 'based notification',
    '101': 'important notice',
    '200': 'OK',
    '201': 'created',
    '202': 'accepted',

    '400': 'incorrect json object',
    '401': 'not authorized',
    '402': 'incorrect login or password',
    '403': 'user forbidden',
    '404': 'user or chat not found in server',
    '409': 'conflict! login is already in use',
    '410': 'user offline',
    '500': 'server error'
}

a = '200'
a = f_alert(a, code[a])
print(a)
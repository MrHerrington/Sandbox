def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}

print(make_user(4, False, None))

def test(cmds, n):
    contact_dict = dict()
    for cmd in cmds:
        op, contact = cmd.strip().split(' ')
        if op == 'add':
            for i in range(1, len(contact) + 1):
                key = contact[0:i]
                if key in contact_dict:
                    contact_dict[key].append(contact)
                else:
                    contact_dict[key] = [contact]

        if op == 'find':
            count = 0
            if contact in contact_dict:
                count = len(contact_dict[contact])
            print(str(count))


cmds = ['add hack',
        'add hackerrank',
        'find hac',
        'find hak']
test(cmds, len(cmds))

import os
import sys
import pathlib

def get_system_users():
    """
    Retrieve system users from /etc/passwd file.
    Returns a list of dictionaries containing user information.

    Returns:
        list: List of dictionaries with keys:
            - username: User's login name
            - uid: User ID
            - gid: Group ID
            - comment: Full name or comment
            - home: Home directory
            - shell: Login shell
    """
    users = []

    try:
        with open('/etc/passwd', 'r') as passwd_file:
            for line in passwd_file:
                if line.strip():
                    # Split the line into fields
                    fields = line.strip().split(':')

                    if len(fields) >= 7:
                        user_info = {
                            'username': fields[0],
                            'uid': int(fields[2]),
                            'gid': int(fields[3]),
                        }
                        if int(fields[2]) < 1000:
                            continue
                        users.append(user_info)

    except (IOError, PermissionError) as e:
        print(f"Error reading /etc/passwd: {e}")
        return []

    return users

def get_users_in_group(group_name: str) -> list[str]:
    """
    Retrieve users in a specific group.

    Args:
        group_name (str): The name of the group to search for

    Returns:
        list: List of usernames in the specified group
    """
    users = []

    try:
        with open('/etc/group', 'r') as group_file:
            for line in group_file:
                if line.strip():
                    # Split the line into fields
                    fields = line.strip().split(':')

                    if len(fields) >= 4:
                        if fields[0] == group_name:
                            users = fields[3].split(',')

    except (IOError, PermissionError) as e:
        print(f"Error reading /etc/group: {e}")
        return []

    return users

def append_to_file(file: str, line: str) -> None:
    """
    Append a line to a file.

    Args:
        file (str): The path to the file
        line (str): The line to append
    """
    with open(file, 'a') as f:
        f.write(f'{line}\n')

def main() -> int:
    users = get_system_users()
    sudo_users = get_users_in_group('sudo')

    allowed_users = pathlib.Path('files/regular_users.txt').read_text().splitlines()
    allowed_users = [user.strip() for user in allowed_users]
    unallowed_users = [user for user in users if user['username'] not in allowed_users]

    allowed_sudo_users = pathlib.Path('files/sudo_users.txt').read_text().splitlines()
    allowed_sudo_users = [user.strip() for user in allowed_sudo_users]
    unallowed_sudo_users = [user for user in sudo_users if user not in allowed_sudo_users]

    if unallowed_sudo_users:
        for user in unallowed_sudo_users:
            print(f"Unauthorized administrator: {user}")

    if unallowed_users:
        for user in unallowed_users:
            print(f"Unauthorized user: {user['username']}")

    os.system('ufw allow in on lo')
    os.system('ufw allow out on lo')
    os.system('ufw deny in from 127.0.0.0/8')
    os.system('ufw deny in from ::1')
    os.system('ufw allow out on all')

    users = get_system_users()

    for user in users:
        os.system(f'chage -m 3 -M 60 -W 7 {user["username"]}')
        os.system(f'echo "{user["username"]}:thisisapassword123" | chpasswd')

    print('do login.defs max ages')
    print('check apt sources')
    print('check sudoers')
    print('check services')
    print('check cron jobs')
    print('check packages')
    print('check ps aux')
    print('enable auto updates')
    print('run through CIS benchmarks chapter 5.3')
    print('check permissions on ssh keys')
    print('check on /etc/passwd to ensure no passwords are stored')

    return 0

if __name__ == '__main__':
    sys.exit(main())

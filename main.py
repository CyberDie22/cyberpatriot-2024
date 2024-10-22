import sys
import os
import re
import subprocess
from tabnanny import check
from typing import Literal

OS = Literal['windows', 'linux']

def detect_os() -> OS:
    if sys.platform == 'win32':
        return 'windows'
    elif sys.platform == 'linux':
        return 'linux'
    else:
        raise NotImplementedError(f'Unsupported platform: {sys.platform}')

def detect_os_version(operating_system: OS) -> str:
    if operating_system == 'windows':
        return str(sys.getwindowsversion().major)
    elif operating_system == 'linux':
        with open('/etc/os-release') as f:
            for line in f:
                if line.startswith('VERSION_ID='):
                    return line.split('=')[1].strip().strip('"')

    return 'unknown'

def detect_distros(operating_system: OS) -> list[str]:
    if operating_system == 'windows':
        return ['Windows']
    elif operating_system == 'linux':
        with open('/etc/os-release') as f:
            distros = []
            for line in f:
                if line.startswith('ID='):
                    distros += [line.split('=')[1].strip().strip('"')]
                if line.startswith('ID_LIKE='):
                    distros += line.split('=')[1].strip().strip('"').split(' ')
            return distros

    return ['unknown']

user_password = "verysecurepassword123"

available_distros = {
    'ubuntu': [
        {'name': 'Disable aliases in .bashrc', 'task_type': 'file_append', 'file': '/home/__user__/.bashrc', 'iter': 'real_user', 'content': '\nunalias -a\n'},
        {'name': 'Disable aliases in /root/.bashrc', 'task_type': 'file_append', 'file': '/root/.bashrc', 'content': '\nunalias -a\n'},
        {'name': 'Disable aliases in /etc/profile', 'task_type': 'file_append', 'file': '/etc/profile', 'content': '\nunalias -a\n'},
        {'name': 'Disable aliases in /etc/bash.bashrc', 'task_type': 'file_append', 'file': '/etc/bash.bashrc', 'content': '\nunalias -a\n'},
        {'name': 'Update root password', 'task_type': 'command', 'command': 'echo "root:__user_password__" | chpasswd', 'vars': ['user_password']},
        {'name': 'Update all users password', 'task_type': 'command', 'command': 'echo "__user__:__user_password__" | chpasswd', 'vars': ['user_password'], 'iter': 'real_user'},
        {'name': 'Replace /etc/ssh/sshd_config with known good config', 'task_type': 'file_replace', 'file': '/etc/ssh/sshd_config', 'replace': 'files/sshd_config'},
    ]
}

def execute_command_with_output(command: str) -> (int, str):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.returncode



def execute_command_task(task: dict) -> None:
    command = task['command']

    print(f'Running command: {command}')
    output, return_code = execute_command_with_output(command)
    print(f'Output ({return_code}): {output}')

def standard_file_checks(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f'File {file_path} does not exist, skipping task')
        return False

    if not os.path.isfile(file_path):
        print(f'Path {file_path} is not a file, skipping task')
        return False

    if not os.access(file_path, os.W_OK):
        print(f'File {file_path} is not writable, skipping task')
        return False

    return True

def execute_file_content_replace_task(task: dict) -> None:
    file_path = task['file']

    if not standard_file_checks(file_path):
        return

    with open(file_path) as f:
        content = f.read()

    if 'regex' in task:
        regex = task['regex'][0]
        flags = 0
        if 'multiline' in task['regex'][1]:
            flags |= re.MULTILINE
        content = re.sub(regex, task['replace'], content, flags=flags)

    with open(file_path, 'w') as f:
        f.write(content)

def execute_file_append_task(task: dict) -> None:
    file_path = task['file']

    if not standard_file_checks(file_path):
        return

    with open(file_path, 'a') as f:
        f.write(task['content'])

def execute_file_replace_task(task: dict) -> None:
    file_path = task['file']
    replace_file_path = task['replace']

    if not standard_file_checks(file_path) or not os.path.exists(replace_file_path):
        return

    # Backup original file
    with open(file_path, 'r') as f:
        original_content = f.read()

    with open('modified_files/' + file_path, 'w') as f:
        f.write(original_content)

    # Replace file with new content
    with open(replace_file_path, 'r') as f:
        replace_content = f.read()

    with open(file_path, 'w') as f:
        f.write(replace_content)

def execute_create_file_task(task: dict) -> None:
    file_path = task['file']
    content = task['content']

    if os.path.exists(file_path):
        print(f'File {file_path} already exists, skipping task')
        return

    with open(file_path, 'w') as f:
        f.write(content)

def execute_load_kernel_module_task(task: dict) -> None:
    module = task['module']

    print(f'Loading kernel module: {module}')
    output, return_code = execute_command_with_output(f'modprobe {module}')
    print(f'Output ({return_code}): {output}')

def execute_unload_kernel_module_task(task: dict) -> None:
    module = task['module']

    print(f'Unloading kernel module: {module}')
    output, return_code = execute_command_with_output(f'modprobe -r {module}')
    print(f'Output ({return_code}): {output}')

available_tasks = {
    'command': { 'function': execute_command_task, 'primary_key': 'command' },
    'file_content_replace': { 'function': execute_file_content_replace_task, 'primary_key': 'file' },
    'file_append': { 'function': execute_file_append_task, 'primary_key': 'file' },
    'file_replace': { 'function': execute_file_replace_task, 'primary_key': 'file' },
    'create_file': { 'function': execute_create_file_task, 'primary_key': 'file' },
    'load_kernel_module': { 'function': execute_load_kernel_module_task, 'primary_key': 'module' },
    'unload_kernel_module': { 'function': execute_unload_kernel_module_task, 'primary_key': 'module' },
}

def check_return_code(command: str, expected_return_code: int) -> bool:
    output, return_code = execute_command_with_output(command)
    return return_code == expected_return_code

def check_file_exists(task: dict) -> bool:
    return os.path.exists(task['file'])

def check_kernel_module_loaded(task: dict) -> bool:
    return check_return_code(f'lsmod | grep -wq "{task["module"]}"', 0)

def check_kernel_module_exists(task: dict) -> bool:
    return check_return_code(f'modinfo {task["module"]}', 0)

def chcek_kernel_module_loadable(task: dict) -> bool:
    return check_return_code(f'modprobe --dry-run {task["module"]}', 0)

def check_file_content(task: dict) -> bool:
    with open(task['file']) as f:
        content = f.read()

    return re.search(task['regex'], content) is not None

conditional_tasks = {  # TODO: implement conditional tasks
    'check_file_exists': check_file_exists,
    'check_kernel_module_loaded': check_kernel_module_loaded,
    'check_kernel_module_exists': check_kernel_module_exists,
    'chcek_kernel_module_loadable': chcek_kernel_module_loadable,
    'check_file_content': check_file_content
}

def get_user_iter_values() -> list[str]:
    with open('/etc/passwd') as f:
        return [line.split(':')[0] for line in f]

def get_real_user_iter_values() -> list[str]:
    with open('/etc/passwd') as f:
        return [line.split(':')[0] for line in f if 1000 <= int(line.split(':')[2]) <= 60000]

available_iter_types = {
    'user': { 'function': get_user_iter_values, 'replace_var': 'user' },
    'real_user': { 'function': get_real_user_iter_values, 'replace_var': 'user' }
}

def execute_task(task: dict) -> None:
    task_name = task['name']
    task_type = task['task_type']

    print(f'Executing task {task_name} of type {task_type}')

    if task_type not in available_tasks:
        print(f'Task type {task_type} ({task["name"]}) is not supported, skipping task')
        return

    task_info = available_tasks[task_type]
    primary_key = task_info['primary_key']

    primary_key_value = task[primary_key]

    if 'vars' in task:
        for var in task['vars']:
            print(f'Processing var {var}, value: {globals()[var]}')
            primary_key_value = primary_key_value.replace(f'__{var}__', globals()[var])
        task[primary_key] = primary_key_value

    primary_key_value = task[primary_key]

    if 'iter' in task:
        iter_type = task['iter']

        if iter_type not in available_iter_types:
            print(f'Iter type {iter_type} ({task["name"]}) is not supported, skipping task')
            return

        iter_info = available_iter_types[iter_type]
        iter_values = iter_info['function']()
        for iter_value in iter_values:
            new_primary_key_value = primary_key_value.replace(f'__{iter_info["replace_var"]}__', iter_value)
            new_task = task.copy()
            new_task[primary_key] = new_primary_key_value
            task_info['function'](new_task)
    else:
        task_info['function'](task)

def main() -> int:
    operating_system = detect_os()
    os_version = detect_os_version(operating_system)
    distros = detect_distros(operating_system)

    print(f'Operating System: {operating_system} {distros} {os_version}')

    distros_to_process = distros.copy()
    distros_to_process.reverse()

    for distro in distros_to_process:
        if distro in available_distros:
            for task in available_distros[distro]:
                execute_task(task)
        else:
            print(f'Distro {distro} is not supported')

    return 0

if __name__ == '__main__':
    sys.exit(main())

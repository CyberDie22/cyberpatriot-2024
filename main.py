import json
import pathlib
import sys
import importlib
import importlib.util
import os
import re
import subprocess
from tabnanny import check
from types import ModuleType
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


def import_string_as_module(code_string: str, module_name: str) -> ModuleType:
    """
    Import a string containing Python code as a module.

    Args:
        code_string (str): The Python code to import
        module_name (str): The name to give the module

    Returns:
        ModuleType: The imported module

    Example:
        code = '''
        def hello(name):
            return f"Hello, {name}!"

        CONSTANT = 42
        '''
        module = import_string_as_module(code, "dynamic_module")
        print(module.hello("World"))  # Hello, World!
        print(module.CONSTANT)  # 42
    """
    # Create a new module spec
    spec = importlib.util.spec_from_loader(
        module_name,
        loader=None
    )

    # Create a new module based on the spec
    module = importlib.util.module_from_spec(spec)

    # Add the module to sys.modules
    sys.modules[module_name] = module

    # Execute the code string in the module's context
    exec(code_string, module.__dict__)

    return module


def unload_module(module_name: str) -> bool:
    """
    Unload a module from sys.modules.

    Args:
        module_name (str): The name of the module to unload

    Returns:
        bool: True if module was successfully unloaded, False if module wasn't found

    Example:
        # Import module
        module = import_string_as_module(code, "test_module")

        # Unload it
        unload_module("test_module")
    """
    try:
        # Remove all references to the module from sys.modules
        if module_name in sys.modules:
            del sys.modules[module_name]

            # If the module is part of a package, also remove parent package references
            parts = module_name.split('.')
            if len(parts) > 1:
                for i in range(1, len(parts)):
                    parent = '.'.join(parts[:-i])
                    if parent in sys.modules:
                        del sys.modules[parent]

            return True
    except Exception as e:
        print(f"Error unloading module {module_name}: {str(e)}")
        return False

    return False

def main() -> int:
    operating_system = detect_os()
    os_version = detect_os_version(operating_system)
    distros = detect_distros(operating_system)

    print(f'Operating System: {operating_system} {distros} {os_version}')

    distros_to_process = distros.copy()
    distros_to_process.reverse()

    distro_files = {
        'ubuntu': 'files/benchmarks/ubuntu/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0.svulns.json',
        'debian': 'files/benchmarks/debian/CIS_Debian_Linux_11_Benchmark_v2.0.0/CIS_Debian_Linux_11_Benchmark_v2.0.0.svulns.json',
    }

    for distro in distros_to_process:
        if distro in distro_files:
            distro_json = json.loads(pathlib.Path(distro_files[distro]).read_text())
            distro_json = [v for v in distro_json if "level-1-workstation" in distro_json['profiles']]
            for item in distro_json:
                print(f"Checking vuln {item['id']} {item['name']}")
                item_module = import_string_as_module(item['python_script'], 'distro_item_module')
                if item_module.audit_vuln():
                    print("Vuln doesn't exist on the system")
                else:
                    print("Remediating vuln")
                    item_module.remediate_vuln()
                    if not item_module.audit_vuln():
                        print("Failed to remediate vuln, may require manual intervention")
                unload_module('distro_item_module')
        else:
            print(f"Distro `{distro}` doesn't exist.")

    return 0

if __name__ == '__main__':
    sys.exit(main())

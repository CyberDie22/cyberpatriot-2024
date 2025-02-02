import asyncio
import concurrent
from concurrent import futures
import json
import sys
from typing import Any
import ast

import openai
import pymupdf
import pymupdf4llm
import pathlib
import re
import os
import time
from tqdm import tqdm

# Options
pdf_file = "files/benchmarks/ubuntu/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0.pdf"
operating_system = "Ubuntu 22.04"
treat_all_manual = False
toc_range = [3, 10]
openrouter_key = "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"
ids = ['1.1.1.1', '1.1.1.2', '1.1.1.3', '1.1.1.4', '1.1.1.5', '1.5.1', '1.5.2', '1.5.3', '1.5.4', '1.5.5', '1.6.1', '1.6.2', '1.6.3', '1.6.4', '1.6.5', '1.6.6', '1.7.2', '1.7.3', '1.7.4', '1.7.5', '1.7.8', '1.7.9', '1.7.10', '2.1.3', '2.1.4', '2.1.5', '2.1.6', '2.1.7', '2.1.8', '2.1.9', '2.1.10', '2.1.12', '2.1.13', '2.1.14', '2.1.15', '2.1.16', '2.1.17', '2.1.18', '2.1.19', '2.2.1', '2.2.2', '2.2.3', '2.2.4', '2.2.5', '2.2.6', '2.3.1.1', '2.3.2.1', '2.4.1.1', '2.4.1.2', '2.4.1.3', '2.4.1.4', '2.4.1.5', '2.4.1.6', '2.4.1.7', '2.4.1.8', '2.4.2.1', '3.3.1', '3.3.2', '3.3.3', '3.3.4', '3.3.5', '3.3.6', '3.3.7', '3.3.8', '3.3.9', '3.3.10', '3.3.11', '4.1.1', '4.1.2', '4.1.3', '4.1.4', '5.1.1', '5.1.2', '5.1.3', '5.1.4', '5.1.5', '5.1.6', '5.1.7', '5.1.8', '5.1.9', '5.1.10', '5.1.11', '5.1.12', '5.1.13', '5.1.14', '5.1.15', '5.1.16', '5.1.17', '5.1.18', '5.1.19', '5.1.20', '5.1.21', '5.1.22', '5.2.1', '5.2.2', '5.2.3', '5.2.5', '5.2.6', '5.2.7', '5.3.1.1', '5.3.1.2', '5.3.1.3', '5.3.2.1', '5.3.2.2', '5.3.2.3', '5.3.2.4', '5.3.3.1.1', '5.3.3.1.2', '5.3.3.2.1', '5.3.3.2.2', '5.3.3.2.4', '5.3.3.2.5', '5.3.3.2.6', '5.3.3.2.7', '5.3.3.2.8', '5.3.3.3.1', '5.3.3.3.2', '5.3.3.3.3', '5.3.3.4.1', '5.3.3.4.2', '5.3.3.4.3', '5.3.3.4.4', '5.4.1.1', '5.4.1.3', '5.4.1.4', '5.4.1.5', '5.4.1.6', '5.4.2.1', '5.4.2.2', '5.4.2.3', '5.4.2.6', '5.4.2.7', '5.4.2.8', '5.4.3.2', '5.4.3.3', '6.2.1.1.1', '6.2.1.1.4', '6.2.1.1.5', '6.2.1.1.6', '6.2.2.1', '7.1.1', '7.1.2', '7.1.3', '7.1.4', '7.1.5', '7.1.6', '7.1.7', '7.1.8', '7.1.9', '7.1.10', '7.2.1', '7.2.2', '7.2.3', '7.2.4', '7.2.5', '7.2.6', '7.2.7', '7.2.8']

# OpenRouter Client
openrouter_client = openai.Client(
    api_key=openrouter_key,
    base_url="https://openrouter.ai/api/v1"
)

async_openrouter_client = openai.AsyncClient(
    api_key=openrouter_key,
    base_url="https://openrouter.ai/api/v1"
)

def extract_pdf_range(file, pdf_range):
    full_pdf = pymupdf.open(file)
    full_pdf.select(range(pdf_range[0] - 1, pdf_range[1]))
    try:
        pdf_md = pymupdf4llm.to_markdown(full_pdf, show_progress=False)
    except Exception as e:
        print(f"Error converting PDF to markdown: {e}")
        pdf_md = ""
    full_pdf.close()
    return pdf_md


def is_valid_python(code_string):
    """
    Tests if a string contains valid Python code.

    Args:
        code_string (str): The string containing Python code to validate

    Returns:
        tuple: (is_valid, error_message)
            - is_valid (bool): True if code is valid Python, False otherwise
            - error_message (str): Description of the error if code is invalid, empty string if valid
    """
    try:
        ast.parse(code_string)
        return True
    except SyntaxError as e:
        return False

print("Extracting table of contents")
toc_md = extract_pdf_range(pdf_file, toc_range)
pathlib.Path(pdf_file.replace('.pdf', '.toc.md')).write_bytes(toc_md.encode())

# Regexes
toc_split_regex = re.compile(r'^### \d.*$', re.MULTILINE)
# ^((?:\d+\.)+\d+) ((?:.|\n)+?)[ \n]\((.*)\)[ \n]*\.*[ \n]*(\d+)$
toc_vuln_regex = re.compile(r'^((?:\d+\.)+\d+) ((?:.|\n)+?)[ \n]\((.*)\)[ \n]*\.*[ \n]*(\d+)$', re.MULTILINE)
# ^(?:(?:\*\*)|(?:##))(?:.|\n)+?(\d+)(?:\*\*$)*$
toc_section_regex = re.compile(r'^(?:(?:\*\*)|(?:##))(?:.|\n)+?(\d+)(?:\*\*$)*$', re.MULTILINE)

print("Parsing table of contents")
toc_vulns = toc_vuln_regex.findall(toc_md)
toc_sections = toc_section_regex.findall(toc_md)

current_section_index = 0

print("Generating vulnerability list from table of contents")
# { 'name': 'name', 'id': '1.2.3.4', 'type': 'automated/manual', 'start_page': 1, 'end_page': 2 }
vulnerabilities = []

for idx, vuln in enumerate(toc_vulns):
    vuln_id = vuln[0]
    vuln_name = vuln[1]
    vuln_type = vuln[2]
    vuln_start_page = int(vuln[3])

    if idx + 1 <= len(toc_vulns) and current_section_index <= len(toc_sections):
        if idx + 1 < len(toc_vulns):
            possible_vuln_end_page = int(toc_vulns[idx + 1][3])

            while True:  # TODO: this assumes that the sections continue forever and never exhaust before the vulns do
                section_page = toc_sections[current_section_index]
                if section_page == '':
                    print("!!!!!!! THIS SHOULD NOT HAPPEN: EMPTY SECTION !!!!!!!")
                    print(f"Current section index: {current_section_index}")
                    print(f"Current vuln index: {idx}")
                    print(f"Current vuln: {vuln}")
                    exit()
                section_page = int(section_page)
                if section_page < vuln_start_page:
                    current_section_index += 1
                else:
                    break

            vuln_end_page = possible_vuln_end_page if section_page > possible_vuln_end_page else section_page
        else:
            print(f"last vuln: {toc_sections[current_section_index]}")
            vuln_end_page = int(toc_sections[current_section_index])
    else:
        print("!!!!!!! THIS SHOULD NOT HAPPEN: EXHAUSTED SECTIONS BEFORE VULNS !!!!!!")
        print(f"Current section index: {current_section_index}")
        print(f"Section count: {len(toc_sections)}")
        print(f"test: {current_section_index <= len(toc_sections)}")
        print(f"Current vuln index: {idx}")
        print(f"Current vuln: {vuln}")
        print(f"Last section: {toc_sections[current_section_index - 1]}")
        print(f"Current section: {toc_sections[current_section_index]}")
        vuln_end_page = toc_range[1]

    vulnerabilities.append({
        'name': vuln_name,
        'id': vuln_id,
        'type': vuln_type,
        'start_page': int(vuln_start_page + 1),
        'end_page': int(vuln_end_page)
    })

def extract_vulnerability(vulnerability, vuln_md):
    # file_path = pdf_file.replace('.pdf', f'.vuln.{vuln["id"]}.md')
    # pathlib.Path(file_path).write_bytes(vuln_md.encode())
    response = openrouter_client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {'role': 'system',
             'content': 'Take the vulnerability description provided by the user and return a json object representing it. Respond with all of the text from the source.'},
            {'role': 'user', 'content': vuln_md}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "vulnerability_extraction",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "profiles": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["level-1-server", "level-1-workstation", "level-2-server",
                                         "level-2-workstation"]
                            }
                        },
                        "description": {"type": "string"},
                        "rationale": {"type": "string"},
                        "audit_details": {"type": "string"},
                        "audit_code": {"type": "string"},
                        "remediation_details": {"type": "string"},
                        "remediation_code": {"type": "string"},
                    },
                    "required": ["name", "profiles", "description", "rationale", "audit_details", "audit_code",
                                 "remediation_details", "remediation_code"],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
    )
    json_text = response.choices[0].message.content
    json_text = re.sub(r'```json(.*?)```', r'\1', json_text, flags=re.DOTALL)
    llm_vuln = json.loads(json_text)

    response = openrouter_client.chat.completions.create(
        model="google/gemini-flash-1.5-8b",
        messages=[
            {'role': 'system',
             'content': 'Take the vulnerability description provided by the user and respond with a detailed description of the vulnerability.'},
            {'role': 'user', 'content': vuln_md}
        ],
    )
    llm_description = response.choices[0].message.content

    new_vuln = {
        'name': vulnerability['name'],
        'id': vulnerability['id'],
        'type': vulnerability['type'],
        'start_page': vulnerability['start_page'],
        'end_page': vulnerability['end_page'],
        'profiles': llm_vuln['profiles'],
        'description': llm_vuln['description'],
        'detailed_description': llm_description,
        'rationale': llm_vuln['rationale'],
        'audit_details': llm_vuln['audit_details'],
        'audit_code': llm_vuln['audit_code'],
        'remediation_details': llm_vuln['remediation_details'],
        'remediation_code': llm_vuln['remediation_code']
    }
    return new_vuln

def process_extracting_vulnerabilities(vulnerabilities, pdf_file: str, max_workers: int = 25):
    output_file = pdf_file.replace(".pdf", ".pvulns.json")
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            results = json.load(f)
    else:
        results = [None] * len(vulnerabilities)

    if all(results):
        return results

    vuln_pdfs = [extract_pdf_range(pdf_file, [vuln['start_page'], vuln['end_page']]) for vuln in tqdm(vulnerabilities, desc="Extracting vuln pdfs to markdown")]

    def write_results_to_file():
        pathlib.Path(output_file).write_text(json.dumps(results, indent=4))

    progress_bar = tqdm(total=len([v for i, v in enumerate(vulnerabilities) if results[i] is None]), desc="Processing vulnerabilities", unit="vulnerability")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_index = {
            executor.submit(extract_vulnerability, vuln, vuln_pdfs[i]): i
            for i, vuln in enumerate(vulnerabilities) if results[i] is None
        }

        # Process completed tasks
        for future in concurrent.futures.as_completed(future_to_index):
            index = future_to_index[future]
            try:
                results[index] = future.result()
                progress_bar.update(1)
            except Exception as e:
                print(f"Vulnerability at index {index} generated an exception: {e}")
                results[index] = None  # or some error placeholder

            # Write current results to file after each processed vulnerability
            write_results_to_file()

    return results

print(f"Extracting vulnerabilities ({len(vulnerabilities)})")
vulnerabilities = process_extracting_vulnerabilities(vulnerabilities, pdf_file)
pathlib.Path(pdf_file.replace('.pdf', '.pvulns.json')).write_text(json.dumps(vulnerabilities, indent=4))

vulnerabilities = [v for v in vulnerabilities if v is not None]
manual_vulnerabilities = [v for v in vulnerabilities if 'Manual' in v['type']]

# write manual vulnerabilities to file
manual_vulns_file = pdf_file.replace('.pdf', '.mvulns.json')
pathlib.Path(manual_vulns_file).write_text(json.dumps(manual_vulnerabilities, indent=4))

# def process_vulnerability_to_md(vuln: dict[str, Any], operating_system: str, openrouter_client) -> dict[str, Any]:
#     """Process a single vulnerability and return a markdown string."""
#     simple_vuln = {
#         'name': vuln['name'],
#         'id': vuln['id'],
#         'profiles': vuln['profiles'],
#         'description': vuln['description'],
#         'detailed_description': vuln['detailed_description'],
#         'rationale': vuln['rationale'],
#         'audit_details': vuln['audit_details'],
#         'audit_code': vuln['audit_code'],
#         'remediation_details': vuln['remediation_details'],
#         'remediation_code': vuln['remediation_code']
#     }
#
#     response = openrouter_client.chat.completions.create(
#         model="anthropic/claude-3.5-sonnet:beta",
#         messages=[
#             {'role': 'system', 'content': "Take the vulnerability details provided by the user and respond with a markdown formatted vulnerability. Respond with the markdown formatted vulnerability in <vuln_md> tags. Respond with the sections: Description, Audit, and Remediation in that order. Make sure to provide steps for both Linux and Windows."},
#             {'role': 'user', 'content': json.dumps(simple_vuln)}
#         ]
#     )
#     vuln_md = response.choices[0].message.content
#     vuln_md = vuln_md.split("<vuln_md>")[1].split("</vuln_md>")[0].strip()
#     return {
#         'id': vuln['id'],
#         'markdown': vuln_md
#     }
#
# def process_vulnerabilities_to_md_parallel(
#         vulnerabilities: list[dict[str, Any]],
#         operating_system: str,
#         openrouter_client,
#         max_workers: int = 25,
# ) -> list[dict[str, Any]]:
#     """
#     Process vulnerabilities in parallel with a maximum of 25 concurrent tasks.
#
#     Args:
#         vulnerabilities: List of vulnerability dictionaries to process
#         operating_system: Target OS for the vulnerability scripts
#         openrouter_client: OpenRouter API client
#         max_workers: Maximum number of concurrent tasks (default: 25)
#
#     Returns:
#         None
#     """
#     progress_bar = tqdm(total=len(vulnerabilities), desc="Generating md files for manual vulnerabilities")
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
#         # Submit initial batch of tasks
#         future_to_index = {
#             executor.submit(
#                 process_vulnerability_to_md,
#                 vuln,
#                 operating_system,
#                 openrouter_client
#             ): i
#             for i, vuln in enumerate(vulnerabilities)
#         }
#
#         # Process completed tasks and update progress
#         for future in concurrent.futures.as_completed(future_to_index):
#             index = future_to_index[future]
#             try:
#                 result = future.result()
#                 if result is not None:
#                     pathlib.Path(pdf_file.replace('.pdf', f'.vuln.{result["id"]}.md')).write_text(result["markdown"])
#                 progress_bar.update(1)
#
#             except Exception as e:
#                 print(f"Task failed for vulnerability at index {index}: {str(e)}")
#
#     progress_bar.close()
#
# vulnerabilities = process_vulnerabilities_to_md_parallel(vulnerabilities, operating_system, openrouter_client)

vulnerabilities = [v for v in vulnerabilities if 'Automated' in v['type']]
vulnerabilities = [v for v in vulnerabilities if 'level-1-workstation' in v['profiles']]

starts_filter = ["1.1.1", "1.1.2", "1.3", "1.4", "2.3.1", "2.3.3", "4", "6.1", "6.2.1.2", "7.2"]
vulnerabilities = [v for v in vulnerabilities if not v['id'].startswith(tuple(starts_filter))]

print(f"Extracted {len(vulnerabilities)} vulnerabilities after filtering")

# auto_vulns = [v for v in vulnerabilities if v['audit_code'].startswith("#!/usr/bin/env bash") and v['remediation_code'].startswith("#!/usr/bin/env bash")]
# non_auto_vulns = [v for v in vulnerabilities if v not in auto_vulns]

def extract_xml_tag_content(text: str, tag: str):
    tag_start = f"<{tag}>"
    tag_end = f"</{tag}>"
    start_index = text.rfind(tag_start)
    end_index = text.rfind(tag_end)
    if start_index == -1 or end_index == -1:
        return ""
    return text[start_index + len(tag_start):end_index].strip()

def extract_markdown_code(text: str, language: str):
    code_start = f"```{language}"
    code_end = "```"
    start_index = text.find(code_start)
    end_index = text.rfind(code_end)
    if start_index == -1 or end_index == -1:
        return ""
    return text[start_index + len(code_start):end_index].strip()

# Generating tasks
# for vuln in vulnerabilities:
#     simple_vuln = {
#         'name': vuln['name'],
#         'description': vuln['description'],
#         'rationale': vuln['rationale'],
#         'audit_details': vuln['audit_details'],
#         'audit_code': vuln['audit_code'],
#         'remediation_details': vuln['remediation_details'],
#         'remediation_code': vuln['remediation_code']
#     }
#     response = openrouter_client.chat.completions.create(
#         model="nvidia/llama-3.1-nemotron-70b-instruct",
#         messages=[
#             {'role': 'system', 'content': """The user will provide a vulnerability along with steps and code to audit and remediate it. Respond with a python script that has 2 functions, one called `def audit_vuln() -> bool` and another called `def remediate_vuln() -> None`. Think about what to do before responding in <thinking> tags. Respond with the python script in <code> tags. When you perform an action in remediation print what you did, e.g. \"Disabled `x` systemd service.\", do not print that remediation or audit has completed or started. Rewrite the script in a way that is more pythonic, don't follow the bash conventions used in the provided scripts. Use python code instead of running shell code where possible. Declare imports all at the top of the file. This will be run on """ + operating_system + "."},
#             {'role': 'user', 'content': json.dumps(simple_vuln)}
#         ]
#     )
#     code = extract_xml_tag_content(response.choices[0].message.content, 'code')
#     if code.startswith("```python") and code.endswith("```"):
#         code = code.lstrip("```python")
#         code = code.rstrip("```")
#
#     vuln['python_script'] = code

def generate_vuln_script(openrouter_client, simple_vuln: dict, operating_system: str, code: str = ""):
    user_message = f"{json.dumps(simple_vuln)}"
    if code:
        user_message += f"\n\n{code}\n\nThe code provided is not correct. Please fix it."

    user_message += "Use the provided vulnerability details to generate a python script that audits and remediates the vulnerability." \
                    "Respond with a python script that has two functions, one called `def audit_vuln() -> bool` and another called `def remediate_vuln() -> None`." \
                    "The audit should return true if no remediation is needed and false if remediation is needed." \
                    "Respond with the python script in markdown code tags. Respond with valid python code." \
                    "You must respond with the full code." \

    response = openrouter_client.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[
            {'role': 'user', 'content': user_message},
        ],
        extra_body={
            'provider': {
                'order': [
                    'DeepSeek'
                ],
                'allow_fallbacks': False
            }
        }
    )
    
    new_response = openrouter_client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {'role': 'user', 'content': f'Message:\n{response.choices[0].message.content}\n\nTake the above message and respond with the whole python script. The python script should be provided in the format:\n```python\n<code>\n```\n\nDo not provide anything other than the code block.'}
        ]
    )
    code = extract_markdown_code(new_response.choices[0].message.content, 'python')
    if code.startswith("```python") and code.endswith("```"):
        code = code.lstrip("```python")
        code = code.rstrip("```")
    print(code)
    return code

def fix_vuln_script(openrouter_client, simple_vuln: dict, operating_system: str, code: str):
    response = openrouter_client.chat.completions.create(
        model="qwen/qwen-2.5-coder-32b-instruct",
        messages=[
            {'role': 'system',
             'content': """The user will provide a vulnerability along with steps and code to audit and remediate it. Respond with a python script that has 2 functions, one called `def audit_vuln() -> bool` and another called `def remediate_vuln() -> None`. The audit should return true if no remediation is needed and false if remediation is needed. Be sure to respond with valid python. Think about what to do before responding in <thinking> tags. Respond with the python script in <code> tags. When you perform an action in remediation print what you did, e.g. \"Disabled `x` systemd service.\", do not print that remediation or audit has completed or started. Rewrite the script in a way that is more pythonic, don't follow the bash conventions used in the provided scripts. Use python code instead of running shell code where possible. Declare imports all at the top of the file. The code must contain the `audit_vuln` and `remediate_vuln` functions. This will be run on """ + operating_system + "."},
            {'role': 'user', 'content': json.dumps(simple_vuln)},
            {'role': 'assistant', 'content': f"<code>\n```python\n{code}\n```\n</code>"},
            {'role': 'user', 'content': "The code provided is not correct. Please fix it."}
        ]
    )
    code = extract_markdown_code(response.choices[0].message.content, 'python')
    if code.startswith("```python") and code.endswith("```"):
        code = code.lstrip("```python")
        code = code.rstrip("```")
    return code

def process_vulnerability_script(vuln: dict[str, Any], operating_system: str, openrouter_client) -> dict[str, Any]:
    """Process a single vulnerability and return the updated vulnerability dict."""
    simple_vuln = {
        'name': vuln['name'],
        'description': vuln['description'],
        'rationale': vuln['rationale'],
        'audit_details': vuln['audit_details'],
        'audit_code': vuln['audit_code'],
        'remediation_details': vuln['remediation_details'],
        'remediation_code': vuln['remediation_code']
    }

    try:
        code = generate_vuln_script(openrouter_client, simple_vuln, operating_system)
        is_valid = is_valid_python(code)
        tries = 1
        while not is_valid and tries < 5:
            print("Invalid python code generated, retrying...")
            tries += 1
            code = generate_vuln_script(openrouter_client, simple_vuln, operating_system, code)
            is_valid = is_valid_python(code)
        if not is_valid:
            print("Invalid python code generated after 5 tries, skipping vulnerability")
            return None

        vuln['python_script'] = code
        return vuln
    except Exception as e:
        print(f"Error processing vulnerability '{vuln['name']}': {str(e)}")
        return None


def process_vulnerabilities_script_parallel(
        vulnerabilities: list[dict[str, Any]],
        operating_system: str,
        openrouter_client,
        max_workers: int = 25,
) -> list[dict[str, Any]]:
    """
    Process vulnerabilities in parallel with a maximum of 25 concurrent tasks.

    Args:
        vulnerabilities: List of vulnerability dictionaries to process
        operating_system: Target OS for the vulnerability scripts
        openrouter_client: OpenRouter API client
        max_workers: Maximum number of concurrent tasks (default: 25)
        output_file: Optional path to save progress (default: None)

    Returns:
        List of processed vulnerabilities with added python_script field
    """
    output_file = pdf_file.replace(".pdf", ".svulns.json")
    results = [None] * len(vulnerabilities)

    # Load existing results if output file exists
    if output_file and os.path.exists(output_file):
        with open(output_file, 'r') as f:
            existing_results = json.load(f)
            results = existing_results

    def save_progress():
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)

    progress_bar = tqdm(total=len(vulnerabilities), desc="Processing vulnerabilities")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit initial batch of tasks
        future_to_index = {
            executor.submit(
                process_vulnerability_script,
                vuln,
                operating_system,
                openrouter_client
            ): i
            for i, vuln in enumerate(vulnerabilities) if results[i] is None
        }

        # Process completed tasks and update progress
        for future in concurrent.futures.as_completed(future_to_index):
            index = future_to_index[future]
            try:
                result = future.result()
                if result is not None:
                    results[index] = result
                progress_bar.update(1)

                # Save progress after each completed task
                save_progress()

            except Exception as e:
                print(f"Task failed for vulnerability at index {index}: {str(e)}")
                results[index] = None

    progress_bar.close()
    return results

vulnerabilities = process_vulnerabilities_script_parallel(vulnerabilities, operating_system, openrouter_client)

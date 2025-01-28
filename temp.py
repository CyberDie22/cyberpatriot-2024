import json

with open(
        'files/benchmarks/ubuntu/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0/CIS_Ubuntu_Linux_22.04_LTS_Benchmark_v2.0.0.svulns_old.json', 'r') as f:
    data = json.load(f)

lines = 0
for item in data:
    lines += item['python_script'].count('\n') + 1

print(lines)
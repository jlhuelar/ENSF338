import json

def process_json_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for record in data:
        if 'payload' in record and 'size' in record['payload']:
            record['payload']['size'] = 42

    data.reverse()

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

input_file_path = 'Lab 1/large-file.json'
output_file_path = 'Lab 1/output.2.3.json'

process_json_file(input_file_path, output_file_path)
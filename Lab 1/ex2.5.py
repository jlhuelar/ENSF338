import json
import timeit

def modify_records(data):
    for record in data:
        if 'payload' in record and 'size' in record['payload']:
            record['payload']['size'] = 42

def load_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data, output_file):
    data.reverse()
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def main(input_file, output_file):
    data = load_data(input_file)

    time_taken = timeit.timeit(lambda: modify_records(data), number = 10)

    average_time = time_taken / 10
    
    print(f'Average time taken to modify records: {average_time} seconds.')

    save_data(data, output_file)

input_file_path = 'Lab 1/large-file.json'
output_file_path = 'Lab 1/output.2.5.json'

main(input_file_path, output_file_path)
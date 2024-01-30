import json
import timeit
import matplotlib.pyplot as plt

def modify_records(data, record_count):
    for record in data[:record_count]:
        if 'payload' in record and 'size' in record['payload']:
            record['payload']['size'] = 42

def load_data(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def time_processing(data, record_count, repetitions):
    return timeit.repeat(lambda: modify_records(data, record_count), number=1, repeat=repetitions)

def main(input_file):
    data = load_data(input_file)
    times = time_processing(data, 1000, 1000)

    plt.figure(figsize=(10, 6))
    plt.hist(times, bins=50, color='blue', edgecolor='black')
    plt.xlabel('Number of Records')
    plt.ylabel('Average Processing Time (seconds)')
    plt.title('Linear Regression of Processing Time vs Number of Records')
    plt.grid(True)

    plt.savefig('Lab 1/output.3.3.png')
    plt.show()

input_file_path = 'Lab 1/large-file.json'
main(input_file_path)
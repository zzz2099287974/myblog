import os
import psutil
import time
import tempfile

def cpu_benchmark(duration=5):
    print("Running CPU benchmark...")
    start_time = time.time()
    count = 0
    while time.time() - start_time < duration:
        count += 1
    print(f"CPU benchmark completed: {count} iterations in {duration} seconds.")

def memory_benchmark(size_in_mb=100):
    print("Running memory benchmark...")
    size_in_bytes = size_in_mb * 1024 * 1024
    data = bytearray(size_in_bytes)
    start_time = time.time()
    for i in range(size_in_bytes):
        data[i] = i % 256
    end_time = time.time()
    duration = end_time - start_time
    print(f"Memory benchmark completed: {size_in_mb} MB written in {duration:.2f} seconds.")

def disk_io_benchmark(file_size_in_mb=100):
    print("Running disk I/O benchmark...")
    file_size_in_bytes = file_size_in_mb * 1024 * 1024
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    start_time = time.time()
    with open(temp_file.name, 'wb') as f:
        f.write(os.urandom(file_size_in_bytes))
    end_time = time.time()
    duration = end_time - start_time
    os.remove(temp_file.name)
    print(f"Disk I/O benchmark completed: {file_size_in_mb} MB written in {duration:.2f} seconds.")

def system_info():
    print("\nSystem Information:")
    print(f"CPU: {psutil.cpu_count(logical=False)} physical cores, {psutil.cpu_count(logical=True)} logical cores")
    print(f"Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Disk: {psutil.disk_usage('/').total / (1024**3):.2f} GB total, {psutil.disk_usage('/').free / (1024**3):.2f} GB free")

def main():
    system_info()
    cpu_benchmark()
    memory_benchmark()
    disk_io_benchmark()

if __name__ == "__main__":
    main()


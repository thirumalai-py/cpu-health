import psutil

"""
The list of available options in the psutil 
"""

# Get CPU usage percentage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get memory usage
memory_info = psutil.virtual_memory()
print(f"Total Memory: {memory_info.total / (1024**3):.2f} GB")
print(f"Available Memory: {memory_info.available / (1024**3):.2f} GB")
print(f"Used Memory: {memory_info.used / (1024**3):.2f} GB")
print(f"Memory Usage: {memory_info.percent}%")

# Get disk usage
disk_usage = psutil.disk_usage('/')
print(f"Total Disk Space: {disk_usage.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk_usage.used / (1024**3):.2f} GB")
print(f"Free Disk Space: {disk_usage.free / (1024**3):.2f} GB")
print(f"Disk Usage: {disk_usage.percent}%")

# Get network information
net_io = psutil.net_io_counters()
print(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
print(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
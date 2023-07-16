import psutil
import time
def get_app_pid(app_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == app_name:
            return proc.pid

    return None

def get_app_usage(app_name):
    pid = get_app_pid(app_name)
    if pid:
        process = psutil.Process(pid)
        cpu_usage = process.cpu_percent(interval=1)
        mem_usage = process.memory_percent()
        return pid, cpu_usage, mem_usage
    else:
        return None

# Example usage:
app_name = "Spotify"
app_usage = get_app_usage(app_name)
if app_usage:
    pid, cpu_usage, mem_usage = app_usage
    print(f"Application: {app_name}, PID: {pid}, CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")
else:
    print(f"Application {app_name} is not running.")


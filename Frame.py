import psutil
import time

def check_spotify_status():
    try:
        return any(proc.name() == "Spotify" for proc in psutil.process_iter())
    except psutil.NoSuchProcess:
        return False

def get_spotify_usage_duration():
    is_spotify_running = False
    start_time = None

    while True:
        if check_spotify_status():
            if not is_spotify_running:
                is_spotify_running = True
                start_time = time.time()

        elif is_spotify_running:
            is_spotify_running = False
            end_time = time.time()
            duration_hours = (end_time - start_time) / 3600  # Convert to hours
            return duration_hours

# Example usage
duration = get_spotify_usage_duration()
print("Spotify usage duration:", duration, "hours")

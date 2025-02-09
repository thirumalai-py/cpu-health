# CPU Monitoring Script with Alerts

This Python script continuously monitors CPU usage and triggers alerts when the usage exceeds a specified threshold. It supports sound alerts.

## Features

- ✅ **Monitors CPU Usage** in real-time
- 🔔 **Plays Sound Alert** if CPU usage exceeds the threshold
- ♻️ Runs infinitely until manually stopped or an error occurs

## Prerequisites

Make sure you have Python installed on your system. You can check by running:

```sh
python --version
```

## Installation

Install the required Python packages using `requirements.txt`:

```sh
pip install -r requirements.txt
```

## Usage

1. **Update Configuration:**

   - Set `CPU_THRESHOLD` (default: `80%`).
   - Replace `alert.mp3` with your sound file.

2. **Run the script:**

```sh
python cpu_monitor.py
```

## Code Overview

**Notes on Dependencies:**
- `psutil`: Used for monitoring CPU usage.
- `playsound`: Used for playing alert sounds.

```python
import psutil
import time
from playsound import playsound

CPU_THRESHOLD = 70  
ALERT_SOUND = "alert.mp3"

while True:
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")

        if cpu_usage > CPU_THRESHOLD:
            print("High CPU usage detected! Playing alert sound...")
            playsound(ALERT_SOUND)

    except Exception as e:
        print(f"Error occurred: {e}")
        break
```

## Notes

- The script checks CPU usage **based on the INTERVAL**.
- If usage is above the threshold, it triggers a **sound alert**.
- Modify the `time.sleep()` interval to control alert frequency.

## Output

![alt text](/media/output.png)

## License

This project is open-source under the MIT License.

---

🔧 **Happy Monitoring!** 🚀

import threading
import subprocess
import time

from localServer import host

# Start the local server in a separate thread
server_thread = threading.Thread(target=host)
server_thread.start()

# Wait for a moment to ensure the server has started
time.sleep(2)

# Start the Flask backend in a subprocess
backend_process = subprocess.Popen(["python", "notetaker.py"])

try:
    # Keep the main thread running
    server_thread.join()

except KeyboardInterrupt:
    # Handle keyboard interrupt to gracefully stop the subprocess
    backend_process.terminate()
    backend_process.wait()
    print("Server stopped.")

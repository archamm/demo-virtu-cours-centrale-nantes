import socket
import os

def get_container_info():
    hostname = socket.gethostname()
    container_id = os.environ.get("CONTAINER_ID", "N/A")

    print(f"Container Hostname: {hostname}")
    print(f"Container ID: {container_id}")

if __name__ == "__main__":
    get_container_info()
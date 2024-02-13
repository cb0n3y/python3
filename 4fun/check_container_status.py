#!/usr/bin/python3

__author__ = 'cb0n3y'
__version__ = '0.1'
__copyright__ = 'Copyright (c) 2023-2024 cb0n3y'


import subprocess
import sys
import json
import argparse


def run_docker_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.output.strip()}")
        sys.exit(3)


def check_container_status(container_id, container_name=None):
    container_info = run_docker_command(f"docker inspect {container_id}")
    container_data = json.loads(container_info)[0]

    current_container_name = container_data["Name"].lstrip("/")  # Remove leading slash from container name

    if container_name is None or current_container_name == container_name:
        container_status = container_data["State"]["Status"]
        if container_status == "running":
            return f"OK: {current_container_name} is running."
        else:
            return f"WARNING: {current_container_name} is {container_status}."

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check status of Docker containers.")
    parser.add_argument("-n", "--name", help="Target a single Docker container by name")
    args = parser.parse_args()

    container_ids = run_docker_command("docker ps -a -q").splitlines()

    for container_id in container_ids:
        container_status = check_container_status(container_id, args.name)
        if container_status:
            print(container_status)

    sys.exit(0)
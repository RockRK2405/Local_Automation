import subprocess
import time
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def simulate_launch_instance():
    """Simulates the launch of a virtual instance and runs a local script."""
    logging.info("Simulating instance launch...")
    
    os.makedirs("output", exist_ok=True)
    try:
        result = subprocess.run(["bash", "script.sh"], check=True)
        logging.info("Script executed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Script execution failed: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def fetch_output():
    """Fetches the output from the simulated instance."""
    output_file = "output/output.txt"
    
    try:
        with open(output_file, "r") as file:
            logging.info("Reading output from script.")
            return file.read()
    except FileNotFoundError:
        logging.warning("Output file not found.")
        return "No output found. Did you run the script?"
    except Exception as e:
        logging.error(f"Error reading output file: {e}")
        return "Error fetching output."

def simulate_terminate_instance():
    """Simulates terminating the instance."""
    logging.info("Simulating instance termination...")
    time.sleep(1)
    return "Simulated instance terminated."

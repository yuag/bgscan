import subprocess
import threading


scan_complete_event = threading.Event()

def run_pocsuite_scan(target, poc_file):


    pocsuite3_command = f"pocsuite -r {poc_file} -u {target}"

    print(f"Starting Pocsuite3 scan for {target} using POC file {poc_file}")

    try:
        result = subprocess.run(pocsuite3_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Pocsuite3 scan for {target} using POC file {poc_file} completed successfully:")
            print(result.stdout)
        else:
            print(f"Pocsuite3 scan for {target} using POC file {poc_file} failed:")
            print(result.stderr)
    except Exception as e:
        print(f"Error running Pocsuite3 for {target}: {str(e)}")


    scan_complete_event.set()

def main():

    targets_and_pocs = [
        {"target_url": "http://xxxx.com", "poc_file_path": "/pco"},


    ]

    threads = []

    for item in targets_and_pocs:
        target_url = item["target_url"]
        poc_file_path = item["poc_file_path"]
        thread = threading.Thread(target=run_pocsuite_scan, args=(target_url, poc_file_path))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

import argparse
import requests
import numpy

# Add Argument
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="Import URL from file")
parser.add_argument("--url", "-u", help="Direct URL check ")
parser.add_argument("--output", "-o", help="Output file location")

arg = parser.parse_args()

# Status Code List
statuses = {
    200: "Website Accessible",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}


# File Import
if arg.file:
    try:
        data_text = numpy.loadtxt(arg.file, dtype=str)
    except FileNotFoundError or FileExistsError:
        print("File not found!")

# Direct URL Check
if arg.url:
    if ("http" in arg.url):
        check_online = requests.get(f"{arg.url}", timeout=5)
        check_status = check_online.status_code
    else:
        check_online = requests.get(f"http://{arg.url}", timeout=5)
        check_status = check_online.status_code
    print(f"URL : {arg.url}\nStatus : {statuses[check_status]}")


# Multiple Target from notepad
if arg.file:
    for web in data_text:
        try:
            if ("http" in web):
                check_online = requests.get(f"{web}", timeout=5)
                check_status = check_online.status_code
            else:
                check_online = requests.get(f"http://{web}", timeout=5)
                check_status = check_online.status_code
            print(f"URL : {web}\nStatus : {check_status}")

            # Output location
            if arg.output:
                if check_status == (200 or 301):
                    with open(arg.output, "a") as output:
                        output.write(str(web) + "\n")
        except Exception:
            pass


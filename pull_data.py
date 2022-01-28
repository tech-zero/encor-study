import csv
from scrapli.driver.core import IOSXEDriver
# from rich import print as rprint
from inv import DEVICES

for device in DEVICES:
    hostname = device['hostname']
    with IOSXEDriver(
        host=device["host"],
        auth_username="admin",
        auth_password="cisco",
        auth_strict_key=False,
        ssh_config_file=True,
    ) as conn:
        response = conn.send_command("show version")
    structured_result = response.textfsm_parse_output()[0]
    version = structured_result["version"]
    serial = structured_result["serial"][0]

    with open("test.csv", "a", encoding="utf8") as csv_data:
        writer = csv.writer(csv_data)
        my_data = ("Tech-Zero", hostname, serial, version)
        writer.writerow(my_data)

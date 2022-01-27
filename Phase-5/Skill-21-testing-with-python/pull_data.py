import csv
from unittest import result
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

for device in DEVICES:
    hostname = device["hostname"
    with IOSXEDriver(
        host=device["host"],
        auth_username="admin",
        auth_password="cisco",
        auth_strict_key=False,
        ssh_config_file=True,
    ) as conn:
        response = conn.send_command("show version")
        print(response.result)
        
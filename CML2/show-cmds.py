from datetime import datetime
from scrapli.driver.core import IOSXEDriver
from inv4 import DEVICES

my_time = datetime.now().strftime("%H:%M:%S")

command_to_send = input("Enter the command you wish to send: ")

for device in DEVICES:
    hostname = device["hostname"]
    with IOSXEDriver(
        host=device["host"],
        auth_username="admin",
        auth_password="cisco",
        auth_strict_key=False,
        ssh_config_file=True,
    ) as conn:
        response = conn.send_command(command_to_send)
    structured_result = response.textfsm_parse_output()

my_list = response.result.splitlines()

with open(f"{command_to_send}-{my_time}.ios", "x") as f:
    for line in my_list:
        f.write(line + "\n")

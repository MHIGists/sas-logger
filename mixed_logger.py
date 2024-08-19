import datetime
import sys
import os
from sas import Sas
from config_handler import *
from models import *

output_file_translated = "sas_output_translated.txt"
output_file_byte = "sas_output_byte.txt"


def split_string_into_chunks(s, chunk_size=8):
    chunks = []
    for i in range(0, len(s), chunk_size):
        chunks.append(s[i:i + chunk_size])
    return chunks


def get_request_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def handle_hex_log(time, command_text):
    with open(output_file_byte, "a") as file:
        file.write(time + "\n")
        file.write(command_text + "\n")
        file.write("\n")


def clean_last_sas_log():
    # Cleaning last byte log since we only append due to the nature of the while loop
    if os.path.exists(output_file_byte):
        # Delete the file
        os.remove(output_file_byte)


# Bits means how many pair of bits is the command long itself after the flag example if it's 7 bits: 01 08 |7bits
# from the command => 00 00 00 00 00 00 00
requests_with_input = {
    "08": {
        "command_name": "Configure bill denominations",
        "bits": 7
    },
    "09": {
        "command_name": "Enable/disable game number",
        "bits": 5
    },
    "0C": {
        "command_name": "Set sound",
        "bits": 6
    },
    "0D": {
        "command_name": "Play sound",
        "bits": 6
    },
    "0E": {
        "command_name": "Enable/disable real time event reporting",
        "bits": 3
    },
    "21": {
        "command_name": "ROM signature verification",
        "bits": 4
    },
    "2D": {
        "command_name": "Send total hand paid cancelled credits for game number",
        "bits": 4
    },
    "2E": {
        "command_name": "Delay the gaming machine by x amount of milliseconds",
        "bits": 4
    },
    "2F": {
        "command_name": "Send selected meters for game n",
        "bits": 6
    },
    "4C": {
        "command_name": "Set enhanced validation ID",
        "bits": 8
    },
    "4D": {
        "command_name": "Set enhanced validation info",
        "bits": 3
    },
    "50": {
        "command_name": "Send validation meters",
        "bits": 3
    },
    "6F": {
        "command_name": "Extended Meters",
        "bits": 7
    },

}

requests = {
    "015108": "Lock Machine",
    "02CA3A": "Unlock Machine",
    "03432B": "Disable all sound",
    "04FC5F": "Enable all sound",
    "05754E": "Disable reel spin sound",
    "06EE7C": "Enable bill acceptor",
    "07676D": "Disable bill acceptor",
    "0A82B6": "Enter maintenance mode",
    "0B0BA7": "Exit maintenance mode",
    "0F": "Send meters 10 trough 15",
    "10": "Send cancelled coin meter",
    "11": "Send total coins in meter",
    "12": "Send total coin out meter",
    "13": "Send total drop meter",
    "14": "Send total jackpot meter",
    "15": "Send games played meter",
    "16": "Send games won meter",
    "17": "Send games lost meter",
    "18": "Send games since last power up and door closure",
    "19": "Send meters 11 trough 15",
    "1A": "Current credits",
    "1B": "Send hand pay information",
    "1C": "Send meters",
    "1D": "Send bill meters (# of bills)",
    "1F": "Send gaming machine ID & information",
    "20": "Send dollar value of bills meter",
    "27": "Send current restricted promotional credits",
    "2A": "Send true coin in meter (coins)",
    "2B": "Send true coin out meter (coins)",
    "2C": "Send current hopper level (coins)",
    "31": "Send 1 bills in meter",
    "32": "Send 2 bills in meter",
    "33": "Send 5 bills in meter",
    "34": "Send 10 bills in meter",
    "35": "Send 20 bills in meter",
    "36": "Send 50 bills in meter",
    "37": "Send 100 bills in meter",
    "38": "Send 500 bills in meter",
    "39": "Send 1000 bills in meter",
    "3A": "Send 200 bills in meter",
    "3B": "Send 25 bills in meter",
    "3C": "Send 2000 bills in meter",
    "3D": "Send cashout ticket information",
    "3E": "Send 2500 bills in meter",
    "3F": "Send 5000 bills in meter",
    "40": "Send 10000 bills in meter",
    "41": "Send 20000 bills in meter",
    "42": "Send 25000 bills in meter",
    "43": "Send 50000 bills in meter",
    "44": "Send 100000 bills in meter",
    "45": "Send 250 bills in meter",
    "46": "Send credit amount of all bills accepted",
    "47": "Send coin amount from an external coin acceptor",
    "48": "Send last accepted bill information",
    "49": "Send number of bills currently in stacker",
    "4A": "Send credit amount of bills currently in stacker",
    "4F": "Send current hopper status",
    "51": "Send total number of games implemented",
    "54": "Send SAS version and machine serial number",
    "55": "Send selected game number",
    "56": "Send enabled game numbers",
    "57": "Send pending cashout info",
    "70": "Send ticket validation data",
    "71": "Send current date and time",
    "84": "Send progressive win amount",
    "85": "Send SAS progressive win amount",
    "87": "Send multiple SAS progressive win amounts",
    "8E": "Send card information",
    "8F": "Send reel stop information",
    "90": "Send legacy bonus win amount",
    "9475CB": "Reset hand pay",
    "B1": "Send current player denomination",
    "B2": "Send enabled player denominations",
    "B3": "Send token denomination"
}
expected_reply = {
    "0F": 26,
    "10": 6,
    "11": 6,
    "12": 6,
    "13": 6,
    "14": 6,
    "15": 6,
    "16": 6,
    "17": 6,
    "18": 6,
    "19": 22,
    "1A": 6,
    "1B": 22,
    "1C": 34,
    "1D": "Send bill meters (# of bills)",
    "1F": "Send gaming machine ID & information",
    "20": 6,
    "27": "Send current restricted promotional credits",
    "2A": 6,
    "2B": 6,
    "2C": "Send current hopper level (coins)",
    "46": 6,
    "47": 6,
    "48": 8,
    "49": 6,
    "4F": 7,
    "51": 4,
    "54": 15,
    "55": 4,
    "56": 124,
    "57": 8,
    "70": "Send ticket validation data",
    "71": "Send current date and time",
    "84": "Send progressive win amount",
    "85": "Send SAS progressive win amount",
    "87": "Send multiple SAS progressive win amounts",
    "8E": "Send card information",
    "8F": "Send reel stop information",
    "90": 6,
    "9475CB": "Reset hand pay",
    "B1": "Send current player denomination",
    "B2": "Send enabled player denominations",
    "B3": "Send token denomination"
}

# Lets init the configuration file
config_handler = ConfigHandler()
config_handler.read_config_file()

sas = Sas(
    port=config_handler.get_config_value("connection", "serial_port"),
    timeout=config_handler.get_config_value("connection", "timeout"),
    poll_address=config_handler.get_config_value("events", "poll_address"),
    denom=config_handler.get_config_value("machine", "denomination"),
    asset_number=config_handler.get_config_value("machine", "asset_number"),
    reg_key=config_handler.get_config_value("machine", "reg_key"),
    pos_id=config_handler.get_config_value("machine", "pos_id"),
    key=config_handler.get_config_value("security", "key"),
    debug_level="DEBUG",
    perpetual=config_handler.get_config_value("connection", "infinite"),
)

sas.open()
print("Port opened")

request_tx = "01"

request_switch = False
command = ""
clean_last_sas_log()

with open(output_file_translated, "w") as f:
    # Redirect stdout to the file
    sys.stdout = f

    print("Start: " + get_request_time() + "\n")

    # Code that prints output goes here
    while True:
        current_comm = sas.connection.read().hex().upper()
        request_time = get_request_time()

        if request_switch:
            if current_comm == request_tx:
                print(f"{request_time}")
                print("SMIB => Machine:")
                print("Unknown. Request and response are most likely merged: " + "01" + command)
                print()
                handle_hex_log(request_time, "01" + command)
                command = ""
                continue
            command += current_comm
            if command in requests:
                print(f"{request_time}")
                print("SMIB => Machine:")
                print(requests[command])

                # Handle hex output
                handle_hex_log(request_time, request_tx + command)

                hex_data = sas.connection.read(expected_reply[command]).hex()
                # Get time after reading bytes
                response_time = get_request_time()
                print(response_time)

                # Handle hex output
                handle_hex_log(response_time, hex_data)

                return_data = split_string_into_chunks(hex_data)
                match command:
                    case "0F":
                        print("Machine => SMIB:" + "\n" + "Total Cancelled Credits Meter: " + return_data[
                            0] + "\n" + "Total Coin In Meter: " + return_data[1] + "\n" + "Total Coin Out Meter: " +
                              return_data[2] + "\n" + "Total Drop Meter: " + return_data[
                                  3] + "\n" + "Total Jackpot Meter: " + return_data[4] + "\n" + "Games Played Meter: " +
                              return_data[5] + "\n")
                    case "1A":
                        print("Machine => SMIB:" + "\n" + "Current Credits: " + return_data[0] + "\n")
                    case "55":
                        print("Machine => SMIB:" + "\n" + "Selected game number: " + return_data[0] + "\n")
                    case _:
                        print(hex_data)
                command = ""
                request_switch = False
        if not request_switch and current_comm == request_tx:
            request_switch = True

    # Reset stdout to its original value (optional)
    sys.stdout = sys.__stdout__

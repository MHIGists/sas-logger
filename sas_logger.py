import datetime
import sys
import dictionaries
import signal
import zipfile
import os
from sas import Sas
from config_handler import *

output_file_byte = "sas_output_byte.txt"
stop_signal = False

#signal handler function
def SignalHandler_SIGINT(SignalNumber,Frame):
    stop_signal = True
    with zipfile.ZipFile("sas_output.zip", "w") as zip_file:
        zip_file.write(output_file_byte, compress_type=zipfile.ZIP_DEFLATED)
    os.remove(output_file_byte)
    exit()
    
#register the signal with Signal handler
signal.signal(signal.SIGINT,SignalHandler_SIGINT)

def get_microsecond_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def handle_hex_log(time, command_text, is_response=False, is_unknown=False):
    if is_unknown:
        print("The following is unknown data:")
    if is_response:
        print("Machine response:")
    if not is_response and not is_unknown:
        print("SMIB request:")
    print(time)
    print(command_text)


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
unknown = ""

with open(output_file_byte, "w") as f:
    # Redirect stdout to the file
    sys.stdout = f

    print("Start: " + get_microsecond_time() + "\n")

    # Code that prints output goes here
    while True:
        if stop_signal == True:
            break
        comm_1 = sas.connection.read().hex().upper()
        comm_2 = sas.connection.read().hex().upper()
        request_time = get_microsecond_time()
        
        current_pair = comm_1 + comm_2
        if comm_2 == "01" and comm_1 != "01":
            comm_3 = sas.connection.read().hex().upper()
            current_pair = comm_2 + comm_3
        if comm_1 != "01" and comm_2 != "01":
            unknown += comm_1 + comm_2
            continue
        if unknown != "":
            handle_hex_log(get_microsecond_time(), unknown, False, True)
            unknown = ""
            print()
        
        if current_pair in dictionaries.requests:
            # Handle hex output
            handle_hex_log(request_time, current_pair, False)
            response = sas.connection.read(dictionaries.expected_reply[current_pair]).hex().upper()
            # Handle hex output
            handle_hex_log(get_microsecond_time(), response, True)
            print()
            continue
        if current_pair in dictionaries.requests_with_input:
            command_buffer = current_pair
            current_pair += sas.connection.read(dictionaries.requests_with_input[current_pair]["bits"]).hex().upper()
            handle_hex_log(get_microsecond_time(), current_pair, False)
            response = sas.connection.read(dictionaries.expected_reply[command_buffer]).hex().upper()
            handle_hex_log(get_microsecond_time(), response, True)
            print()
            continue
         



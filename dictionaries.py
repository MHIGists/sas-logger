# Bits means how many pair of bits is the command long itself after the flag example if it's 7 bits: 01 08 |7bits
# from the command => 00 00 00 00 00 00 00
requests_with_input = {
    "0108": {
        "command_name": "Configure bill denominations",
        "bits": 7
    },
    "0109": {
        "command_name": "Enable/disable game number",
        "bits": 5
    },
    "010C": {
        "command_name": "Set sound",
        "bits": 6,
    },
    "010D": {
        "command_name": "Play sound",
        "bits": 6
    },
    "010E": {
        "command_name": "Enable/disable real time event reporting",
        "bits": 3
    },
    "0121": {
        "command_name": "ROM signature verification",
        "bits": 4
    },
    "012D": {
        "command_name": "Send total hand paid cancelled credits for game number",
        "bits": 4
    },
    "012E": {
        "command_name": "Delay the gaming machine by x amount of milliseconds",
        "bits": 4
    },
    "012F": {
        "command_name": "Send selected meters for game n",
        "bits": 6
    },
    "014C": {
        "command_name": "Set enhanced validation ID",
        "bits": 8
    },
    "014D": {
        "command_name": "Set enhanced validation info",
        "bits": 3
    },
    "0150": {
        "command_name": "Send validation meters",
        "bits": 3
    },
    "016F": {
        "command_name": "Extended Meters",
        "bits": 7
    },
    "0172": {
        "command_name": "AFT",
        "bits": 70
    },
    "0173": {
        "command_name": "AFT register gaming machine",
        "bits": 2
    },
    "0174": {
        "command_name": "AFT register gaming machine",
        "bits": 3
    },
    "017B": {
        "command_name": "AFT register gaming machine",
        "bits": 5
    },
}

requests = {
    "0101": "Lock Machine",
    "0102": "Unlock Machine",
    "0103": "Disable all sound",
    "0104": "Enable all sound",
    "0105": "Disable reel spin sound",
    "0106": "Enable bill acceptor",
    "0107": "Disable bill acceptor",
    "010A": "Enter maintenance mode",
    "010B": "Exit maintenance mode",
    "010F": "Send meters 10 trough 15",
    "0110": "Send cancelled coin meter",
    "0111": "Send total coins in meter",
    "0112": "Send total coin out meter",
    "0113": "Send total drop meter",
    "0114": "Send total jackpot meter",
    "0115": "Send games played meter",
    "0116": "Send games won meter",
    "0117": "Send games lost meter",
    "0118": "Send games since last power up and door closure",
    "0119": "Send meters 11 trough 15",
    "011A": "Current credits",
    "011B": "Send hand pay information",
    "011C": "Send meters",
    "011D": "Send bill meters (# of bills)",
    "011F": "Send gaming machine ID & information",
    "0120": "Send dollar value of bills meter",
    "0127": "Send current restricted promotional credits",
    "012A": "Send true coin in meter (coins)",
    "012B": "Send true coin out meter (coins)",
    "012C": "Send current hopper level (coins)",
    "0131": "Send 1 bills in meter",
    "0132": "Send 2 bills in meter",
    "0133": "Send 5 bills in meter",
    "0134": "Send 10 bills in meter",
    "0135": "Send 20 bills in meter",
    "0136": "Send 50 bills in meter",
    "0137": "Send 100 bills in meter",
    "0138": "Send 500 bills in meter",
    "0139": "Send 1000 bills in meter",
    "013A": "Send 200 bills in meter",
    "013B": "Send 25 bills in meter",
    "013C": "Send 2000 bills in meter",
    "013D": "Send cashout ticket information",
    "013E": "Send 2500 bills in meter",
    "013F": "Send 5000 bills in meter",
    "0140": "Send 10000 bills in meter",
    "0141": "Send 20000 bills in meter",
    "0142": "Send 25000 bills in meter",
    "0143": "Send 50000 bills in meter",
    "0144": "Send 100000 bills in meter",
    "0145": "Send 250 bills in meter",
    "0146": "Send credit amount of all bills accepted",
    "0147": "Send coin amount from an external coin acceptor",
    "0148": "Send last accepted bill information",
    "0149": "Send number of bills currently in stacker",
    "014A": "Send credit amount of bills currently in stacker",
    "014F": "Send current hopper status",
    "0151": "Send total number of games implemented",
    "0154": "Send SAS version and machine serial number",
    "0155": "Send selected game number",
    "0156": "Send enabled game numbers",
    "0157": "Send pending cashout info",
    "0170": "Send ticket validation data",
    "0171": "Send current date and time",
    "0184": "Send progressive win amount",
    "0185": "Send SAS progressive win amount",
    "0187": "Send multiple SAS progressive win amounts",
    "018E": "Send card information",
    "018F": "Send reel stop information",
    "0190": "Send legacy bonus win amount",
    "019475CB": "Reset hand pay",
    "01B1": "Send current player denomination",
    "01B2": "Send enabled player denominations",
    "01B3": "Send token denomination"
}
expected_reply = {
    "0108": 1,
    "0109": 1,
    "010C": 8,
    "010D": 8,
    "010E": 3,
    "010F": 26,
    "0110": 6,
    "0111": 6,
    "0112": 6,
    "0113": 6,
    "0114": 6,
    "0115": 6,
    "0116": 6,
    "0117": 6,
    "0118": 6,
    "0119": 22,
    "011A": 6,
    "011B": 22,
    "011C": 34,
    "011E": 26,
    "011F": 22,
    "0120": 6,
    "0121": 8,
    "0127": 0,
    "012A": 6,
    "012B": 6,
    "012C": 0,
    "012D": 8,
    "012E": 8,
    "012F": 8,
    "0131": 6,
    "0132": 6,
    "0133": 6,
    "0134": 6,
    "0135": 6,
    "0136": 6,
    "0137": 6,
    "0138": 6,
    "0139": 6,
    "013A": 6,
    "013B": 6,
    "013C": 6,
    "013E": 6,
    "013F": 6,
    "0140": 6,
    "0141": 6,
    "0142": 6,
    "0143": 6,
    "0144": 6,
    "0145": 6,
    "0146": 6,
    "0147": 6,
    "0148": 8,
    "0149": 6,
    "014A": 6,
    "014C": 8,
    "014D": 8,
    "014F": 7,
    "0150": 8,
    "0151": 4,
    "0152": 20,
    "0154": 18,
    "0155": 4,
    "0156": 124,
    "0157": 8,
    "016F": 8,
    "0170": 0,
    "0171": 19,
    "0172": 80,
    "0184": 9,
    "0185": 9,
    "0187": 5,
    "018E": 0,
    "018F": 0,
    "0190": 6,
    "019475CB": 3,
    "01B1": 3,
    "01B2": 8,
    "01B3": 3,
    "0173": 32,
    "0174": 38,
    "017B": 10
}
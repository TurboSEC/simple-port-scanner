    1 # Simple Python Port Scanner                                                                │
│     2                                                                                             │
│     3 A basic, educational-purpose port scanner written in Python. This script checks for open    │
│       TCP ports on a specified IP address within a given range.                                   │
│     4                                                                                             │
│     5 ## Description                                                                              │
│     6                                                                                             │
│     7 This tool iterates through a range of ports (by default, 1-1023) on a target IP address (by │
│       default, `127.0.0.1`). It attempts to establish a connection on each port to determine if   │
│       it is open or closed. A timeout is implemented to ensure the scan runs efficiently without  │
│       getting stuck on unresponsive ports.                                                        │
│     8                                                                                             │
│     ## Features                                                                                 │
│    10                                                                                             │
│    11 -   Scans a user-defined range of ports.                                                    │
│    12 -   Reports the status (open/closed) of each port.                                          │
│    13 -   Uses a socket timeout for faster scanning.                                              │
│    14 -   Lightweight and easy to modify.                                                         │
│    15                                                                                             │
│    16 ## How to Use                                                                               │
│    17                                                                                             │
│    18 1.  Save the code into a file named `port_scanner.py`.                                      │
│    19 2.  Open your terminal or command prompt.                                                   │
│    20 3.  Run the script using Python:                                                            │
│    21     ```bash                                                                                 │
│    22     python port_scanner.py                                                                  │
│    23     ```                                                                                     │
│    24 4.  The script will print the status of each port in the console. You can modify the `ip`   │
│       variable and the `range` in the `for` loop to scan different targets and port ranges.       │
│    25                                                                                             │
│    26 ---                                                                                         │
│    27                                                                                             │
│    28 ## ⚠️ Disclaimer                                                                           │
│    29                                                                                             │
│    30 **This tool is for educational purposes only.**                                             │
│    31                                                                                             │
│    32 Unauthorized port scanning of networks or systems is illegal. Only use this script to scan  │
│       systems and networks that you own or have explicit, written permission to test. The author  │
│       is not responsible for any misuse or damage caused by this script.     

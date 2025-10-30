✦ Simple Python Port Scanner

  A basic, educational-purpose port scanner written in Python. This script checks for open TCP ports
  on a specified IP address within a given range.

  Description

  This tool iterates through a range of ports (by default, 1-1023) on a target IP address (by
  default, 127.0.0.1). It attempts to establish a connection on each port to determine if it is open
  or closed. A timeout is implemented to ensure the scan runs efficiently without getting stuck on
  unresponsive ports.

  Features

   - Scans a user-defined range of ports.
   - Reports the status (open/closed) of each port.
   - Uses a socket timeout for faster scanning.
   - Lightweight and easy to modify.

  How to Use

   1. Save the code into a file named port_scanner.py.
   2. Open your terminal or command prompt.
   3. Run the script using Python:
   1     python port_scanner.py
   4. The script will print the status of each port in the console. You can modify the ip variable and
      the range in the for loop to scan different targets and port ranges.

  ---

  ⚠️ Disclaimer

  This tool is for educational purposes only.

  Unauthorized port scanning of networks or systems is illegal. Only use this script to scan systems
  and networks that you own or have explicit, written permission to test. The author is not
  responsible for any misuse or damage caused by this script.

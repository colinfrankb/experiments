- linux exposes devices as files
- All serial ports are represented as device files
- list all serial devices
  - ls /dev/tty*

- The dmesg command shows kernel messages, including when serial devices are connected.
  - dmesg | grep tty
  - dmesg | grep -E 'ttyUSB|ttyACM'

- use udevadm to get details about connected serial devices:
  - udevadm info -q all -n /dev/ttyACM0

- The /dev/serial/by-id/ directory contains symbolic links with human-readable names that often include the manufacturer and model.
  - ls -l /dev/serial/by-id/

- test communicatoin
  - screen /dev/ttyACM0 9600

- list open files `lsof`, will display if any processes have the device file open
  - lsof /dev/ttyS0

- Connected Serial Ports are associated to a site, so even if you use multiple tabs, they will all have access to the accepted serial ports, but only one tab can have an open connection to a serial port, which makes sense

- https://developer.chrome.com/docs/capabilities/serial#open-port
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API
While readable is locked, the serial port can't be closed.

- chrome://device-log/

Surname MC CREE - Last Name
Names VIRGINIA ELIZABETH - First Name
Sex F - Gender
Nationality RSA - Nationality
Identity Number 5906220141082 - Id Number
Day of Birth 22 JUN 1959 - Date of Birth
Country of Birth RSA
Status CITIZEN
Date of Issue 03 JUL 2018

MC CREE|VIRGINIA ELIZABETH|F|RSA|5906220141082|22 JUN 1959|RSA|CITIZEN|03 JUL 2018|41954|108121210|123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
MC CREE|VIRGINIA ELIZABETH|F|RSA|5906220141082|22 JUN 1959|RSA|CITIZEN|03 JUL 2018|41954|108121210|123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
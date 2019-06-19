# Example of using Python3 to parse an Nginx access log to view the top 10 source IP addresses

## Requirements
- Pre-req is to have an offline copy of the logs to parse.  You can `tailf /PATH/TO/YOURFILE > yourfile` to obtain this.

- Python3

## Example usage

Be sure to use the --log

```
python3 top-ip.py --log access.log

('192.168.22.235', 684)
('192.168.22.57', 115)
('10.159.139.26', 111)
('192.168.20.90', 106)
('192.168.18.55', 102)
('192.168.22.203', 92)
('192.168.23.91', 79)
('192.168.23.86', 70)
('192.168.22.164', 69)
('192.168.18.32', 57)
```

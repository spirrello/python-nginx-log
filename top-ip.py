#!/usr/bin/env python3
"""
Example of how to parse an nginx access log to find the top 10 IP addresses
"""


import argparse
import re


def getArgs():
    """
    Provie arguments
    """
    parser = argparse.ArgumentParser(
           description='script for finding top ip addresses')


    parser.add_argument('--log', required=False, default = 'access.log', action='store',
                           help='File containing logs')

    parser.add_argument('--top', required=False, default = 10, action='store',
                           help='Top x of ip adddresses to view.')

    config_args = parser.parse_args()

    return config_args



def main():

    #Fetch the args
    configArgs = getArgs()

    #Access log to view, default is access.log
    try:
        nginxAccessLog = open(configArgs.log, "r")
    except Exception as err:
        print("Error opening file:\n{}".format(err))
        sys.exit(1)


    ipList = []
    ipStats = {}
    for line in nginxAccessLog:
        ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip != None:
            ipList.append(ip.group())

    for ip in ipList:
        ipStats.update({ip:ipList.count(ip)})

    #Need to sort the dictionary
    sortedIpStats = [(ipAddr, ipStats[ipAddr]) for ipAddr in sorted(ipStats, key=ipStats.get, reverse=True)]

    #We'll now print a sorted list of the top x IP addreses
    ipIndex = 0
    for ip in range(configArgs.top):
        print(sortedIpStats[ipIndex])
        ipIndex += 1



if __name__ == "__main__":
    main()
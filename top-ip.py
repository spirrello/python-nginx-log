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


def createSourceIPList(nginxAccessLog):
    """
    Extract the source IP addresses
    """
    sourceIPList = []

    for line in nginxAccessLog:
        ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip != None:
            sourceIPList.append(ip.group())

    return sourceIPList


def createSourceIPStats(sourceIPList):
    """
    Create dictionary for source IP stats and sort the list.
    """
    sourceIPStats = {}

    for ip in sourceIPList:
        sourceIPStats.update({ip:sourceIPList.count(ip)})

    #Need to sort the dictionary
    sortedsourceIPStats = [(ipAddr, sourceIPStats[ipAddr]) for ipAddr in sorted(sourceIPStats, key=sourceIPStats.get, reverse=True)]

    return sortedsourceIPStats



def main():

    #Fetch the args
    configArgs = getArgs()

    #Access log to view, default is access.log
    try:
        nginxAccessLog = open(configArgs.log, "r")
    except Exception as err:
        print("Error opening file:\n{}".format(err))
        sys.exit(1)


    #Fetch list of source IP addresses
    sourceIPList = createSourceIPList(nginxAccessLog)

    #Fetch the sorted list with stats
    sortedsourceIPStats = createSourceIPStats(sourceIPList)


    #We'll now print a sorted list of the top x IP addreses
    for ip in range(configArgs.top):
        print(sortedsourceIPStats[ip])




if __name__ == "__main__":
    main()
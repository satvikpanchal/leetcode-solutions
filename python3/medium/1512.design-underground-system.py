# LeetCode Solution
# Problem: 1512. Design Underground System
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/design-underground-system/
# Submitted: 2025-11-05 01:22:34 UTC
# Status: Accepted

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.customerTrack = {}
        self.averageTime = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # add info in the customerTrack hashmap
        if id not in self.customerTrack:
            self.customerTrack[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # adding the startStation and endStation name and time in the averageTime hashmap
        bothStations = ""

        if id in self.customerTrack:
            bothStations += self.customerTrack[id][0] + "." + stationName
            timeDiff = t - self.customerTrack[id][1]

            self.averageTime[bothStations].append(timeDiff)
            # if bothStations not in self.averageTime:
            #     self.averageTime[bothStations] = [timeDiff]
            # else:
            #     self.averageTime[bothStations].append(timeDiff)

        # delete based on the id from the customerTrack hashmap
        del self.customerTrack[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        bothStation = ""
        bothStation += startStation + "." + endStation

        if bothStation in self.averageTime:
            average = sum(self.averageTime[bothStation]) / len(self.averageTime[bothStation])

            return average
            
        return

# hashmap:
# key: id
# value: list of station name and time

# hashmap:
# key: string combo startStation and endStation    Leyton, Waterloo k: LeytonWaterloo
# value: a list of time differences from start station and end station.   v: [12]

# checkIn: add the kv pair in the hashmap everytime the method is called
# checkOut: remove the kv pair in the hashmap, everytime its called
# getAvg: see if that combination exists in the hashmap, if it does, then return the avg as a double


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# 45, a, 3
# 32, aa, 8
# 27, a, 10
# 45, ab, 15
# 27, ab, 20
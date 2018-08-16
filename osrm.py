# -*- coding: utf-8 -*-


import json
from geopy.distance import vincenty
import os
import sqlite3
import requests


class OSRM():
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(dir_path + "/db.sqlite")

    def __del__(self):
        self.conn.close()

    def __getdistance__(self, route):
        total_distance = 0
        old_lat = 0
        old_lon = 0
        for r_index, node in enumerate(route):
            lat = node[1]
            lon = node[0]
            if old_lat != 0 and old_lon != 0:
                total_distance += vincenty((old_lat, old_lon), (lat, lon)).meters
            old_lat = lat
            old_lon = lon
        return total_distance

    def __route__(self, lat1, lon1, lat2, lon2):
        result = dict()
        result["result"] = "failure"

        max_distance = 10 ** 8
        interval = 0.0002
        start_lat, start_lon = lat1, lon1

        # center
        j = requests.get('http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (lon1, lat1, lon2, lat2),
                         params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    start_lat, start_lon = lat1, lon1
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # center -- end

        # up
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (lon1, lat1 + interval, lon2, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    start_lat, start_lon = lat1 + interval, lon1
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # up -- end

        # down
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (lon1, lat1 - interval, lon2, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    start_lat, start_lon = lat1 - interval, lon1
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # down -- end

        # left
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (lon1 - interval, lat1, lon2, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    start_lat, start_lon = lat1, lon1 - interval
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # left -- end

        # right
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (lon1 + interval, lat1, lon2, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    start_lat, start_lon = lat1, lon1 + interval
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # right -- end

        # endup
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (
            start_lon, start_lat, lon2, lat2 + interval),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # endup -- end

        # enddown
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (
                start_lon, start_lat, lon2, lat2 - interval),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # enddown -- end

        # endleft
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (
                start_lon, start_lat, lon2 - interval, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # endleft -- end

        # endright
        j = requests.get(
            'http://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f' % (
                start_lon, start_lat, lon2 + interval, lat2),
            params={'geometries': 'geojson'}).json()
        if j["code"] == "Ok":
            try:
                route = j["routes"][0]["geometry"]["coordinates"]
                route[0] = [lon1, lat1]
                route[-1] = [lon2, lat2]
                distance = self.__getdistance__(route)
                if max_distance > distance:
                    max_distance = distance
                    result["route"] = route
                    result["result"] = "success"
            except:
                pass
        # endright -- end

        return result

    def route(self, lat1, lon1, lat2, lon2):
        result = None
        sql = "SELECT route FROM osrm WHERE lat1 = %f AND lon1 = %f AND lat2 = %f AND lon2 = %f LIMIT 1" % (
            lat1, lon1, lat2, lon2)

        for row in self.conn.execute(sql):
            result = json.loads(row[0])
            break

        if result is None:
            route = self.__route__(lat1, lon1, lat2, lon2)

            if route["result"] == "success":

                jsonroute = dict()
                jsonroute["result"] = "success"

                # total_distance
                total_distance = self.__getdistance__(route["route"])
                jsonroute["distance"] = total_distance
                # total distance -- end

                # route
                jsonroute["route"] = []
                old_lat = 0
                old_lon = 0
                distance = 0
                for r_index, node in enumerate(route["route"]):
                    lat = node[1]
                    lon = node[0]
                    if old_lat != 0 and old_lon != 0:
                        distance += vincenty((old_lat, old_lon), (lat, lon)).meters
                        rate = distance / total_distance
                        jsonroute["route"].append([lat, lon, distance, rate, r_index])
                    else:
                        jsonroute["route"].append([lat, lon, 0., 0., r_index])
                    old_lat = lat
                    old_lon = lon
                    # route -- end

                    route = jsonroute

                sql = "INSERT INTO osrm(lat1, lon1, lat2, lon2, route) VALUES (%f, %f, %f, %f, '%s')" % (
                    lat1, lon1, lat2, lon2, json.dumps(route))
                self.conn.execute(sql)
                self.conn.commit()

                result = jsonroute
            else:
                result = '{result:"no_route"}'

        return result


if __name__ == "__main__":
    router = OSRM()
    rs = router.route(34.91938, 137.167146, 34.92273, 137.166829)
    print(rs)

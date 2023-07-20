from flask import Flask, request
from flask_cors import CORS
from pathlib import Path


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return """
           <h1>API</h1>
           /wrf/times = list of model init times
           /wrf/domains = list of map domains
           /wrf/stations = list of sounding stations
           /wrf/products = wrf products
           """


@app.route("/wrf", methods=["GET"])
def wrf():
    return """
           <h1>WRF API</h1>
           /wrf/times = list of model init times
           /wrf/domains = list of map domains
           /wrf/stations = list of sounding stations
           /wrf/products = wrf products
           """


@app.route("/wrf/times", methods=["GET"])
def wrf_times():
    try:
        data = Path("init_times.json").read_text()
        return data
    except:
        return """
               <h1>WRF API</h1>
               Invalid Request
               """


@app.route("/wrf/domains", methods=["GET"])
def wrf_domains():
    try:
        data = Path("wrf_domains.json").read_text()
        return data
    except:
        return """
               <h1>WRF API</h1>
               Invalid Request
               """

@app.route("/wrf/stations", methods=["GET"])
def wrf_stations():
    try:
        data = Path("wrf_stations.json").read_text()
        return data
    except:
        return """
               <h1>WRF API</h1>
               Invalid Request
               """
@app.route("/wrf/products", methods=["GET"])
def wrf_products():
    try:
        data = Path("wrf_products.json").read_text()
        return data
    except:
        return """
               <h1>WRF API</h1>
               Invalid Request
               """

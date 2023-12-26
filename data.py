from flask import Flask, request, send_file
from flask_cors import CORS
from pathlib import Path


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return """
           <h1>API</h1>
           /wrf/times = list of model init times</br>
           /wrf/domains = list of map domains</br>
           /wrf/stations = list of sounding stations</br>
           /wrf/products = wrf products</br>
           /wrf/images = wrf images</br>
           /wrf/time_series = wrf time series</br>
           """


@app.route("/wrf", methods=["GET"])
def wrf():
    return """
           <h1>WRF API</h1>
           /wrf/times = list of model init times</br>
           /wrf/domains = list of map domains</br>
           /wrf/stations = list of sounding stations</br>
           /wrf/products = wrf products</br>
           /wrf/images = wrf images</br>
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


@app.route("/wrf/images", methods=["GET"])
def wrf_images():
    try:
        req = dict(request.values)
        domain = req.get("domain")
        ens = req.get("ens")
        fcst_date = req.get("fcst_date")
        init_date = req.get("init_date")
        product = req.get("product")
        return send_file(
            f"images_wrf/{init_date}/{ens}/{product}/{domain}/{product}_{domain}_{fcst_date}.png",
            download_name=f"{product}_{domain}_{fcst_date}.png")
    except:
        return """
               <h1>WRF API</h1>
               ?domain = domain</br>
               ?ens = ensemble member</br>
               ?fcst_date = forecast date (YYYYMMDDHHmm)</br>
               ?init_date = initialized date (YYYYMMDDHH)</br>
               ?product = product</br>
               """


@app.route("/wrf/time_series", methods=["GET"])
def wrf_time_series():
    try:
        req = dict(request.values)
        domain = req.get("domain")
        ens = req.get("ens")
        init_date = req.get("init_date")
        return send_file(
            f"images_wrf/{init_date}/{ens}/time_series/{domain}/time_series.json",
            download_name=f"time_series_{domain}_{init_date}.json")
    except:
        return """
               <h1>WRF API</h1>
               ?domain = domain</br>
               ?ens = ensemble member</br>
               ?init_date = initialized date (YYYYMMDDHH)</br>
               """

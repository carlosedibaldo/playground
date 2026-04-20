# NOTE: ROOT_DIR empty to anonymize submission
ROOT_DIR = ""
CSV_PATHS = {
    "crime": f"{ROOT_DIR}/csv/crime_2026.csv",
    "stops": f"{ROOT_DIR}/csv/stops_2026.csv",
    "income": f"{ROOT_DIR}/csv/IncomeData.csv",
    "courts": f"{ROOT_DIR}/csv/CourtsData1.csv",
    "appraisal": f"{ROOT_DIR}/csv/RESIDENTIAL_CAMA.csv",
    "population": f"{ROOT_DIR}/csv/fred_dc_population.csv",
}

GEOJSON_PATHS = {
    "address_points": f"{ROOT_DIR}/geojson/Address_Points.geojson",
    "bike_lanes": f"{ROOT_DIR}/geojson/Bicycle_Lanes.geojson",
    "bike_share_locations": f"{ROOT_DIR}/geojson/Capital_Bike_Share_Locations.geojson",
    "housing_characteristics": f"{ROOT_DIR}/geojson/Housing_Characteristics_DC_Census_Tracts.geojson",
}

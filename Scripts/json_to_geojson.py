import json
import geojson

def create_geojson(inp):
    '''
    Takes the JSON File and creates a GeoJSON file
    *note chatgpt was largely used to help with this function*
    :param inp:
    :return:
    '''
    with open(inp, 'r') as file:
        data = json.load(file)
    features = []
    for line in data:
        try:
            lon = float(line["Long"])
            lat = float(line["Lat"])
        except Exception as e:
            print("lat or long is not valid")
        else:
            point = geojson.Point((lon, lat))
            resort = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "Name": line.get("Name"),
                    "Address": line.get("Address "),
                    "City": line.get("City"),
                    "Zip Code": line.get("Zip Code"),
                    "Plus Code": line.get("Plus Code"),

                    "Lift Ticket Price": line.get("Lift Ticket Price (1 Day Adult on Jan 8th 2026)"),
                    "Rental Price": line.get("Rental Prices (Assuming Skis, Boots, Poles, Helmet)"),

                    "Total Trails": int(line.get("Total Trails")),
                    "Total Skiable Acres": int(line.get("Total Skiable Acres ")),
                    "Vertical Drop": int(line.get("Vertical Drop (in feet)")),
                    "Highest Peak": int(line.get("Highest Peak (in feet)")),

                    "Green Trails": float(line.get("# Green Circle")),
                    "Blue Trails": float(line.get("# Blue Square")),
                    "Black Trails": float(line.get("# Black Diamond")),
                    "Double Black Trails": float(line.get("# Double Black Diamond")),

                    "Terrain Parks": int(line.get("# Terrain parks")),
                    "Glades": int(line.get("# Glades ")),
                    "Night Skiing": line.get("Night Skiing offered?"),
                    "Indy Pass": line.get("Indy Pass?") == "Yes",
                    "Sources": line.get("Sources")
                }

            }
            features.append(resort)
            geojson_data = {
                "type": "FeatureCollection",
                "features": features
            }

            # Write output file
            with open("DataV2.geojson", "w", encoding="utf-8") as f:
                json.dump(geojson_data, f, indent=4)

            print(f"✅ Total Resorts Exported: {len(features)}")

if __name__ == '__main__':
    """ Main Method
            :arg none
            :return none
        """
    inp = input("Enter File Name: ")
    try:
        file = open(inp)
    except FileNotFoundError:
        print("File Not Found")
    else:
        file.close()
        create_geojson(inp)

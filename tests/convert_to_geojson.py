import query
import os
import json
key = os.environ.get('PETFINDER_KEY')
secret_key = os.environ.get('PETFINDER_SECRET_KEY')



def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        description_str = "<strong>"+feature["properties"]["name"]+"</strong><br>"+feature["properties"]["age"]+" "+feature["properties"]["gender"]+"<br>"+feature["properties"]["breeds.primary"]
        feature['properties']['description']=description_str
        feature['properties']['image']=feature['properties']['primary_photo_cropped.small']
        geojson['features'].append(feature)

    return geojson




def write_file(pets):

    pf = query.authenticate(key, secret_key)
    
    useful_cols = ["age", "gender", "size", "name", "breeds.primary", "primary_photo_cropped.small"]
    geojson_dict = df_to_geojson(df=pets, properties=useful_cols,lat="contact.address.lat",lon="contact.address.long")
    

    geojson_str = json.dumps(geojson_dict, indent=2)
    output_filename = 'pet_results.geojson'
    with open(os.path.join("../petsite/static/js/",output_filename), 'w') as output_file:
        output_file.write('{}'.format(geojson_str))


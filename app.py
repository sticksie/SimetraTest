from flask import Flask
import os
from PostcodeHub import *


app = Flask(__name__)

@app.route('/')
def index():
    res = []
    hub = PostcodeHub('xml')
    res.append( hub.getAddressByPostcode('test_full', 'asnkD61iH1SGO2l', 'YO62 7TU') )
    res.append( hub.getAddressByStreet('test_full', 'asnkD61iH1SGO2l', 'Old Town Street', 'Plymouth') )
    res.append( hub.getGeoDataByPostcode('test_geo', 'asnkD61iH1SGO2l', 'YO62 7TU') )
    res.append( hub.getGeoDataByPosition('test_geo', 'asnkD61iH1SGO2l', '50.370324946997', '-4.1381841195554') )
    res.append( hub.getGeoDataByLocation('test_geo', 'asnkD61iH1SGO2l', '247964', '54523') )
    res.append( hub.getCredits('test_full', 'asnkD61iH1SGO2l') )
    return ''.join(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='127.0.0.1', port=port)
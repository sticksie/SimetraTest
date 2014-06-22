import urllib

class PostcodeHub:

    def __init__(self, format = 'xml'):
        self.apiUrl = 'http://postcodehub.co.uk/api/?%s&%s'
        self.output_format = format

    def getAddressByPostcode(self, username, password, postcode):
        params = {
            'user': username,
            'pass': password,
            'postcode': postcode,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getAddressDetails', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getAddressByPostcode:', ex
            raise
        return data
        
    def getAddressByStreet(self, username, password, street, town):
        params = {
            'user': username,
            'pass': password,
            'street': street,
            'town': town,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getAddressDetails', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getAddressByStreet:', ex
            raise
        return data
    
    def getGeoDataByPostcode(self, username, password, postcode):
        params = {
            'user': username,
            'pass': password,
            'postcode': postcode,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getGeoData', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getGeoDataByPostcode:', ex
            raise
        return data

    def getGeoDataByPosition(self, username, password, latitude, longitude):
        params = {
            'user': username,
            'pass': password,
            'lat': latitude,
            'lon': longitude,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getGeoData', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getGeoDataByPosition:', ex
            raise
        return data
        
    def getGeoDataByLocation(self, username, password, eastings, northings):
        params = {
            'user': username,
            'pass': password,
            'eastings': eastings,
            'northings': northings,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getGeoData', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getGeoDataByLocation:', ex
            raise
        return data

    def getCredits(self, username, password):
        params = {
            'user': username,
            'pass': password,
            'format': self.output_format }
        query_string = urllib.urlencode(params)
        try:
            data = urllib.urlopen(self.apiUrl % ('getCredits', query_string)).read()
        except Exception as ex:
            print 'error in PostCodeHub.getCredits:', ex
            raise
        return data


if __name__ == '__main__':
    pass


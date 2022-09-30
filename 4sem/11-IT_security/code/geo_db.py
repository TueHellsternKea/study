import geoip2.webservice


# p7o4YM9dGv7aujF7
# OCzDNvd59Kg6Q09o
with geoip2.webservice.Client(42, 'p7o4YM9dGv7aujF7') as client:
    response = client.city('203.0.113.0')
    print(response.country.iso_code)
    print(respons.country.name)


    
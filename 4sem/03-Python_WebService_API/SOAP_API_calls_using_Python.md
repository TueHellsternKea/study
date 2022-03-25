[Home](./README.md)

# SOAP API calls using Python
SOAP stands for [Simple Object Access Protocol](https://www.geeksforgeeks.org/basics-of-soap-simple-object-access-protocol/), as the name suggests nothing but a protocol for exchanging structured data between nodes. It uses XML instead of JSON.

To make SOAP requests to the SOAP API endpoint, use the "*Content-Type: application/soap+xml*" request header, which tells the server that the request body contains a SOAP envelope. 

The server informs the client that it has returned a SOAP envelope with a "*Content-Type: application/soap+xml*" response header. 

# Zeep
Zeep is a Python SOAP client

[docs.python-zeep.org/en/master](https://docs.python-zeep.org/en/master/)

Zeep inspects the **WSDL** document and generates the corresponding code to use the services and types in the document. This provides an easy to use programmatic interface to a SOAP server.

You have to install the Zeep module

    pip3 install zeep

# Country phone code example
We are using SOAP to get the phone dialing code from the Country code - Like *DK* - Returns *45*

- Set the **WSDL URL**. You can get the **WSDL URL** simply by visiting the base URL and click on Service Description. That will take you to the **WSDL URL**. The base URL will be service_url and append the service name after the base URL.
- You need to create a **header element**. Set the header element with **method_url** and **service_url**.
- Initialize a **zeep** client with the **WSDL URL**.
- The setup is done, just call the *zeep service* with the service name, here the service name is **CountryIntPhoneCode**. You need to pass the parameters with the country_code and also pass the header to **_soapheaders** as a list.
- This returns the phone code of the country.

## The Python code
- [github.com/TueHellsternKea/SOAP-Country-Demo](https://github.com/TueHellsternKea/SOAP-Country-Demo)
- [phone_country_code.py](./codefiles/phone_country_code.py)

```python
import zeep

# Set the WSDL URL
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Set method URL
method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"

# Set service URL
service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Create the header element
header = zeep.xsd.Element(
	"Header",
	zeep.xsd.ComplexType(
		[
			zeep.xsd.Element(
				"{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
			),
			zeep.xsd.Element(
				"{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
			),
		]
	),
)
# Set the header value from header element
header_value = header(Action=method_url, To=service_url)

# Initialize zeep client
client = zeep.Client(wsdl=wsdl_url)

# Set country code for Denmark
# Just change to the country you want UK/US/SE
country_code = "DK"

# Make the service call
result = client.service.CountryIntPhoneCode(
	sCountryISOCode=country_code,
	_soapheaders=[header_value]
)
# Print the result
print(f"Phone Code for {country_code} is {result}")
```
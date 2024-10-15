# studiensuche.DefaultApi

All URIs are relative to *https://rest.arbeitsagentur.de/infosysbub/studisu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studiensuche**](DefaultApi.md#studiensuche) | **GET** /pc/v1/studienangebote | Studiensuche


# **studiensuche**
> Response studiensuche()

Studiensuche

Die Studiensuche ermöglicht, verfügbare Studienangebote mit verschiedenen GET-Parametern zu filtern. In der Regel ist dabei die Angabe mindestens eines Suchwortes (sw), Studienfeldes (sfe) oder eines Studienfachs (sfa) erforderlich. Eine Ausnahme von dieser Regel besteht beispielsweise darin, den Filter zum Studienmodell (smo) auf 5 (für Duales Studium) zu setzen.

### Example

* Api Key Authentication (APIKeyHeaders):

```python
import time
from deutschland import studiensuche
from deutschland.studiensuche.api import default_api
from deutschland.studiensuche.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/infosysbub/studisu
# See configuration.py for a list of all supported configuration parameters.
configuration = studiensuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/studisu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeaders
configuration.api_key['APIKeyHeaders'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeaders'] = 'Bearer'

# Enter a context with an instance of the API client
with studiensuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    sw = "Informatikberufe" # str | Suchwort (optional)
    sfa = 93683 # int | Studienfach-ID (optional)
    sfe = "94175;94350" # str | dkzIds einer Studienfeld(gruppe), idR. zwei Semikolon-getrennte Werte je Studienfeld(gruppe). (optional)
    orte = "Feucht_90537_11.224918_49.376701" # str | Ortsangabe nebst Postleitzahl und Koordinaten (longitude und latitude) jeweils durch Unterstriche getrennt. (optional)
    pg = 1 # int | Ergebnissseite (optional)
    uk = "Bundesweit" # str | Umkreis - Bundesweit=Bundesweit, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km. (optional)
    re = "BW" # str | Region/Bundesland - BW=Baden-Württemberg, BY=Bayern, BE=Berlin, BB=Brandenburg, HB=Bremen, HH=Hamburg, HE=Hessen, MV=Mecklenburg-Vorpommern, NI=Niedersachsen, NW=Nordrhei-Westfalen, RP=Rheinland-Pfalz, SL=Saarland, SN=Sachsen, ST=Sachsen-Anhalt, SH=Schleswig-Holstein, TH=Thüringen, iA=Österreich. Mehrere Semikolon-getrennte Angaben möglich. (optional)
    sfo = 1 # int | Studienform - 0=Auf Anfrage, 1=Vollzeitstudium, 2=Teilzeitstudium, 3=Wochenendveranstaltung, 4=Fernstudium, 5=Selbststudium, 6=Blockstudium. Mehrere Semikolon-getrennte Angaben möglich. (optional)
    st = 1 # int | Studientyp - 0=Studiengang grundständig, 1=Studiengang weiterführend. (optional)
    smo = 5 # int | Studiengangmodell - 1=ausbildungsintegrierend, 2=berufsintegrierend, 3=berufsbegleitend, 4=praxisintegrierend, 5=Duales Studium allgemein. Mehrere Semikolon-getrennte Angaben möglich. (optional)
    abg = 0 # int | Studiengangsabschlussgrad - 0=ohne Angabe, 1=Abschlussprüfung, 2=Bachelor, 3=Diplom, 4=Diplom(FH), 10=Master, 12=Staatsexamen (optional)
    hsa = 108 # int | Hochschulart - 101=Berufsakademie/Duale Hochschule, 106=FH/FAW, 107=Kunst- und Musikhochschule, 108=Universität, 111=Verwaltungshochschule, 113=Private Hochschule. 114=Hochschule eigenen Typs. Mehrere Semikolon-getrennte Angaben möglich. (optional)
    san = 26218 # int | Studienanbieter-ID (optional)
    ffst = 1 # int | Eignungstest - 1=Studiencheck, 2=OSA. Mehrere Semikolon-getrennte Angaben möglich. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Studiensuche
        api_response = api_instance.studiensuche(sw=sw, sfa=sfa, sfe=sfe, orte=orte, pg=pg, uk=uk, re=re, sfo=sfo, st=st, smo=smo, abg=abg, hsa=hsa, san=san, ffst=ffst)
        pprint(api_response)
    except studiensuche.ApiException as e:
        print("Exception when calling DefaultApi->studiensuche: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sw** | **str**| Suchwort | [optional]
 **sfa** | **int**| Studienfach-ID | [optional]
 **sfe** | **str**| dkzIds einer Studienfeld(gruppe), idR. zwei Semikolon-getrennte Werte je Studienfeld(gruppe). | [optional]
 **orte** | **str**| Ortsangabe nebst Postleitzahl und Koordinaten (longitude und latitude) jeweils durch Unterstriche getrennt. | [optional]
 **pg** | **int**| Ergebnissseite | [optional]
 **uk** | **str**| Umkreis - Bundesweit&#x3D;Bundesweit, 25&#x3D;25 km, 50&#x3D;50 km, 100&#x3D;100 km, 150&#x3D;150 km, 200&#x3D;200 km. | [optional]
 **re** | **str**| Region/Bundesland - BW&#x3D;Baden-Württemberg, BY&#x3D;Bayern, BE&#x3D;Berlin, BB&#x3D;Brandenburg, HB&#x3D;Bremen, HH&#x3D;Hamburg, HE&#x3D;Hessen, MV&#x3D;Mecklenburg-Vorpommern, NI&#x3D;Niedersachsen, NW&#x3D;Nordrhei-Westfalen, RP&#x3D;Rheinland-Pfalz, SL&#x3D;Saarland, SN&#x3D;Sachsen, ST&#x3D;Sachsen-Anhalt, SH&#x3D;Schleswig-Holstein, TH&#x3D;Thüringen, iA&#x3D;Österreich. Mehrere Semikolon-getrennte Angaben möglich. | [optional]
 **sfo** | **int**| Studienform - 0&#x3D;Auf Anfrage, 1&#x3D;Vollzeitstudium, 2&#x3D;Teilzeitstudium, 3&#x3D;Wochenendveranstaltung, 4&#x3D;Fernstudium, 5&#x3D;Selbststudium, 6&#x3D;Blockstudium. Mehrere Semikolon-getrennte Angaben möglich. | [optional]
 **st** | **int**| Studientyp - 0&#x3D;Studiengang grundständig, 1&#x3D;Studiengang weiterführend. | [optional]
 **smo** | **int**| Studiengangmodell - 1&#x3D;ausbildungsintegrierend, 2&#x3D;berufsintegrierend, 3&#x3D;berufsbegleitend, 4&#x3D;praxisintegrierend, 5&#x3D;Duales Studium allgemein. Mehrere Semikolon-getrennte Angaben möglich. | [optional]
 **abg** | **int**| Studiengangsabschlussgrad - 0&#x3D;ohne Angabe, 1&#x3D;Abschlussprüfung, 2&#x3D;Bachelor, 3&#x3D;Diplom, 4&#x3D;Diplom(FH), 10&#x3D;Master, 12&#x3D;Staatsexamen | [optional]
 **hsa** | **int**| Hochschulart - 101&#x3D;Berufsakademie/Duale Hochschule, 106&#x3D;FH/FAW, 107&#x3D;Kunst- und Musikhochschule, 108&#x3D;Universität, 111&#x3D;Verwaltungshochschule, 113&#x3D;Private Hochschule. 114&#x3D;Hochschule eigenen Typs. Mehrere Semikolon-getrennte Angaben möglich. | [optional]
 **san** | **int**| Studienanbieter-ID | [optional]
 **ffst** | **int**| Eignungstest - 1&#x3D;Studiencheck, 2&#x3D;OSA. Mehrere Semikolon-getrennte Angaben möglich. | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[APIKeyHeaders](../README.md#APIKeyHeaders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


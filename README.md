# Hiring Task 3
## Country Details App
### Tech
- Python - Language
- FastAPI - Webframework

## How to run Locally

cd into root directory and install requirements. Create virutal env if necessary.
```sh
pip install -r requirements.txt
```
Starting the App
Runs the app with uvicorn server
```sh
python app/main.py
```
## How to run as Docker Container
Install Docker Engine by following the official installation [Guide](https://www.mongodb.com/docs/manual/installation/).
cd into the root directory
Using docker compose to pull and build image and building container
```sh
docker-compose up --build
```
or start in detached mode without interactive shell
```sh
docker-compose up -d
```

If everthing went correct we will see following message at the end
```sh
$ Application startup complete.
```
## How to use the APIs:
FastAPI provides web interface to use the APIs, also can be used with other API testing tools and curl or dedicated frontend

User http://0.0.0.0:3000/docs/ to open interactive docs provide by FastAPI to try all apis.

##### Get a country details
http://0.0.0.0:3000/{country_name}

eg. http://0.0.0.0:3000/France
###### Method: GET
Fetches Country details of the given country if the country is allowed.
Response Body
```sh
[
  {
    "top_level_domain": [
      ".fr"
    ],
    "alpha2_code": "FR",
    "alpha3_code": "FRA",
    "currencies": [
      {
        "code": "EUR",
        "name": "Euro",
        "symbol": "€"
      }
    ],
    "capital": "Paris",
    "calling_codes": [
      "33"
    ],
    "alt_spellings": [
      "FR",
      "French Republic",
      "République française"
    ],
    "relevance": null,
    "region": "Europe",
    "subregion": "Western Europe",
    "translations": {
      "br": "Frañs",
      "pt": "França",
      "nl": "Frankrijk",
      "hr": "Francuska",
      "fa": "فرانسه",
      "de": "Frankreich",
      "es": "Francia",
      "fr": "France",
      "ja": "フランス",
      "it": "Francia",
      "hu": "Franciaország"
    },
    "population": 67391582,
    "latlng": [
      46,
      2
    ],
    "demonym": "French",
    "area": 640679,
    "gini": 32.4,
    "timezones": [
      "UTC-10:00",
      "UTC-09:30",
      "UTC-09:00",
      "UTC-08:00",
      "UTC-04:00",
      "UTC-03:00",
      "UTC+01:00",
      "UTC+02:00",
      "UTC+03:00",
      "UTC+04:00",
      "UTC+05:00",
      "UTC+10:00",
      "UTC+11:00",
      "UTC+12:00"
    ],
    "borders": [
      "AND",
      "BEL",
      "DEU",
      "ITA",
      "LUX",
      "MCO",
      "ESP",
      "CHE"
    ],
    "native_name": "France",
    "name": "France",
    "numeric_code": "250",
    "languages": [
      {
        "iso639_1": "fr",
        "iso639_2": "fra",
        "name": "French",
        "nativeName": "français"
      }
    ],
    "flag": "https://flagcdn.com/fr.svg",
    "regional_blocs": [
      {
        "acronym": "EU",
        "name": "European Union"
      }
    ],
    "cioc": "FRA"
  }
]
```
Results error if the country is not allowed
http://0.0.0.0:3000/Canada
###### Method: GET
```sh
{
  "detail": "Country Canada is not in the list of allowed countries"
}
```

###### Additional Info:
Can be further improved by adding options to fetch only specified fields and more.

Handling allowed countries with alt_spellings is stored in list, this approach may need revision if the number of
allowed countries increases. May need to fetch the country detail and them check if the fetched country alt_spellins are
present in our allowed countries.





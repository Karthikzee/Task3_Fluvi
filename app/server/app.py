from fastapi import FastAPI, HTTPException, status
from fastapi.concurrency import run_in_threadpool
from restcountries import RestCountryApiV2 as rapi
from server.constants import ALLOWED_COUNTRIES
from server.exceptions import InvalidCountryException


app = FastAPI()


@app.get("/{country}", tags=["Root"])
async def get_country_details(country: str):
    """
    returns details of the given country if it is allowed
    :param country: str
    :return: json response object
    """
    try:
        if country.lower() not in ALLOWED_COUNTRIES:
            raise InvalidCountryException(country)
        country_list = await run_in_threadpool(rapi.get_countries_by_name, country)
        return country_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

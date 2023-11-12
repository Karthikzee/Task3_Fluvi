class InvalidCountryException(Exception):
    def __init__(self, country):
        message = f"Country {country} is not in the list of allowed countries"
        super().__init__(message)

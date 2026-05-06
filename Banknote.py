#this file is used for data validation

from pydantic import BaseModel

class Banknote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float    #if others are not float then the pydantic will change in to float and if the data is not convertible to float then it will raise an error and this is the advantage of using pydantic for data validation and parsing.
from typing import List
from spanish_dni.dni import DNI
from spanish_dni.exceptions import NotValidDNIException
from spanish_dni.validator import validate_dni


my_dnis: List[str] = [
    "23414538D",
    "Y2853959H",
    "23418D",
    "U2853959H",
    "23414538T",
    "72478072N"
]


for dni in my_dnis:
    valid = True
    try:
        dni_parsed: DNI = validate_dni(dni)
        print(f"DNI {dni} is type {dni_parsed.dni_type}")
    except NotValidDNIException:
        valid = False
        print(f"DNI {dni} is not valid")

from enum import Enum


class UserType(str, Enum):
    INDIVIDUAL = "individual"
    ENTITY = "entity"


class UserRoles(str, Enum):
    CONSTRUCTION_SITE = "construction_site"
    PROVIDER = "provider"
    CONTRACTOR = "contractor"


class ContractorField(str, Enum):
    SUPPLY = "supply"
    SALES_DEPARTMENT = "sales_department"


class CONSTRUCTIONSITETYPE(str, Enum):
    CONTRACTOR_ORGANIZATION = "contractor_organization"
    RENTAL_OF_SPECIAL_EQUIPMENT = "rental_of_special_equipment"

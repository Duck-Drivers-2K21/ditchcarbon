import requests

BASE_URL = "https://api.ditchcarbon.com/v1.0"


def args_gen(items: dict):
    """Convert dictionary to URL parameters"""
    result = [
        f"{key}={value}"
        for key, value in items.items()
        if value is not None
    ]
    return '&'.join(result)


def _call_ditch_carbon(endpoint, args: dict):
    args = args_gen(args)
    headers = {"accept": "application/json"}
    url = BASE_URL + f"/{endpoint}?{args}"
    response = requests.get(url, headers=headers)
    return response


def expense(supplier_, amount, description=None, amount_currency=None, date=None, region=None):
    return _call_ditch_carbon("calculate", locals())


def supplier(name, currency='USD', country=None, date=None, category=None):
    return _call_ditch_carbon("supplier", locals())


def product(name, manufacturer, category_name=None, unit=None, price_cents=None, price_currency=None, months=None,
            country=None):
    return _call_ditch_carbon("product", locals())


def find_server(manufacturer_name, model, ram_bytes, cpu_name=None, os_name=None, cpu_count=None, core_count=None,
                thread_count=None, is_virtual: bool = None, disk_count: int = None):
    return _call_ditch_carbon("servers", locals())


def get_server(id):
    return _call_ditch_carbon("servers/id", locals())


def server_emissions(id, hours, region: None, server_farm_size: None):
    locals_ = locals()
    locals_['id'] = None
    return _call_ditch_carbon(f"servers/{id}", locals_)


def emissions(q, unit=None, region=None, date=None, quantity=None):
    return _call_ditch_carbon(f"emissions", locals())


def categories(q, page):
    return _call_ditch_carbon(f"categories", locals())


def activity_categories(region=None):
    return _call_ditch_carbon(f"activities/top-level", locals())


def activities(region=None, name=None, page=None):
    return _call_ditch_carbon(f"activities", locals())


def activity(id):
    return _call_ditch_carbon(f"activities/{id}", {})


def activity_assessment(id, region=None, year=None, declared_unit=None):
    locals_ = locals()
    locals_['id'] = None
    return _call_ditch_carbon(f"activities/{id}", locals_)

import requests

BASE_URL = "https://api.ditchcarbon.com/v1.0"


class DitchCarbonClient:

    def __init__(self, api_key=None):
        assert api_key is not None
        self.api_key = api_key

    @staticmethod
    def args_gen(items: dict):
        """Convert dictionary to URL parameters"""
        result = [
            f"{key}={value}"
            for key, value in items.items()
            if value is not None
        ]
        return '&'.join(result)

    def _call_ditch_carbon(self, endpoint, args: dict):
        args = self.args_gen(args)
        headers = {
            "accept": "application/json",
            'authorization': "Bearer " + self.api_key
        }
        url = BASE_URL + f"/{endpoint}?{args}"
        response = requests.get(url, headers=headers)
        return response

    def get_expense(self, supplier, amount, description=None, amount_currency=None, date=None, region=None):
        print(locals())
        return self._call_ditch_carbon("calculate", locals())

    def get_supplier(self, name, currency='USD', country=None, date=None, category=None):
        return self._call_ditch_carbon("supplier", locals())

    def get_product(self, name, manufacturer, category_name=None, unit=None, price_cents=None, price_currency=None,
                    months=None,
                    country=None):
        return self._call_ditch_carbon("product", locals())

    def find_server(self, manufacturer_name, model, ram_bytes, cpu_name=None, os_name=None, cpu_count=None,
                    core_count=None,
                    thread_count=None, is_virtual: bool = None, disk_count: int = None):
        return self._call_ditch_carbon("servers", locals())

    def get_server(self, id):
        return self._call_ditch_carbon(f"servers/{id}", locals())

    def get_server_emissions(self, id, hours, region=None, server_farm_size=None):
        locals_ = locals()
        locals_['id'] = None
        return self._call_ditch_carbon(f"servers/{id}", locals_)

    def get_emissions(self, q, unit=None, region=None, date=None, quantity=None):
        return self._call_ditch_carbon(f"emissions", locals())

    def get_categories(self, q=None, page=None):
        return self._call_ditch_carbon(f"categories", locals())

    def get_activity_categories(self, region=None):
        return self._call_ditch_carbon(f"activities/top-level", locals())

    def get_activities(self, region=None, name=None, page=None):
        return self._call_ditch_carbon(f"activities", locals())

    def get_activity(self, id):
        return self._call_ditch_carbon(f"activities/{id}", {})

    def get_activity_assessment(self, id, region=None, year=None, declared_unit=None):
        locals_ = locals()
        locals_['id'] = None
        return self._call_ditch_carbon(f"activities/{id}", locals_)

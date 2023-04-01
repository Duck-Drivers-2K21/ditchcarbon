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


# carbon_client = DitchCarbonClient(api_key='680de78ec2812d2729138cb7e5b8319e')
# print("SUPPLIER" + str(carbon_client.get_supplier('Nestle', currency='GBP')))
#
# print("EXPENSE" + str(carbon_client.get_expense('Nestle', amount=120, amount_currency='USD')))
#
# print("PRODUCT" + str(carbon_client.get_product('Macbook', manufacturer='Apple')))
#
# print("FIND SERVER" + str(
#     carbon_client.find_server(manufacturer_name='Hewlett-Packard', model='ProLiant BL460c G8', ram_bytes=68719476736)))
#
# print("RET SERVER" + str(carbon_client.get_server(id='1')))
#
# print("GET SERVER EMISSIONS" + str(carbon_client.get_server_emissions(id='1', hours=2)))
#
# print("GET CATEGORIES" + str(carbon_client.get_categories()))
#
# print("GET ACTIVITY CATEGORIES" + str(carbon_client.get_activity_categories(region='GB')))
#
# print("GET ACTIVITIES" + str(carbon_client.get_activities(region='GB')))
#
# print("GET ACTIVITY" + str(carbon_client.get_activity(id='act_024b1cd615')))
#
# print("GET ACTIVITY ASS" + str(
#     carbon_client.get_activity_assessment(id='act_dac6b9fe9b', region='GB', declared_unit='tonnes')))

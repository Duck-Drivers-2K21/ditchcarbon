import requests

BASE_URL = "https://api.ditchcarbon.com/v1.0"


class DitchCarbonClient:
    """
    A client for the Ditch Carbon API.

    Args:
        api_key (str): The API key to use for authentication.

    Raises:
        AssertionError: If no API key is provided.
    """
    def __init__(self, api_key=None):
        assert api_key is not None
        self.api_key = api_key

    @staticmethod
    def args_gen(items: dict):
        """
        Convert a dictionary to URL parameters.

        Args:
            items (dict): A dictionary of parameters.

        Returns:
            str: The URL parameters.
        """
        result = [
            f"{key}={value}"
            for key, value in items.items()
            if value is not None
        ]
        return '&'.join(result)

    def _call_ditch_carbon(self, endpoint, args: dict):
        """
        Make a call to the Ditch Carbon API.

        Args:
            endpoint (str): The endpoint to call.
            args (dict): A dictionary of parameters.

        Returns:
            response: A requests.models.Response Object.
        """
        args = self.args_gen(args)
        headers = {
            "accept": "application/json",
            'authorization': "Bearer " + self.api_key
        }
        url = BASE_URL + f"/{endpoint}?{args}"
        response = requests.get(url, headers=headers)
        return response

    def get_expense(self, supplier, amount, description=None, amount_currency='GBP', date=None, region='US'):
        """
        Get the carbon emissions for an expense.

        Args:
            supplier (str): The name of the supplier of the expense.
            amount (int): Value of the expense.
            description (str, optional): A description of the expense. Defaults to None.
            amount_currency (str, optional): The currency of the expense amount. Defaults to GBP.
            date (str, optional): The date of the expense. Defaults to None.
            region (str, optional): The region of the expense. Defaults to US.

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon("calculate", locals())

    def get_supplier(self, name, currency='USD', country=None, date=None, category=None):
        """
        Look up the emissions factor of a supplier.

        Args:
            name (str): The name of the supplier.
            currency (str, optional): ISO three-letter currency code. Defaults to 'USD'.
            country (str, optional): Country of supplier's operations. ISO two-letter country code.
            date (date, optional): The date to use. Defaults to today's date.
            category (str, optional): The name of the supplier's industry

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon("supplier", locals())

    def get_product(self, name, manufacturer, category_name=None, unit=None, price_cents=None, price_currency=None,
                    months=None,
                    country=None):
        """
        Get information about a product (any goods or services).

        Args:
            name (str): The name of the product (fuzzy matched).
            manufacturer (str): The name of the organization that supplies the product (fuzzy-matched).
            category_name (str, optional): The category of the product. Defaults to None.
            unit (str, optional): The unit of the product. Leave blank for countable products.
            price_cents (int, optional): The price of the product in cents.
            price_currency (str, optional): Three letter currency code.
            months (int, optional): The number of months the product be used for.
            country (str, optional): The two-letter country code the product is used in.
            
        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon("product", locals())

    def find_server(self, manufacturer_name, model, ram_bytes, cpu_name=None, os_name=None, cpu_count=None,
                    core_count=None,
                    thread_count=None, is_virtual: bool = None, disk_count: int = None):
        """
        Finds a server with the given specifications.

        Args:
            manufacturer_name (str): The name of the server's manufacturer.
            model (str): The model name of the server.
            ram_bytes (int, optional): The amount of RAM used in bytes.
            cpu_name (str, optional): The name of the server's CPU.
            os_name (str, optional): The name of the server's operating system.
            cpu_count (int, optional): The number of physical CPUs.
            core_count (int, optional): The number of CPU cores per chip.
            thread_count (int, optional): The number of CPU threads across all chips.
            is_virtual (bool, optional): Whether the server is virtual or physical.
            disk_count (int, optional): The number of physical disks.

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon("servers", locals())

    def get_server(self, id):
        """
        Gets information about a server with the given ID.

        Args:
            id (str): The ID of the server.

        Returns:
            response: A requests.models.Response Object.

        """
        return self._call_ditch_carbon(f"servers/{id}", locals())

    def get_server_emissions(self, id, hours, region=None, server_farm_size=None):
        """
        Retrieves the emissions data for a specific server over a specified time period.

        Args:
            id (str): The ID of the server to retrieve emissions data for.
            hours (int): The number of hours the server has been in use.
            region (str, optional): ISO two-letter country code in which the server is running. When left blank, we'll use global averages.
            server_farm_size (str, optional): The size of the server farm.

        Returns:
            response: A requests.models.Response Object.

        """
        locals_ = locals()
        locals_['id'] = None
        return self._call_ditch_carbon(f"servers/{id}", locals_)

    def get_emissions(self, q, unit=None, region=None, date=None, quantity=None):
        """
        Retrieves emissions data for a specific query.

        Args:
           q (str): The query to retrieve emissions data for.
           unit (str, optional): The unit of measurement to return the emissions data in.
           region (str, optional): The [ISO 3166-2] country and optional subdivision code.
           date (date, optional): The date to retrieve emissions data for. Defaults to today's date
           quantity (int, optional): The amount of units to look up.

        Returns:
           response: A requests.models.Response Object.

        """
        return self._call_ditch_carbon(f"emissions", locals())

    def get_categories(self, q=None, page=None):
        """
        Retrieves a list of categories.

        Args:
            q (str, optional): The query to search categories for.
            page (int, optional): The page number of the categories to retrieve.

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon(f"categories", locals())

    def get_activity_categories(self, region=None):
        """
        Get the top-level activity categories available on the Ditch Carbon platform.

        Args:
           region (str, optional): ISO two-letter country code of activity region

        Returns:
           response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon(f"activities/top-level", locals())

    def get_activities(self, region=None, name=None, page=None):
        """
        Get a list of activities available on the Ditch Carbon platform.

        Args:
            region (str, optional): ISO two-letter country code or Global
            name (str, optional): Filter by top-level activity name.
            page (int, optional): The page number to retrieve.

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon(f"activities", locals())

    def get_activity(self, id):
        """
        Get detailed information about a specific activity on the Ditch Carbon platform.

        Args:
            id (str): The ID of the activity to retrieve.

        Returns:
            response: A requests.models.Response Object.
        """
        return self._call_ditch_carbon(f"activities/{id}", {})

    def get_activity_assessment(self, id, region=None, year=None, declared_unit=None):
        """
        Get the carbon assessment for a specific activity.

        Args:
        id (str): The ID of the activity to retrieve.
        region (str, optional): ISO two-letter country code.
        year (int, optional): Source year to use. e.g. 2022 will use 2022's data.
        declared_unit (str, optional): GHG emission factors will be in reference to this unit.

        Returns:
            response: A requests.models.Response Object.
        """
        locals_ = locals()
        locals_['id'] = None
        return self._call_ditch_carbon(f"activities/{id}", locals_)


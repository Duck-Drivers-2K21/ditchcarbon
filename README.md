# DitchPy

Introducing "DitchPy", an open-source Python package that allows users to easily call the DitchCarbon API (v1.0) using HTTP requests.

DitchCarbon is an API that provides information on carbon emissions of different energy sources across the globe. With DitchPy, users can easily retrieve information about the carbon emissions of different energy sources and use it in their own projects.

DitchPy is built on top of the popular Python requests library and provides a simple interface for making HTTP requests to the DitchCarbon API. The package includes a set of functions that allow users to retrieve data for specific countries, energy sources, and time periods.

To get started, users can simply install DitchPy using pip:

```
pip install DitchPy
```

## Usage

Create an instance of the DitchCarbonClient:

```
carbon_client = DitchCarbonClient(api_key=API_KEY)
```

Then call one of the DitchCarbonAPIs endpoints:

```
carbon_client.get_supplier('Nestle', currency='GBP'))
```



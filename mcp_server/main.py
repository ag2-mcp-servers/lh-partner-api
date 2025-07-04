# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T04:39:25+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Header, Path, Query

app = MCPProxy(
    description='',
    license={'name': 'LH', 'url': 'https://developer.lufthansa.com'},
    title='LH Partner API',
    version='1.0',
    servers=[{'url': 'https://api.lufthansa.com/v1'}],
)


@app.get(
    '/baggage/baggagetripandcontact/{searchID}',
    description=""" Retrieve passenger trip, contact and baggage details. This service is only accessible for LH privileged partners """,
    tags=['baggage_operations_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def baggage__trip_and__contact(
    search_i_d: str = Path(..., alias='searchID'),
    accept: str = Header(..., alias='Accept'),
):
    """
    Baggage Trip and Contact
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/allfares',
    description=""" Retrieves all available fares for a specific Origin & Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def all__fares(
    catalogues: str,
    origin: str = ...,
    destination: str = ...,
    travel_date: str = Query(..., alias='travel-date'),
    return_date: Optional[str] = Query(None, alias='return-date'),
    cabin_class: Optional[str] = Query('economy', alias='cabin-class'),
    travelers: Optional[str] = None,
    fare_family: Optional[str] = Query('smart', alias='fare-family'),
    trackingid: Optional[str] = None,
    accept: Optional[str] = Header('application/json', alias='Accept'),
):
    """
    All Fares
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/bestfares',
    description=""" Retrieve best fares for the requested journey across multiple days or multiple months. """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def best__fares(
    catalogues: str,
    origin: str = ...,
    destination: str = ...,
    travel_date: str = Query(..., alias='travel-date'),
    trip_duration: str = Query(..., alias='trip-duration'),
    range: str = ...,
    accept: str = Header(..., alias='Accept'),
    cabin_class: Optional[str] = Query(None, alias='cabin-class'),
    country: Optional[str] = None,
    trackingid: Optional[str] = None,
    fare_family: Optional[str] = Query(None, alias='fare-family'),
):
    """
    Best Fares
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/deeplink',
    description=""" Returns valid deep links for the provided input parameters """,
    tags=['deep_link_management', 'fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def deep__links(
    catalogues: str,
    trackingid: str = ...,
    country: str = ...,
    lang: str = ...,
    accept: str = Header(..., alias='Accept'),
    origin: Optional[str] = None,
    origin_name: Optional[str] = Query(None, alias='origin-name'),
    destination: Optional[str] = None,
    destination_name: Optional[str] = Query(None, alias='destination-name'),
    travel_date: Optional[str] = Query(None, alias='travel-date'),
    return_date: Optional[str] = Query(None, alias='return-date'),
    cabin_class: Optional[str] = Query(None, alias='cabin-class'),
    outbound_segments: Optional[str] = Query(None, alias='outbound-segments'),
    return_segments: Optional[str] = Query(None, alias='return-segments'),
    travelers: Optional[str] = None,
    fare: Optional[str] = None,
    net_fare: Optional[str] = Query(None, alias='net-fare'),
    fare_currency: Optional[str] = Query(None, alias='fare-currency'),
    partnerid: Optional[str] = None,
    encryption_key: Optional[str] = Query(None, alias='encryption-key'),
):
    """
    Deep Links
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/deeplink/ffp',
    description=""" Returns valid LH deep links (FFP - links to flight selection screen on LH.COM) """,
    tags=['deep_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def l_h__deep__links____f_f_p(
    catalogues: str,
    origin: str = ...,
    destination: str = ...,
    travel_date: str = Query(..., alias='travel-date'),
    trackingid: str = ...,
    country: str = ...,
    lang: str = ...,
    accept: str = Header(..., alias='Accept'),
    return_date: Optional[str] = Query(None, alias='return-date'),
    cabin_class: Optional[str] = Query(None, alias='cabin-class'),
    travelers: Optional[str] = None,
    partnerid: Optional[str] = None,
    encryption_key: Optional[str] = Query(None, alias='encryption-key'),
):
    """
    LH Deep Links - FFP
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/deeplink/itco',
    description=""" Returns valid LH deep links (ITCO - links to shopping cart on LH.COM) """,
    tags=['fare_information_management', 'deep_link_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def l_h__deep__links____i_t_c_o(
    catalogues: str,
    origin: str = ...,
    destination: str = ...,
    travel_date: str = Query(..., alias='travel-date'),
    outbound_segments: str = Query(..., alias='outbound-segments'),
    fare: str = ...,
    fare_currency: str = Query(..., alias='fare-currency'),
    trackingid: str = ...,
    country: str = ...,
    lang: str = ...,
    accept: str = Header(..., alias='Accept'),
    return_date: Optional[str] = Query(None, alias='return-date'),
    cabin_class: Optional[str] = Query(None, alias='cabin-class'),
    return_segments: Optional[str] = Query(None, alias='return-segments'),
    travelers: Optional[str] = None,
    net_fare: Optional[str] = Query(None, alias='net-fare'),
    partnerid: Optional[str] = None,
    encryption_key: Optional[str] = Query(None, alias='encryption-key'),
):
    """
    LH Deep Links - ITCO
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/fares',
    description=""" Retrieve all available fares per fare family for a specific Origin & Destination on a given date """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def fares(
    catalogues: str,
    segments: str = ...,
    carriers: str = ...,
    accept: str = Header(..., alias='Accept'),
    travelers: Optional[str] = None,
    fare_types: Optional[str] = Query('basic', alias='fare-types'),
):
    """
    Fares
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/lowestfares',
    description=""" Retrieve lowest fare for a specific Origin & Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS & LH """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def lowest__fares(
    catalogues: str,
    origin: str = ...,
    destination: str = ...,
    travel_date: str = Query(..., alias='travel-date'),
    accept: str = Header(..., alias='Accept'),
    return_date: Optional[str] = Query(None, alias='return-date'),
    cabin_class: Optional[str] = Query(None, alias='cabin-class'),
    travelers: Optional[str] = None,
    fare_family: Optional[str] = Query('basic', alias='fare-family'),
    country: Optional[str] = None,
):
    """
    Lowest Fares
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/fares/subscriptions',
    description=""" Create a subscription for best price O&D. Receive regular updates on lowest fares """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def fares__subscriptions(
    origin: str,
    destination: str = ...,
    cabin_class: str = Query(..., alias='cabin-class'),
    trip_duration: str = Query(..., alias='trip-duration'),
    email: str = ...,
    lang: str = ...,
    accept: str = Header(..., alias='Accept'),
    country: Optional[str] = None,
    trackingid: Optional[str] = None,
):
    """
    Fares Subscriptions
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/ond/route/{origin}/{destination}',
    description=""" Returns LH route origin & destination information """,
    tags=['route_status_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def o_n_d__route(
    origin: str,
    destination: str = ...,
    accept: str = Header(..., alias='Accept'),
    catalogues: Optional[str] = 'LH',
    limit: Optional[str] = None,
    offset: Optional[str] = None,
):
    """
    OND Route
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/ond/status',
    description=""" Returns LH network route status information. Search for recently added or retired routes """,
    tags=['route_status_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def o_n_d__status(
    accept: str = Header(..., alias='Accept'),
    catalogues: Optional[str] = 'LH',
    new_routes: Optional[str] = Query(None, alias='new-routes'),
    old_routes: Optional[str] = Query(None, alias='old-routes'),
):
    """
    OND Status
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/offers/ond/top',
    description=""" Returns LH Top routes per country or across all countries """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def top__o_n_d(
    accept: str = Header(..., alias='Accept'),
    catalogues: Optional[str] = 'LH',
    origin: Optional[str] = None,
):
    """
    Top OND
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/orders/orders/{orderID}/{name}',
    description=""" Retrieve order by ID and optionally name. This service is only accessible for LH privileged partners """,
    tags=['user_session_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def orders(
    order_i_d: str = Path(..., alias='orderID'),
    accept: str = Header(..., alias='Accept'),
    name: str = ...,
):
    """
    Orders
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/preflight/autocheckin/{ticketnumber}',
    description=""" Trigger an automatic check-in given a ticket number. This service is only accessible for LH privileged partners """,
    tags=['user_session_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def auto__check__in(
    ticketnumber: str,
    email_address: str = Query(..., alias='emailAddress'),
    accept: str = Header(..., alias='Accept'),
):
    """
    Auto Check-In
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/promotions/priceoffers/flights/ond/{origin}/{destination}',
    description=""" Retrieve a best price offer given an origin and destination. """,
    tags=['fare_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def price__offers(
    origin: str,
    destination: str = ...,
    departure_date: str = Query(..., alias='departureDate'),
    return_date: str = Query(..., alias='returnDate'),
    service: Optional[str] = 'amadeusBestPrice',
):
    """
    Price Offers
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/references/seatdetails/{aircraftCode}/{cabinCode}',
    description=""" A description of all available seat details by aircraft type. You can retrieve the full set or details for a particular aircraft type. """,
    tags=['seating_information_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def seat__details(
    aircraft_code: str = Path(..., alias='aircraftCode'),
    accept: str = Header(..., alias='Accept'),
    cabin_code: str = Path(..., alias='cabinCode'),
    lang: Optional[str] = None,
):
    """
    Seat Details
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup

import copy


def check_address(rest_location):
    auth_id = "90919a9b-d1fc-ed72-059a-c40f0c48eb26"
    auth_token = "bpz3YBWzuVHByBsQQHSr"
    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_street_api_client()

    lookup = StreetLookup()
    lookup.street = rest_location
    lookup.candidates = 1
    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return None

    result = lookup.result

    if not result:
        print("No candidates. This means the address is not valid.")
        return None

    first_candidate = result[0]

    print("There is at least one candidate.")
    print("If the match parameter is set to STRICT, the address is valid.")
    print("Otherwise, check the Analysis output fields to see if the address is valid.\n")
    print("ZIP Code: " + first_candidate.components.zipcode)
    print("County: " + first_candidate.metadata.county_name)
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))
    # print("Precision: {}".format(first_candidate.metadata.precision))
    # print("Residential: {}".format(first_candidate.metadata.rdi))
    # print("Vacant: {}".format(first_candidate.analysis.dpv_vacant))

    return copy.copy(first_candidate.delivery_line_1)
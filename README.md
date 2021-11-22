Current as of 2021 November elections. No map (only a list of addresses) existed for Bernalillo county so I took the data from that list and mapped it

# [Polling Locations in Bernalillo County 2021](http://albuquerque-polling-locations.s3-website-us-west-1.amazonaws.com/)

## Development notes
* List of addresses is contained in `locations.txt`
* Additional pre-geocoded addresses that could not be geocoded by OSM are stored in `raw_gps_additions.jsonl`
* Uncomment `geocode_all` to re-run geocoding for `locations.txt` but remember that it appends to the `geocode_results.jsonl` file so you must clear the contents before doing so

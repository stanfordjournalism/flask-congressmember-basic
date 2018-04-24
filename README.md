# Base Congressmembers Flask App


Data comes from the [unitedstates/congress-legislators repo](https://github.com/unitedstates/congress-legislators):

The file in [static/legislators.csv](static/legislators.csv) comes from here:

https://theunitedstates.io/congress-legislators/legislators-current.csv

The [unitedstates/images repo](https://github.com/unitedstates/images) hosts public domain photos of legislators so that we don't have to have store them ourselves. We just have to follow this convention:


https://theunitedstates.io/images/congress/225x275
/[bioguide_id].jpg

Where `[bioguide_id]` is the bioguide identifier for a given congressmember. For example, Senator Dianne Feinstein has a Bioguide ID of [F000062](http://bioguide.congress.gov/scripts/biodisplay.pl?index=f000062)

Which means her photo can be found at:

https://theunitedstates.io/images/congress/225x275
/F000062.jpg

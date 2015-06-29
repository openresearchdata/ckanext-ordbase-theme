# ckanext-ordbase-theme

CKAN theme for the following four Open Research Data instances:

* Open Research Data Platform Switzerland (http://openresearchdata.ch/)
* Open Social Sciences Data (http://opendata.forscenter.ch/)
* Open Life Sciences Data (http://lifesciencedata.ch/)
* Open Humanities Data (http://data.humanities.ch/)

## settings.ini config options

```
ckan.site_title = Instance title
ckan.site_logo = /path/to/logo
ckan.favicon = "/path/to/favicons"

ckan.ordbasetheme.enable_language_nav = [true|false]
ckan.ordbasetheme.theme = [ordplatform|socialsci|lifesci|humanities]
ckan.ordbasetheme.analytics.trackingid = UA-123456789-0

licenses_group_url = file:///path/to/ckan/ckanext-ordbase-theme/public/licenses.json
```
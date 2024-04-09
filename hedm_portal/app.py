
from django.apps import AppConfig
from hedm_portal import checks

class Hedmportal(AppConfig):
    name = 'HEDM Portal'



SEARCH_INDEXES = {
    "hedm_portal": {
        "uuid": "2908df1b-fee4-4f55-b2e6-cf627dac88ee",
        "name": "HEDM Portal",
        "template_override_dir": "hedm_portal",
        "fields": [],
    }
}
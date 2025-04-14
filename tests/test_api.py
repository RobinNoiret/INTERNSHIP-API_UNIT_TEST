import pytest
import vcr
import os
from dotenv import load_dotenv
from app.main import get_communes_by_postal_code, get_age_by_full_name, get_echo_from_hackuity_api

load_dotenv()
HACKUITY_API_KEY = os.getenv("HACKUITY_API_KEY")

my_vcr = vcr.VCR(
    cassette_library_dir="tests/cassettes",
    record_mode="new_episodes",
    filter_headers=[("Authorization", "Bearer [REDACTED]")],
)

class TestGetCommunesByPostalCode:
    @my_vcr.use_cassette("get_communes_by_postal_code.yaml")
    def test_get_communes_by_postal_code(self):
        result = get_communes_by_postal_code("69270")
        assert result == [
            {"codePostal": "69270", "codeCommune": "69033", "nomCommune": "Cailloux-sur-Fontaines", "libelleAcheminement": "CAILLOUX-SUR-FONTAINES"},
            {"codePostal": "69270", "codeCommune": "69068", "nomCommune": "Couzon-au-Mont-d'Or", "libelleAcheminement": "COUZON-AU-MONT-D OR"},
            {"codePostal": "69270", "codeCommune": "69087", "nomCommune": "Fontaines-Saint-Martin", "libelleAcheminement": "FONTAINES-SAINT-MARTIN"},
            {"codePostal": "69270", "codeCommune": "69088", "nomCommune": "Fontaines-sur-Saône", "libelleAcheminement": "FONTAINES SUR SAONE"},
            {"codePostal": "69270", "codeCommune": "69168", "nomCommune": "Rochetaillée-sur-Saône", "libelleAcheminement": "ROCHETAILLEE-SUR-SAONE"},
            {"codePostal": "69270", "codeCommune": "69233", "nomCommune": "Saint-Romain-au-Mont-d'Or", "libelleAcheminement": "SAINT-ROMAIN-AU-MONT-D OR"}
        ]

    @my_vcr.use_cassette("get_communes_by_postal_code_error.yaml")
    def test_get_communes_by_postal_code_error(self):
        with pytest.raises(Exception):
            get_communes_by_postal_code("99999")


class TestGetAgeByFullName:
    @my_vcr.use_cassette("get_age_by_full_name.yaml")
    def test_get_age_by_full_name(self):
        result = get_age_by_full_name("John")
        assert result == {"name": "John", "age": 74, "count": 277407}

    @my_vcr.use_cassette("get_age_by_full_name_error.yaml")
    def test_get_age_by_full_name_error(self):
        result = get_age_by_full_name("UnknownName")
        assert result == {"name": "UnknownName", "age": None, "count": 0}

class TestHackuity:
    def test_hackuity_api_key_is_loaded(self):
        assert HACKUITY_API_KEY is not None, "La clé API HACKUITY_API_KEY n'est pas chargée."
        assert HACKUITY_API_KEY != "", "La clé API HACKUITY_API_KEY est vide."

    @my_vcr.use_cassette("get_echo_from_hackuity.yaml")
    def test_get_echo_from_hackuity(self):
        result = get_echo_from_hackuity_api(HACKUITY_API_KEY)
        assert result == {
            'groupIds': ['group-admin-N112233445501'],
            'kind': 'hy#authenticatedUser',
            'namespace': 'N112233445501',
            'roles': ['USER'],
            'rootGroupId': 'group-admin-N112233445501',
            'userId': 'admin-N112233445501',
            'userKeyId': 'cuq62fzotpd9s3ZgWEE9Sq',
            'userNamespace': 'N112233445501'
        }

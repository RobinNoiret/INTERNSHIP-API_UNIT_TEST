import pytest
import vcr
from app.main import get_communes_by_postal_code, get_age_by_full_name

my_vcr = vcr.VCR(
    cassette_library_dir="tests/cassettes",
    record_mode="new_episodes",
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

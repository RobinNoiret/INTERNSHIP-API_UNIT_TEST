import pytest
import requests_mock
from app.main import get_communes_by_postal_code

class TestGetCommunesByPostalCode:
    def test_get_communes_by_postal_code(self):
        with requests_mock.Mocker() as m:
            m.get(
                "https://apicarto.ign.fr/api/codes-postaux/communes/69270",
                json={
                    "communes": [
                        {
                            "code_postal": "69270",
                            "nom_commune": "Saint-Priest",
                            "code_insee": "69280"
                        }
                    ]
                }
            )
            result = get_communes_by_postal_code("69270")
            assert result == {
                "communes": [
                    {
                        "code_postal": "69270",
                        "nom_commune": "Saint-Priest",
                        "code_insee": "69280"
                    }
                ]
            }

import pytest
import requests_mock
import requests
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

    def test_get_communes_by_postal_code_error(self):
        with requests_mock.Mocker() as m:
            # Simuler une réponse avec un code HTTP 404
            m.get(
                "https://apicarto.ign.fr/api/codes-postaux/communes/99999",
                status_code=404,
                json={"error": "Code postal non trouvé"}
            )

            # Vérifier que la fonction lève une exception
            with pytest.raises(requests.exceptions.HTTPError):
                get_communes_by_postal_code("99999")

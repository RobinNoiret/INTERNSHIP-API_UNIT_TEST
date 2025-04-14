import requests
import os
from dotenv import load_dotenv

load_dotenv()
HACKUITY_API_KEY = os.getenv("HACKUITY_API_KEY", "FAKE_API_KEY_FOR_TESTS")

def get_communes_by_postal_code(code_postal):
    url = f"https://apicarto.ign.fr/api/codes-postaux/communes/{code_postal}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        raise

def get_age_by_full_name(nom_complet):
    url = f"https://api.agify.io?name={nom_complet}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        raise

def get_echo_from_hackuity_api(api_key):
    url = f"https://random-for-n112233445501-corp.standalone.rd.bigupfor.me/api/v1/echo/user"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        raise

def get_version(api_key):
    url = f"https://random-for-n112233445501-corp.standalone.rd.bigupfor.me/api/v1/version/full"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        raise


if __name__ == "__main__":
    code_postal = "69270"
    try:
        communes = get_communes_by_postal_code(code_postal)
        print(f"Communes pour le code postal {code_postal} : {communes}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    nom_complet = "John Doe"
    try:
        age_data = get_age_by_full_name(nom_complet)
        print(f"Âge estimé pour {nom_complet} : {age_data}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    try:
        echo_data = get_echo_from_hackuity_api(HACKUITY_API_KEY)
        print(f"Données d'écho : {echo_data}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    try:
        assessment_data = get_version(HACKUITY_API_KEY)
        print(f"Données d'évaluation : {assessment_data}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

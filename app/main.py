import requests

def get_communes_by_postal_code(code_postal):
    """
    Effectue un appel API pour récupérer les communes associées à un code postal.

    :param code_postal: Le code postal à rechercher.
    :return: Les données JSON renvoyées par l'API ou une exception en cas d'erreur.
    """
    url = f"https://apicarto.ign.fr/api/codes-postaux/communes/{code_postal}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")
        raise


if __name__ == "__main__":
    code_postal = "69270"  # Exemple de code postal
    try:
        communes = get_communes_by_postal_code(code_postal)
        print(f"Communes pour le code postal {code_postal} : {communes}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

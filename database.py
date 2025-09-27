import requests
import os
import dotenv

dotenv.load_dotenv()


def create_summary(data: dict):
    # This function is correct. No changes needed.
    print("sending data to server")
    url = os.getenv("CREATE_SUMMARY_URL")
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code, response.json())
    return response


def get_summaries(user_id, server_id):
    # This function works, but I'm updating it to match Go handler for clarity.
    print("getting summaries")
    url = os.getenv("GET_SUMMARY_URL")
    headers = {"ID": str(user_id)}  # Go handler uses this for auth
    params = {"user_id": str(user_id), "server_id": str(server_id)}  # Go handler ignores these but it's good practice
    response = requests.get(url, params=params, headers=headers)
    print(response.status_code, response.json())
    return response


def update_summary(user_id, summary_id, content):
    """
    Updates a specific summary's content.
    """
    print("updating summary")
    url = os.getenv("UPDATE_SUMMARY_URL")
    # The Go handler needs the user's ID in the header for auth
    headers = {"Content-Type": "application/json", "ID": str(user_id)}

    # --- CHANGED: The payload MUST include summary_id and use snake_case keys ---
    payload = {
        "summary_id": str(summary_id),
        "content": str(content)
    }

    response = requests.put(url, headers=headers, json=payload)
    print(response.status_code, response.json())
    return response


def del_summary(user_id: str, summary_id: str):
    print("deleting summary")
    url = os.getenv("DELETE_SUMMARY_URL")
    # The Go handler gets the user ID from the 'ID' header
    headers = {"ID": str(user_id)}

    # --- CHANGED: The JSON key is now 'summary_id' (snake_case) ---
    payload = {"summary_id": str(summary_id)}

    response = requests.delete(url, json=payload, headers=headers)
    print(response.status_code, response.json())
    return response


def del_summary(user_id: str, summary_id: str):
    """
    Deletes a summary by its ID for a given user.
    """
    print(f"user_id: {user_id}, summary_id: {summary_id}")
    print(f"Attempting to delete summary {summary_id} for user {user_id}")
    url = os.getenv("DELETE_SUMMARY_URL")

    # The Go handler gets the user ID from the 'ID' header for authentication
    headers = {"ID": str(user_id)}

    # The JSON key MUST be 'summary_id' (snake_case) to match the Go struct tag
    payload = {"summary_id": str(summary_id)}
    print(f"headers: {headers}, \npayload: {payload}")

    response = requests.delete(url, json=payload, headers=headers)

    print(f"Response for deleting {summary_id}: {response.status_code}", response.json())
    return response
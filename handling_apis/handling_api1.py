import requests


def get_random_user_profile():
    response = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random")
    
    if response.status_code == 200:
        user_data = response.json()["data"]
        firstname = user_data["name"]["first"]
        lastname = user_data["name"]["last"]
        email = user_data["email"]
        return firstname, lastname,email


def main():
    try:
        firstname, lastname , email = get_random_user_profile()
        print(f"Random user profile\n")
        print(f"First name: {firstname}")
        print(f"Last name: {lastname}")
        print(f"Email: {email}")
    except Exception as e:
        print(f"Error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    main()
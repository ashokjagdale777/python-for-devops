import requests
import json


def get_github_repositories():
    """
    This function calls GitHub public API
    and returns repository data in JSON format
    """
    url = "https://api.github.com/repositories"

    response = requests.get(url)

    # Check if API call is successful
    if response.status_code == 200:
        return response.json()
    else:
        print("GitHub API call failed")
        return []


def extract_required_data(repositories):
    """
    GitHub API gives a lot of data.
    We only extract what is useful for us.
    """
    final_data = []

    # Taking only first 10 repos to keep output clean
    for repo in repositories[:10]:
        repo_info = {
            "repository_name": repo["name"],
            "full_name": repo["full_name"],
            "owner_name": repo["owner"]["login"],
            "repo_url": repo["html_url"]
        } 

        final_data.append(repo_info)

    return final_data


def save_output_to_file(data):
    """
    Save processed data into a JSON file
    """
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)


def main():
    # Step 1: Fetch data from GitHub API
    repositories = get_github_repositories()

    if not repositories:
        return

    # Step 2: Process and filter required fields
    cleaned_data = extract_required_data(repositories)

    # Step 3: Print output to terminal
    print("\nPublic GitHub Repositories:\n")
    for repo in cleaned_data:
        print(
            f"Repo: {repo['full_name']} | "
            f"Owner: {repo['owner_name']}"
        )

    # Step 4: Save data to JSON file
    save_output_to_file(cleaned_data)
    print("\nData successfully saved to output.json")


if __name__ == "__main__":
    main()

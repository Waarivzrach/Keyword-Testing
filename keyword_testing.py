import requests
import time

# For reading queries from a text file
def read_queries_from_file(file_path):
    with open(file_path, 'r') as file:
        queries = [line.strip() for line in file.readlines() if line.strip()]
    return queries

# For reading queries from a GitHub raw URL
def read_queries_from_github(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        queries = [line.strip() for line in response.text.splitlines() if line.strip()]
        return queries
    else:
        print(f"Failed to fetch the file from GitHub. Status code: {response.status_code}")
        return []

# Sends the requests and processes the responses
def send_request(query):
    query_params = {'search': query}
    
    # REPLACE THIS with the actual sink server URL when we have it
    sink_server_url = 'http://google.com'
    
    # Sends the GET request to the sink server and measures the time it takes
    start_time = time.time()  # Starts timing the request
    response = requests.get(sink_server_url, params=query_params)
    end_time = time.time()  # Finishes timing the request

    # Handles the response from the server
    response_time = end_time - start_time  # Calculates how long the request took
    print(f"Request for query '{query}' took {response_time:.2f} seconds")

    if response.status_code == 200:
        try:
            # This prints out whatever JSON results we get
            response_json = response.json()
            print(f"Status: {response_json.get('status', 'Unknown')}")
            print(f"Message: {response_json.get('message', 'No message provided')}")

            # Print the search results
            if 'data' in response_json:
                print("Search Results:")
                for result in response_json['data'].get('results', []):
                    print(f"- {result['title']}: {result['url']}")
        except ValueError:
            print("Response is not in JSON format.")
    else:
        print(f"Request failed for query '{query}' with status code {response.status_code}")

def main():
    # Only have one of these uncommented to choose the input method.

    # READ FROM TEXT FILE OPTION
    #file_path = r'TEXT_FILE_LOCATION.txt'  # Provide the path to your local text file
    #queries = read_queries_from_file(file_path)

    # READ FROM GITHUB OPTION
    github_url = 'URL_OF_WHERE_THE_FILE_IS.txt'
    queries = read_queries_from_github(github_url)
    
    for query in queries:
        send_request(query)

# Run that thang
if __name__ == "__main__":
    main()

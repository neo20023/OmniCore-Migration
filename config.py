import os

# Environment Variables
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

# Secure API Key Management
if API_KEY is None:
    raise ValueError("No API key provided. Please set the API_KEY environment variable.")

# Example usage of the environment variables
if __name__ == '__main__':
    print(f"Database URL: {DATABASE_URL}")
    print(f"API Key: {API_KEY}")

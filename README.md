# Open Source Intelligence Application

This is a web application built with Flask that allows users to retrieve, view and visualize details from Instagram and Twitter profiles.

## Features

- **Instagram Details:** Users can input an Instagram username to retrieve details such as username, full name, biography, follower count, following count, total posts, etc. The application also fetches and displays details of the user's recent posts including captions, likes, comments, and post URLs.
  
- **Twitter Details:** Similar to Instagram, users can input a Twitter username to fetch details such as screen name, real name, follower count, following count, and total tweets.

## Requirements

- Python >=3.10.10

## Setup
1. **Create a Virtual Environment:**

        # Create a virtual environment (optional but recommended)
        python -m venv osint

        # Activate the virtual environment (Windows)
        venv\Scripts\activate

        # Activate the virtual environment (macOS/Linux)
        source venv/bin/activate

2. **Clone the Repository:**

        git clone https://github.com/your-username/social-media-details.git


3. **Install Dependencies:**

        pip install -r requirements.txt
        L.interactive_login("your_instagram_username_here")

3. **Configuration**
Before running the application, make sure to update the Instagram username in the `insta.py` file. Locate the following line in `insta.py`:

        L.interactive_login("your_instagram_username_here")

Replace it with your Instagram username

5. **Run the Application:**

        flask run 

5. **Access the Application:**
Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. **Instagram:**
- Enter an Instagram username in the provided input field and click the "Submit" button.
- View the retrieved user details and recent post details.

2. **Twitter:**
- Enter a Twitter username in the provided input field and click the "Submit" button.
- View the retrieved user details.

## Limitations

- While the application does not impose limitations on Instagram search queries, fetching details for users with a large number of followers or posts may result in longer response times. This delay is primarily due to the time taken by Instagram's servers to process and retrieve data for such profiles.

## To-Do

- [ ] Implement Reddit and LinkedIn APIs.
- [ ] Add support for fetching more detailed user information from Instagram and Twitter.
- [ ] Improve error handling and error messages.
- [ ] Enhance the UI/UX of the web application.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

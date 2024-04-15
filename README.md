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


## Screenshots

 **Homepage**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEjGfwAOJclPcYrmKuh35axkxa_gLXLJfQao6Gw51AtDqMEZ-ivv-jpeT5D5L2BmBBvKVgZlpkelTHXBJcpP1l1EGYG2r-KRZUreqVR5-_X-5gzcIcd2Id49UsEL8mlW0rMIOGSNTrTrIrIkfn9EB7E7eyHloWpCvGSRTzigdeTtUQ-UVoQXUCXSTK83W2Gx=s16000)

 **Data Retrieved from Instagram**

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEiXiSbPACvJmusxKuKixTCl2__Bcvg1Nb045nM_qHovC_mS5mhdbsVH9eQzb77rRAyRDtnzbQkXAGQ8CXfHIqagR1y7TybqRG7z-s9nYeN5R28QUw3w7DjXMQHMHpZIc90Pf3pAw1ESSsJtbZ6S7Sv_j1SwFkIL6obGPe-f9zKVdDoa1wPkUUWHtP6l7-y8=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgCAGFf4Wtc3KM1YIhMT9a6-mHGw25ZQIdWr3pzEGiFPwnv1o64OEJ7e3dhWCwMNNWamhM5MOM1hH3iESPhncGxEUmKGjeGnGLvHQfCAYNKdBs2ZMrx-I_7ponl17V701Y3giwn77UfddJn6Dy7r688096iNGC8hSSaqV3Ie_XCWliT5to_vtgcPv6KYSwQ=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEhGQ68SOPd9SqJgnCkppfpQPimYyfs4z28fyuqTUrYcFfzJ2cO68-UyGP42bCTC_weOxB_myTXp_FQjdulhWrf2WIbkH2dN5Rl_8e-ePpXvl_DklQVZwfeddZtZDCvdq3u07pOPwXMiscmyze-0T4LhmUpyJTJCk28PR6RD8SS10zfP90lWPVPvmF8y8JxJ=s16000)

 **Data Retrieved from Twitter**


![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEh0RMWFNRSEF7faGxxgeok0mECCkDo_xHtjw9HhS7xrUBzAY7s4GSZEFWOdyHeIKLhvsDF4EwLiuW9tyxWQW_hmUNUbykqMn_AGnMq6xXEWFW1MitnRBgfz6WECZABho19jviZQVyGQZgZ2TC3uNevT2Y1qiz8PW3Fd05m9_xWZS0X7fjbC647r5XnuTyX6=s16000)

![App Screenshot](https://blogger.googleusercontent.com/img/a/AVvXsEgzV4WZ_GyXVbZEqsnffmxxQ6vfmoY7nmldTqztTykbnqCHDu9dSGyK9NQcDhPwc1CuxeQbFFpecnQ6_AweH2EGV6zFvBAZaAbWxoahtVU1ceXM8KOe8Z9aq8-6HTQ_TpPooO9DgH85hso0IVybsWN6hfxNcIRNByGxXYHiFZqvib5hcQT6zA2I5xFgWdA2=s16000)

## To-Do

- [ ] Implement Reddit and LinkedIn APIs.
- [ ] Add support for fetching more detailed user information from Instagram and Twitter.
- [ ] Improve error handling and error messages.
- [ ] Enhance the UI/UX of the web application.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

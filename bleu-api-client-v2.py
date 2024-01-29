import requests

class FacekiAPIError(Exception):
    pass


class BleuApiClientV2:


    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://sdk.faceki.com"

    def generate_token(self):
        """
        Generates an access token using client credentials.

        Returns:
            str: Access token for API authentication.

        Raises:
            FacekiAPIError: If token generation fails.
        """
        endpoint = "/auth/api/access-token"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers
        headers = {
            'Content-Type': 'application/json',
        }

        # Set up request data (client ID and client secret)
        data = {
            'clientId': self.client_id,
            'clientSecret': self.client_secret,
        }

        try:
            # Make a POST request to generate the token
            response = requests.post(url, headers=headers, json=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the access token
                return response.json().get('token')
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Token generation failed. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")

    def getKYCRules(self):
        """
        Retrieves KYC rules from the Faceki API.

        Returns:
            dict: KYC rules.

        Raises:
            FacekiAPIError: If the request to get KYC rules fails.
        """
        endpoint = "/kycrules/api/kycrules"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        try:
            # Make a GET request to retrieve KYC rules
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the KYC rules
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Failed to retrieve KYC rules. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")

    def requestKYC(self, selfie_image, doc_front_image, doc_back_image):
        """
        Performs KYC verification using provided images.

        Args:
            selfie_image (str): Path to the selfie image file.
            doc_front_image (str): Path to the front of the identity document image file.
            doc_back_image (str): Path to the back of the identity document image file.

        Returns:
            dict: Verification results.

        Raises:
            FacekiAPIError: If the KYC verification request fails.
        """
        endpoint = "/kycverify/api/kycverify/kyc-verification"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        # Set up request data (selfie image, document front image, document back image)
        data = {
            'selfie_image': selfie_image,
            'doc_front_image': doc_front_image,
            'doc_back_image': doc_back_image,
        }

        try:
            # Make a POST request to perform KYC verification
            response = requests.post(url, headers=headers, json=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the verification results
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"KYC verification failed. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")

    def multiKYCVerification(self, selfie_image, id_front_image, id_back_image, dl_front_image=None, dl_back_image=None, pp_front_image=None, pp_back_image=None):
        """
        Performs multiple KYC verification using provided images.

        Args:
            selfie_image (str): Path to the selfie image file.
            id_front_image (str): Path to the front of the identity document image file.
            id_back_image (str): Path to the back of the identity document image file.
            dl_front_image (str, optional): Path to the front of the driving license image file.
            dl_back_image (str, optional): Path to the back of the driving license image file.
            pp_front_image (str, optional): Path to the front of the passport image file.
            pp_back_image (str, optional): Path to the back of the passport image file.

        Returns:
            dict: Verification results.

        Raises:
            FacekiAPIError: If the multiple KYC verification request fails.
        """
        endpoint = "/kycverify/api/kycverify/multi-kyc-verification"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        # Set up request data (parameters for multiple KYC verification)
        data = {
            'selfie_image': selfie_image,
            'id_front_image': id_front_image,
            'id_back_image': id_back_image,
            'dl_front_image': dl_front_image,
            'dl_back_image': dl_back_image,
            'pp_front_image': pp_front_image,
            'pp_back_image': pp_back_image,
        }

        try:
            # Make a POST request to perform multiple KYC verification
            response = requests.post(url, headers=headers, json=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the verification results
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Multiple KYC verification failed. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")


    def getKycSummary(self):
        """
        Retrieves a list of KYC summaries from the Faceki API.

        Returns:
            dict: KYC summaries.

        Raises:
            FacekiAPIError: If the request to get KYC summaries fails.
        """
        endpoint = "/kycverify/api/kycverify/kyc-verify-summary"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        try:
            # Make a GET request to retrieve KYC summaries
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the KYC summaries
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Failed to retrieve KYC summaries. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")

    def generateKYCLink(self, expire_time, application_id):
        """
        Generates a unique KYC link for user identity verification.

        Args:
            expire_time (int): The expiration time for the generated link in seconds.
            application_id (str): The application ID associated with the link.

        Returns:
            str: Generated KYC link.

        Raises:
            FacekiAPIError: If the request to generate the KYC link fails.
        """
        endpoint = "/kycverify/api/kycverify/kyc-verify-link"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        # Set up request data (parameters for generating KYC link)
        data = {
            'expire_time': expire_time,
            'application_id': application_id,
        }

        try:
            # Make a POST request to generate the KYC link
            response = requests.post(url, headers=headers, json=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the generated KYC link
                return response.json().get('link', '')
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Failed to generate KYC link. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")
    

    def getKYCrecords(self, link_id):
        """
        Fetches KYC records based on the provided link ID.

        Args:
            link_id (str): The unique ID associated with the KYC link.

        Returns:
            dict: KYC records.

        Raises:
            FacekiAPIError: If the request to fetch KYC records fails.
        """
        endpoint = f"/kycverify/api/kycverify/link/{link_id}"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        try:
            # Make a GET request to fetch KYC records
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the KYC records
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Failed to fetch KYC records. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")

    def getKYCrecordsByRequestID(self, request_id):
        """
        Fetches KYC records based on the provided Request ID.

        Args:
            request_id (str): The unique Request ID associated with the KYC records.

        Returns:
            dict: KYC records.

        Raises:
            FacekiAPIError: If the request to fetch KYC records fails.
        """
        endpoint = f"/kycverify/api/kycverify/records/{request_id}"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'application/json',
        }

        try:
            # Make a GET request to fetch KYC records
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the KYC records
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Failed to fetch KYC records. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")


    def faceMatch(self, selfie_image_path):
        """
        Performs a face match verification using the Face Match API.

        Args:
            selfie_image_path (str): The file path to the user's selfie image.

        Returns:
            dict: Result of the face match verification.

        Raises:
            FacekiAPIError: If the request for face match verification fails.
        """
        endpoint = "/facelink/api/face-check"
        url = f"{self.base_url}{endpoint}"

        # Set up request headers with Authorization Bearer Token
        headers = {
            'Authorization': f'Bearer {self.generate_token()}',
            'Content-Type': 'multipart/form-data',
        }

        # Set up request data (parameters for face match)
        files = {
            'selfie_image': (selfie_image_path, open(selfie_image_path, 'rb')),
        }

        try:
            # Make a POST request for face match verification
            response = requests.post(url, headers=headers, files=files)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract and return the result of face match verification
                return response.json()
            else:
                # Raise an exception for unsuccessful requests
                raise FacekiAPIError(f"Face match verification failed. Status code: {response.status_code}, Response: {response.text}")

        except requests.exceptions.RequestException as e:
            # Handle request exceptions
            raise FacekiAPIError(f"Request failed: {str(e)}")
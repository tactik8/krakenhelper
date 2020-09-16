
"""
Helper functions for common tasks.

Provides helper functions to help with common data tasks, avoiding th eneed to load several dfferent libraries of perform error handling.

"""

import validators
from urllib.parse import urlparse
import datetime
import pytz
import uuid


class Url:
    def __init__(self, url = None):
        self.url = url
        self.domain = None
        self.valid = None


    def valid(self, url = None):
        """
        Validate a url format.

        Parameters
        ----------
        url (str): The url to vlaidate

        Returns
        -------
        bool : True if valid, else false
        """

        if url:
            self.url = url
        
        # Error handling
        if not self.url:
            self.valid = False
            return self.valid

        # Perform validation
        self.valid = validators.url(url)
        return self.valid


    def get_domain(self, url = None):
        """
        Returns the domain of a url.

        Parameters
        ----------
        url (str): The url from which to get the domain

        Returns
        -------
        str : The domain of the url or None
        """

        if url:
            self.url = url

        # Error handling
        if not self.url:
            return None
    
        # Get the domain of an url
        
        parsed = urlparse(self.url)
        domain = parsed.netloc
        
        # Put domain in lowercase
        domain = domain.lower()

        domain = domain.replace('www.', '')
        
        self.domain = domain
        return self.domain


class Email:
    def __init__(self, email = None):
        self.email = email
        self.domain = None
        self.valid = None

    def valid(self, email=None):
        """
        Validate an email format.

        Parameters
        ----------
        email (str): The email to validate

        Returns
        -------
        bool : True if valid, else false
        """

        if email:
            self.email = email
        
        self.valid = validators.email(email)
        return self.valid

    def get_domain(self, email = None):
        """
        Returns the domain of an email.

        Parameters
        ----------
        url (str): The email from which to get the domain

        Returns
        -------
        str : The domain of the email or None
        """

        if email:
            self.email = email

        # Error handling
        if not self.email:
            return None

        # Extract domain
        self.domain = self.email.split('@')[1]
        
        return self.domain


class Date:
    def _init__(self, input_date = None):
        self.date = input_date

    # Date handling functions
    def now(self):
        """
        Returns the current date in datetime format.

        Parameters
        ----------

        Returns
        -------
        datetime : The current datetime
        """

        # Returns current datetime 
        self.date = datetime.datetime.now(datetime.timezone.utc)
        return self.date

    def text(self, input_date):
        """
        Returns the date in human-readable date format.

        Parameters
        ----------
        input_date (datetime): The date to convert

        Returns
        -------
        str : The date in human format
        """


        self.text = input_date.strftime("%x")
        return self.text


class UUID:
    def __init__(self):
        self.uuid = None
    
    def get(self):
        """
        Returns a random uuid.

        Parameters
        ----------

        Returns
        -------
        str : A random uuid
        """

        new_uuid = uuid.uuid4()
        self.uuid = str(new_uuid)
        return self.uuid


class Dict:
    def __init__(self, record = None):
        self.record = record


    def is_in(self, dict2):
        """
        Check if dict1 is part of dict 2 (<)

        Parameters
        ----------
        dict1 (dict): The dict to check
        dict2 (dict): The reference dict

        Returns
        -------
        bool : True if dict1 in dict2
        """

        dict1 = self.record

        # error handling
        if not isinstance(dict1, dict):
            dict1 = {}
        if not isinstance(dict2, dict):
            dict2 = {}

        # Comparison
        if dict1.items() <= dict2.items():
            result = True,
        else:
            result = False
        
        return result


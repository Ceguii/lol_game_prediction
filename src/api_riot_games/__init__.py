import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import time
import requests
from typing import List
from handle_api_error import handle_api_error
from config import API_KEY, REGION, RIOT_ID, TAGLINE
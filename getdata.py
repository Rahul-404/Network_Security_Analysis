import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGODB_LOAD_URL= os.getenv("MONGODB_URL")

print(MONGODB_LOAD_URL)

import certifi

cs = certifi.where()

import pandas as pd
import numpy as np

from networksecurity.exception.exception import customexception
from networksecurity.logger.logger import logging


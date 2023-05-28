import os
import sys
from dotenv import load_dotenv
load_dotenv()

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
REPORT_URL = os.getenv("REPORT_URL")
WORKSPACE_ID = os.getenv("WORKSPACE_ID")
USER_ID = os.getenv("USER_ID")
PATH_FOR_USER = URL + "user"
API_KEY = os.getenv("CLOCKIFY_API")
PATH_FOR_TIME_ENTRY = URL + f"workspaces/{WORKSPACE_ID}/user/{USER_ID}/time-entries"
PATH_FOR_TOTAL_DURATION = REPORT_URL + f"workspaces/{WORKSPACE_ID}/reports/summary"

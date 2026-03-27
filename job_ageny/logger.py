
"""
Handles logging of job applications to an Excel file.
"""
import pandas as pd
import os

LOG_FILE = "output/applications_log.xlsx"

def log_application(data):
    if os.path.exists(LOG_FILE):
        df_existing = pd.read_excel(LOG_FILE)
        df_new = pd.concat([df_existing, pd.DataFrame([data])], ignore_index=True)
    else:
        df_new = pd.DataFrame([data])

    df_new.to_excel(LOG_FILE, index=False)
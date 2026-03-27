import os
from job_api import fetch_jobs
from documents import generate_cv, generate_cover_letter, safe_filename
from logger import log_application
import config

# Get absolute path to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define folders properly
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

CV_TEMPLATE = os.path.join(TEMPLATE_DIR, "cv_template.docx")
LETTER_TEMPLATE = os.path.join(TEMPLATE_DIR, "cover_letter_template.docx")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Debug (optional but useful)
    print("CV template path:", CV_TEMPLATE)
    print("Exists:", os.path.exists(CV_TEMPLATE))

    jobs = fetch_jobs(
        config.KEYWORD,
        config.REGION,
        config.OCCUPATION_FIELD,
        config.MAX_JOBS
    )

    for job in jobs:
        title = job["title"]
        company = job["company"]

        filename_base = safe_filename(f"{company}_{title}")

        cv_path = os.path.join(OUTPUT_DIR, f"cv_{filename_base}.docx")
        letter_path = os.path.join(OUTPUT_DIR, f"letter_{filename_base}.docx")

        context = {
            "name": config.NAME,
            "job_title": title,
            "company": company,
            "skills": ", ".join(config.SKILLS)
        }

        generate_cv(CV_TEMPLATE, cv_path, context)
        generate_cover_letter(LETTER_TEMPLATE, letter_path, context)

        log_application({
            "name": config.NAME,
            "job_title": title,
            "company": company,
            "status": "Generated"
        })

        print(f"Created application for {title} at {company}")


if __name__ == "__main__":
    main()
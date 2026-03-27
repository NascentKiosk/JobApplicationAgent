import requests

def fetch_jobs(keyword, region, occupation_field, limit):
    url = "https://jobsearch.api.jobtechdev.se/search"

    params = {
        "q": keyword,
        "region": region,
        "occupation-field": occupation_field,
        "limit": limit
    }

    headers = {
        "User-Agent": "JobAgent/1.0"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    jobs = []

    for ad in data.get("hits", []):
        jobs.append({
            "title": ad.get("headline"),
            "company": ad.get("employer", {}).get("name"),
            "description": ad.get("description", {}).get("text"),
            "apply_url": ad.get("application_details", {}).get("url")
        })

    return jobs
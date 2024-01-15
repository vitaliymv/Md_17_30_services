import datetime

from core.constants import *
import requests

headers = {
    "Content-Type": "application/json",
    "X-Api-Key": API_KEY
}
response = requests.get(PATH_FOR_TIME_ENTRY, headers=headers)
records = response.json()


def convert_to_date(date_str):
    return datetime.datetime.strptime(
        date_str, "%Y-%m-%dT%H:%M:%Sz"
    ).replace(
        tzinfo=datetime.timezone.utc
    ).astimezone(tz=None)


def generate_data():
    data = dict()
    for task in records:
        start = convert_to_date(task['timeInterval']['start'])
        end = convert_to_date(task['timeInterval']['end'])
        duration = end - start
        description = task['description']
        date = start.date()
        if str(date) in data.keys():
            data[str(date)].append({
                "description": description,
                "duration": duration,
                "start": start,
                "end": end
            })
        else:
            data.update({
                str(date): [{
                    "description": description,
                    "duration": duration,
                    "start": start,
                    "end": end
                }]
            })
    return data


def get_total_duration(start, end):
    body = {
        "dateRangeStart": start,
        "dateRangeEnd": end,
        "summaryFilter": {
            "groups": [
                "USER"
            ]
        },
        "exportType": "JSON"
    }
    return requests.post(
        url=PATH_FOR_TOTAL_DURATION,
        json=body,
        headers=headers
    ).json()["totals"][0]["totalTime"]

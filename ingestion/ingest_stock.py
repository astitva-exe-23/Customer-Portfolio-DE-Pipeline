import requests
import json
from datetime import datetime
from config.configuration import API_URL, API_KEY, SYMBOLS, BUCKET_NAME
from utils.s3_utils import get_s3_client

import requests
import time

def fetch_stock_data():
    all_data = []
    all_meta = []

    for i in range(0, len(SYMBOLS), 3):
        batch = SYMBOLS[i:i+3]
        params = {
            "api_token": API_KEY,
            "symbols": ",".join(batch)
        }

        response = requests.get(API_URL, params=params)

        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code}")

        result = response.json()

        # Track API behavior (important)
        all_meta.append(result.get("meta", {}))

        if "data" in result:
            all_data.extend(result["data"])

        time.sleep(1)  # avoid rate limits

    return {
        "meta": all_meta,
        "data": all_data
    }

def upload_to_s3(data):
    s3 = get_s3_client()

    today = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H-%M-%S")

    key = f"bronze/stock_api/date={today}/stock_{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(data)
    )

    print(f"Uploaded to s3://{BUCKET_NAME}/{key}")

if __name__ == "__main__":
    data = fetch_stock_data()

    if "data" not in data or len(data["data"]) == 0:
        raise Exception("Empty API response")
    if len(data["data"]) < len(SYMBOLS):
        print("⚠️ WARNING: Some symbols may be missing due to API limits")

    upload_to_s3(data)
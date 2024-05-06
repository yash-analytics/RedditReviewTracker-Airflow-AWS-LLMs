import os
import instructor
from openai import OpenAI
from pydantic_class.models import LabelRedditPosts
import json
import pandas as pd

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

def data_enhancement(csv_path: str, output_csv_path: str):

    try:
        data = pd.read_csv(csv_path)
        ...
    except Exception as e:
        print(f"Failed to process data: {str(e)}")
        raise

    # Initialize the OpenAI client
    client = instructor.patch(OpenAI())

    # Lists to store the new column data
    post_category = []
    sentiments = []

    # Iterate through each title in the DataFrame
    for title in data['title']:
        # Prepare the API request
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            response_model = LabelRedditPosts,
            messages=[
                {"role": "user", "content": f"Classify the sentiment and category of this Reddit post title: '{title}'"},
            ],
        )

        # Process the response and extract data
        response_data = json.loads(response.model_dump_json())
        post_category.append(response_data.get('post_category', 'Unknown'))
        sentiments.append(response_data.get('sentiment', 'Neutral'))

    # Add the new columns to the DataFrame
    data['post_category'] = post_category
    data['sentiment'] = sentiments

    # Save the enhanced DataFrame to a new CSV
    data.to_csv(output_csv_path, index=False)

    print(f"Enhanced data saved to {output_csv_path}")
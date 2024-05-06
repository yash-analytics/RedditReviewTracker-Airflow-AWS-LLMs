from pydantic import BaseModel, Field
from typing import Literal

class LabelRedditPosts(BaseModel):
    post_category: Literal['Technical', 'Business', 'Customer Support', 'Other'] = Field(
        ..., description='Category of the post', example='Technical'
    )

    sentiment: Literal['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive'] = Field(
        ..., description='Sentiment of the post', example='Very Negative'
    )
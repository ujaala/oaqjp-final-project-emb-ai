import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Check if the API request was successful
    if response.status_code != 200:
        return {"error": f"API request failed with status code {response.status_code}"}
    
      # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting sentiment label and score from the response
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    
    # Create a list of emotion scores
    emotion_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    
    # Find the index of the dominant emotion
    dominant_emotion_index = emotion_list.index(max(emotion_list))
    
    # Mapping emotion index to emotion name
    emotion_keys = ["anger", "disgust", "fear", "joy", "sadness"]
    dominant_emotion_key = emotion_keys[dominant_emotion_index]

    # Prepare the result dictionary
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_key
    }
    
    return result  # Return the final result dictionary
# Example usage
if __name__ == "__main__":
    text_to_analyse = "I am so happy I am doing this."
    result = emotion_detector(text_to_analyse)
    print(result)  # Print the result
import http.client
import json

# Language index mapping 
language_map = {
    1: ('English', 'en'),
    2: ('French', 'fr'),
    3: ('Spanish', 'es'),
    4: ('German', 'de'),
    5: ('Italian', 'it'),
    6: ('Portuguese', 'pt'),
    7: ('Russian', 'ru'),
    8: ('Chinese (Simplified)', 'zh'),
    9: ('Japanese', 'ja'),
    10: ('Korean', 'ko'),
    11: ('Hindi', 'hi'),
    12: ('Tamil', 'ta'),
    13: ('Telugu', 'te'),
    14: ('Bengali', 'bn'),
    15: ('Gujarati', 'gu'),
    16: ('Kannada', 'kn'),
    17: ('Malayalam', 'ml'),
    18: ('Marathi', 'mr'),
    19: ('Punjabi', 'pa'),
    20: ('Urdu', 'ur'),
    21: ('Arabic', 'ar'),
    22: ('Turkish', 'tr'),
    23: ('Vietnamese', 'vi'),
    24: ('Thai', 'th'),
    25: ('Dutch', 'nl'),
    26: ('Greek', 'el'),
    27: ('Hebrew', 'iw'),
    28: ('Polish', 'pl'),
    29: ('Ukrainian', 'uk'),
    30: ('Romanian', 'ro')
}

# Show language options
print("Select the target language:")
for idx, (lang, code) in language_map.items():
    print(f"{idx}. {lang} ({code})")

# Take user input for text
text_to_translate = input("\nEnter the text to translate: ")

# Take user input for language (number or code)
user_input = input("Enter the number or code of the target language (e.g., 2 or fr): ").strip()

# Determine target language code
target_language = None
if user_input.isdigit():
    lang_choice = int(user_input)
    target_language = language_map.get(lang_choice, (None, None))[1]
else:
    for lang, code in language_map.values():
        if user_input.lower() == code:
            target_language = code
            break

if not target_language:
    print("Invalid selection. Exiting.")
    exit()

# Setup HTTPS connection
conn = http.client.HTTPSConnection("google-translate113.p.rapidapi.com")

# Prepare the payload
payload = {
    "from": "auto",
    "to": target_language,
    "protected_paths": [],
    "common_protected_paths": [],
    "json": {
        "text": text_to_translate
    }
}

headers = {
    'x-rapidapi-host': "google-translate113.p.rapidapi.com",
    'x-rapidapi-key': "b3f908e177mshc6e18f1ad07cbb6p183bdbjsne93bc24941dc",  
    'Content-Type': "application/json"
}

# Send the translation request
conn.request("POST", "/api/v1/translator/json", body=json.dumps(payload), headers=headers)

res = conn.getresponse()
data = res.read()

# Parse response and extract translated text
translated = json.loads(data.decode("utf-8"))
translated_text = translated['trans']['text']

print("\nTranslated Text:", translated_text)

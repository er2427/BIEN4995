import json
import requests

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Extract variables
vna_url = config['options']['vna_url']
api_key = config.get('api_key')
modalities = config.get('modalities', {})
start_time = config.get('start_time')
end_time = config.get('end_time')


# Save variables to a TXT file
with open('variables.txt', 'w') as txt_file:
    txt_file.write(f"VNA URL: {vna_url}\n")
    txt_file.write(f"API Key: {api_key}\n")
    txt_file.write(f"Modalities: {modalities}\n")
    txt_file.write(f"Start Time: {start_time}\n")
    txt_file.write(f"End Time: {end_time}\n")


# Function to make API calls and get study UIDs
def get_study_uids(modality):
    # Make API call here and extract study UIDs
    # Modify the API endpoint and parameters based on your VNA API documentation

    # https://colab.research.google.com/drive/1J_63kTnmt7h5qUCBrno0FGdrGafEedTp
      # code from SIIM this summer used for OMOP group
      # has api call examples in it

    # https://hackathon.siim.org/dicomweb/
      #

    # https://hackathon.siim.org/dicomweb/studies?00080061=CT
        # include a date range that the studies should be from
        # find the use "includefeild" to just pull patient uid from
          # dicom tag for patient UID 0020000D
        # 00080061 tag for modality

    # also need a api request for the dicom image
      #

    api_endpoint = f"{vna_url}/api/{modality}/studies"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        study_uids = [study.get('StudyInstanceUID') for study in response.json()]
        return study_uids
    else:
        print(f"Error fetching study UIDs for {modality}: {response.status_code}")
        return []

# Iterate through modalities and get study UIDs
all_study_uids = {}
for modality, enabled in modalities.items():
    if enabled:
        study_uids = get_study_uids(modality)
        all_study_uids[modality] = study_uids

# Print or save the study UIDs as needed
print("Study UIDs for each modality:", all_study_uids)










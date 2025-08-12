from google_auth_oauthlib.flow import InstalledAppFlow

# Gmail scopes — use gmail.modify if you want to send, delete, mark as read, etc.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Create the flow using the client_secret.json you downloaded
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)

# This will open your browser to log in
creds = flow.run_local_server(port=0, prompt="consent")

# Save to file locally (optional)
with open("token.json", "w") as token:
    token.write(creds.to_json())

# Print for pasting into GOOGLE_OAUTH_TOKEN env var
print("\n----- COPY THIS INTO GOOGLE_OAUTH_TOKEN -----\n")
print(creds.to_json())
print("\n----- END -----")


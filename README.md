# YouTube Uploader

## Introduction

This project was created based on code samples from YouTube's Python API documentation with adjustments made to enable mass uploads using a CSV metadata file.

[This page](https://developers.google.com/youtube/v3/guides/uploading_a_video) in the YouTube API documentation was very helpful for creating this project.

## Create OAuth tokens

First, you need to enable the YouTube API and setup a client_id and client_secret.  To do this, follow the steps below.

1. Go to the [Google Cloud Console](https://console.cloud.google.com)
1. Create a new project by clicking **Select a project** in the header and then click **NEW PROJECT**.  *Note: If you already have a project, the **Select a project** button will be the name of the current project you are viewing.*
1. Add a name for the project (i.e. Python YouTube uploader)
1. After the project is created, click **Select a project** and select the project you just created
1. In the left sidebar click **APIs & Services** -> **Dashboard**
1. Click **ENABLE APIS AND SERVICES**
1. Enter **YouTube** in the search box and select **YouTube Data API v3**
1. Click **Enable**
1. Once the API is enabled, click **Credentials** in the left sidebar
1. Click **Create credentials** and select the option **OAuth client ID**
1. If a message appears about setting a product name for the consent screen follow these instructions.
   1. click **Configure consent screen**
   1. Enter a product name in the field labeled **Product name shown to users** (i.e. Python YouTube uploader)
   1. Click **Save**
1. Select **Other** for the application type and name it what you would like (i.e. Python YouTube uploader)
1. Copy the client ID and the client secret to use when running the create tokens command

Now that you have that, run the following command to create OAuth2 tokens.

```bash
python create_oauth_token.py
```

## Running the upload script

To use, add the videos you would like to upload to files.csv.  Then you can invoke the script using the code below.

```bash
python youtube.py
```

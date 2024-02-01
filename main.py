import requests
import json
from dotenv import load_dotenv 
import pymysql.cursors 
import pymysql
import os
from bs4 import BeautifulSoup


load_dotenv()

def lambda_handler(event, context):
    message = event['message']['text']
    chat_id = event['message']['chat']['id']

    try:
        title = get_url_title(message)
    except:
        sendMessage(chat_id, 'Error getting title from message')
        return {'statusCode': 400}
    
    table = 'bookmarks'
    cnxn = connect()
    try: 
        with cnxn:
            with cnxn.cursor() as cursor:
                query = """INSERT INTO bookmarks (title, url) VALUES (%s, %s)"""
                cursor.execute(query, (title, message))
            cnxn.commit()
    except:
        sendMessage(chat_id, 'Failed bookmarking the url.')


    sendMessage(chat_id, 'URL bookmarked successfully.')

    return {
        'statusCode': 200,
    }

def sendMessage(chat_id, message):
    url = f"{os.getenv('TELEGRAM_API')}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, data)
    if response.status_code == 200:
        print('Message sent successfully.')
    else: 
        print('Failed sending message.')


def connect():
    cnxn = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return cnxn


def get_url_title(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title tag and extract its text
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.text.strip()
        else:
            return "No title found on the page."
    else:
        raise ValueError(f'Request failed with status code {response.status_code}: {response.text}')

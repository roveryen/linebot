from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import logging
import openai
import re

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

openai.api_key = "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"


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s',
                    filename = '/project/logs/log.txt')


def get_response_from_chatgpt(message):

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message,
        max_tokens=128,
        temperature=0.5
    )

    logging.info(response)

    completed_text = response['choices'][0]['text']
    return completed_text


def check_spam_message(message):
    try:
        message = re.sub(r"\s+", "", message)
        message = re.sub(r"[,/]+", "", message)
        logging.info(message)

    except:
        return False

    return True

# override callback function of csrf_exempt
@csrf_exempt
def callback(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        # events from LINE
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()

    for event in events:
        if isinstance(event, MessageEvent):

            #logging.info(event)

            message = event.message.text

            reply_message = message

            check_spam_message(message)

            reply_message = get_response_from_chatgpt(message)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply_message)
            )

    return HttpResponse()



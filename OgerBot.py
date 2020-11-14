import os
import time
import json
import random
import threading
import re
import urllib.request
from datetime import datetime

import praw
import yaml
from prawcore import NotFound


class OgreBot(threading.Thread):
    __config = dict()
    __dictionary = dict()
    __error_dictionary = dict()
    __header_dictionary = dict()
    __active_bots = list()
    __bot_name = str
    __reddit = praw.Reddit
    __is_cancellation_requested = False
    __test_mode = bool

    # Constructor of the "Ogre_Bot" Jesus....
    def __init__(self, bot_name, bot_user_agent, test_mode=False):

        if bot_name in self.__active_bots:
            raise Exception("This bot already Exists")

        self.__test_mode = test_mode
        self.__config = self.__init_config_instance()
        self.__dictionary = self.__init_dictionary("dict/dictionary_default.json")
        self.__error_dictionary = self.__init_dictionary("dict/dictionary_error_messages.json")
        self.__header_dictionary = self.__init_dictionary("dict/dictionary_header.json")
        self.__reddit = self.__init_reddit_instance(bot_name, bot_user_agent)
        self.__bot_name = bot_name
        self.__active_bots.append(bot_name)

        # Constructor of super class (Threading)
        threading.Thread.__init__(self)
        print("Created Bot: " + self.__bot_name)

    # Deconstructer
    def __del__(self):
        self.__active_bots.remove(self.__bot_name)
        print("Deleted Bot: " + self.__bot_name)

    # Override of super class starts the Thread
    def start(self) -> None:
        self.__is_cancellation_requested = False
        super().start()
        print("Started Bot: " + self.__bot_name)

    # stop current Bot
    def stop(self):
        self.__is_cancellation_requested = True
        print("Stopped Bot: " + self.__bot_name)

    # Override of super class for Run Function => Threading
    def run(self):

        while not self.__is_cancellation_requested:

            try:

                time.sleep(self.__config['BOT_TIMEOUT_MS'] / 1000)

                # Search mentions in inbox
                inbox = list(self.__reddit.inbox.unread(limit=self.__config['BOT_INBOX_LIMIT']))
                inbox.reverse()
                for message in inbox:
                    try:
                        if self.__check_if_valid_message(message):
                            self.__process_message(message)
                        else:
                            message.mark_read()
                    except Exception as e:
                        print(e)
                        self.__send_error_message(message)

            except NotFound:
                pass
            except Exception as e:
                print(e)

    def __process_message(self, message):

        try:

            if "u/" + self.__bot_name + " \\--" in message.body:

                additional_parameter = re.search("--(.*)", message.body)
                additional_parameter = additional_parameter.group(1).split(" ")[0]

                # Switch case maybe?
                if additional_parameter == 'error':
                    self.__send_error_message(message)
                    return

            message_to_translate = message.parent()

            if isinstance(message_to_translate, praw.reddit.Submission):
                title = message_to_translate.title
                body = message_to_translate.selftext
                text_to_translate = "**" + title + "**" + "\n\n" + body
            else:
                text_to_translate = message_to_translate.body

            translated_text = self.__translate_to_ogre_speak(text_to_translate)

            reply = self.__config['HEADER'] + random.choice(self.__header_dictionary['header']) + translated_text + \
                    self.__config['FOOTER']

            if not self.__test_mode:
                message.reply(reply)
                message.mark_read()

            print("New Comment!!!"
                  + "\n\nTime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                  + "\n\nFrom: " + str(message.author)
                  + "\n\nOriginal Text: " + text_to_translate
                  + "\n\nTranslation: " + translated_text
                  + "\n\n")

        except Exception as e:
            print(e)
            self.__send_error_message(message)
            return

    def __translate_to_ogre_speak(self, text_to_translate):

        full_list = self.__dictionary['translate']
        text_to_translate = text_to_translate.splitlines()
        translated_text_bytes = b""

        # NO!!! you can't just go through a whole Json Dictionary and check everything twice
        # hahah for loops go: brrrrrrrrrrrrrrrrrrrrrrrr

        for line_to_translate in text_to_translate:

            translated_line = line_to_translate

            for key, item in full_list.items():
                word_to_translate = re.escape(key)
                translated_line = re.sub(word_to_translate, lambda m: re.escape(random.choice(item)), translated_line)

            translated_text_bytes += translated_line.encode() + b'\n'

        return translated_text_bytes.decode("utf-8").replace("\\", "")

    def __check_if_valid_message(self, message):
        if message.type == 'username_mention' or 'u/' + self.__bot_name in message.body:
            return True
        return False

    def __send_error_message(self, message):

        try:
            error_message = random.choice(self.__error_dictionary['error'])
            print(error_message)

            reply = self.__config['HEADER_ERROR'] + error_message + self.__config['FOOTER_ERROR']

            if not self.__test_mode:
                message.reply(reply)
                message.mark_read()

        except Exception as e:
            print(e)
            self.__reply_per_pm(message)
            message.mark_read()
            return

    @staticmethod
    def __reply_per_pm(message):
        reply = "Sorry ich hab nicht funktioniert, evtl. bin ich in diesem Sub gebannt :("
        topic = "Whoops"
        user = message.author
        user.message(topic, reply)

    @staticmethod
    def __init_reddit_instance(bot_name, bot_user_agent):
        return praw.Reddit(bot_name, user_agent=bot_user_agent)

    @staticmethod
    def __init_config_instance():
        conf_file = os.path.relpath("cfg/config.yaml")
        with open(conf_file, encoding='utf8') as f:
            configuration = yaml.safe_load(f)

        configuration['FOOTER'] = "\n\n ***  \n" + configuration['INFO_LINK'] \
                                  + "&#32;|&#32;" + "&#32;|&#32;" + configuration['GITHUB_LINK']\
                                  + "&#32;|&#32;" + "&#32;|&#32;" + "**NEW** " + configuration['CHANGELOG_LINK']

        configuration['FOOTER_ERROR'] = "\n\n ***  \n" + configuration['INFO_TEXT_ERROR'] + "\n" \
                                        + configuration['INFO_LINK'] + "&#32;|&#32;" + "&#32;|&#32;" \
                                        + configuration['GITHUB_LINK'] \
                                        + "&#32;|&#32;" + "&#32;|&#32;" + "**NEW** " + configuration['CHANGELOG_LINK']

        return configuration

    @staticmethod
    def __init_dictionary(path):
        json_path = os.path.relpath(path)
        with open(json_path, encoding='utf-8') as json_file:
            return json.load(json_file)


def startup():
    try:
        url = os.environ['PRAWURL']
        urllib.request.urlretrieve(url, 'praw.ini')
        my_bot = OgreBot("DeutschZuOgerBot", "PastaPizzaSecretAgent", test_mode=False)
        my_bot.start()
        while True:
            time.sleep(20)
    except Exception as e:
        print(e)
        print("Restarting...")
        del my_bot
        startup()


# init and run routine
if __name__ == '__main__':
    startup()

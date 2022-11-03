import requests
import time
import datetime
import urllib3

import mock_server

http = urllib3.PoolManager()
FAILURES = 3
TIMEOUT = datetime.timedelta(0,6)
STATUS = "CLOSED"
CURRENT_FAILURE = 0
CURRENT_TIME = 0


def get_greeting(url, port):
    global CURRENT_TIME
    CURRENT_TIME = datetime.datetime.now()
    response = requests.get("http://{}:{}/".format(url, port))
    return response


def greetings_test(iterations=10, delay=1, url="localhost", port=5000):
    global CURRENT_FAILURE
    global STATUS
    global CURRENT_TIME
    ans = ''
    for i in range(iterations):
        try:
                if (STATUS == "CLOSED"):
                    a = get_greeting(url, port)
                    ans = a.status_code
                elif (datetime.datetime.now() - CURRENT_TIME) > TIMEOUT and STATUS == "OPEN":
                    STATUS = "HALF-OPEN"
                elif (STATUS == "OPEN"):
                    CURRENT_FAILURE += 1
                    ans = ("wait")
                    pass

                elif STATUS == "HALF-OPEN":
                    a = get_greeting(url, port)
                    STATUS = "CLOSED"
                    CURRENT_FAILURE = 0
        except:
            if CURRENT_FAILURE == 0:
                CURRENT_TIME = datetime.datetime.now()
                ans = ("Ошибка сервера")
            CURRENT_FAILURE += 1
            if STATUS == "HALF-OPEN":
                CURRENT_TIME = datetime.datetime.now()
            if (CURRENT_FAILURE >= FAILURES) and STATUS != "OPEN":
                STATUS = "OPEN"

        print(ans, STATUS)
        time.sleep(delay)


if __name__ == "__main__":
    print("Server is turned OFF...")
    greetings_test()

    print("Server is turning ON...")
    with mock_server.app.run("localhost", 5000):
        greetings_test()

    print("Server is turned OFF...")
    greetings_test()

    print("Server is turning ON...")
    with mock_server.app.run("localhost", 5000):
        greetings_test()

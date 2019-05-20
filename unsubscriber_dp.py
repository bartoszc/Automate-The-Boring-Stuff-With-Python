#! python3
# unsubscriber.py - scans through  email, finds all the unsubscribe links in all  emails, and  opens them in a browser

import sys
import bs4
import imapclient
import pyzmail
import webbrowser
import threading


class Unsubscribe:
    class __Unsubscribe:
        def __init__(self, provider, login, password, folder):
            self.__provider = provider
            self.__login = login
            self.__password = password
            self.__folder = folder

    instance = None

    def __init__(self, provider, login, password, folder):
        if not Unsubscribe.instance:
            Unsubscribe.instance = Unsubscribe.__Unsubscribe(provider, login, password, folder)
        else:
            Unsubscribe.instance.__provider = provider
            Unsubscribe.instance.__login = login
            Unsubscribe.instance.__password = password
            Unsubscribe.instance.__folder = folder

    def process(self):
        imapObj = imapclient.IMAPClient(Unsubscribe.instance.__provider, ssl=True)
        imapObj.login(Unsubscribe.instance.__login, Unsubscribe.instance.__password)
        imapObj.select_folder(Unsubscribe.instance.__folder, readonly=True)
        emails = imapObj.search(['ALL'])

        for email in emails:
            raw_email = imapObj.fetch([email], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_email[email][b'BODY[]'])
            if not message.html_part:
                continue
            else:
                soup = bs4.BeautifulSoup(message.html_part.get_payload().decode(message.html_part.charset), features='html.parser')
                for element in soup.find_all('a', href=True):
                    if element.text.lower() == 'unsubscribe':
                        webbrowser.open(element['href'])

    def threading(self):
        # Create and start the Thread objects.
        unsubscribed_emails = []
        for i in range(2):
            ue = threading.Thread(target=self.process)
            unsubscribed_emails.append(ue)
            ue.start()

        # Concurrency pattern - dalsze wykonywanie programu odbywa się po zakończeniu wszystkich 20 wątków
        for ue in unsubscribed_emails:
            ue.join()
        print('Done')


u1 = Unsubscribe('imap.gmail.com', 'bartosz.chojnacki4@gmail.com', sys.argv[1], 'Test')
u1.process()
u1.threading()


# Blad: instancja klasy Unsubscribe juz istnieje
#  u2 = Unsubscribe('imap.gmail.com', 'bartosz.chojnacki4@gmail.com', sys.argv[1], 'Test')


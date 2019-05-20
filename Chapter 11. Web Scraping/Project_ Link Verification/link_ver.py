# USAGE python linkver.py <url>


import logging, sys, requests, bs4, os

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

if len(sys.argv) == 2:
    # TODO: get url
    url = sys.argv[1]
    # TODO: get page
    try:
        res = requests.get(url)
        res.raise_for_status()
        # TODO: get all links
        page_soup = bs4.BeautifulSoup(res.text, "html.parser")
        page_links = page_soup.select("a")
        # TODO: create and write links into respective text files
        good_file = open("good_links.txt", "w")
        bad_file = open("bad_links.txt", "w")
        good_file.close()
        bad_file.close()
        # TODO: create and write links into respective text files
        good_file = open("good_links.txt", "a")
        bad_file = open("bad_links.txt", "a")
        # TODO: make requests to all links
        for link in page_links:
            link = link.get("href")
            if not link.startswith("http"):
                link = url + link
            try:
                link_res = requests.get(link)
                # TODO: get status code
                status = link_res.status_code
                # TODO: update 404 and good pages list
                if int(status) == 200:
                    good_file.write(link + "\n")
                    logging.info("Good links written")
                else:
                    bad_file.write(link + "\n")
                    logging.info("Bad links written")
            except Exception as err:
                logging.error("Page Link Error: " + str(err))

        good_file.close()
        bad_file.close()
    except Exception as err:
        logging.error("Url Error: " + str(err))
else:
    logging.error("USAGE python linkver.py <url>")
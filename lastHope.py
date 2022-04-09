from selenium import webdriver
from selenium.webdriver.common.by import By
from scripy import CleanAuthors
from scripy import CleanAffiliate
from scripy import CleanJournal


def pubmed(term):
    link = []
    for i in range(1,50):
        #url to be scraped
        pubmed_url = "https://pubmed.ncbi.nlm.nih.gov/?term="+term+"&page="+str(i)
        driver = webdriver.Chrome()
        driver.get(pubmed_url)
        links = driver.find_elements(By.CLASS_NAME, "docsum-pmid")
        for c in links:
            link.append(c.text)
        driver.close()

    print(link)

    for l in link:
        driver = webdriver.Chrome()
        linko = "https://pubmed.ncbi.nlm.nih.gov/" + l
        driver.get(linko)

        journal = driver.find_element(By.CLASS_NAME, "article-source")
        J = CleanJournal.getJournal(journal.text)

        Date = CleanJournal.ExtractDateFromString(journal.text)

        title = driver.find_element(By.CLASS_NAME, "heading-title")
        Titre = title.text

        authors = driver.find_elements(By.CLASS_NAME, "full-name")
        author = []
        for a in authors:
            author.append(a.text)
        Author = CleanAuthors.removeNoneList(author)

        element = driver.find_element(By.CLASS_NAME, "more-details")
        element.click();
        affi = driver.find_element(By.CLASS_NAME, "item-list")
        affiliate = CleanAffiliate.cleanAffiliate(affi.text)

        location = CleanAffiliate.whereAreLocations(affiliate)

        brevet = {
            "Titre" : Titre,
            "Date" : Date,
            "Journal" : J,
            "Authors": Author,
            "Affiliate" : affiliate,
            "Location" : location,
            "PMID" : l,
            "link" : linko,
        }
        print(brevet)
        driver.close()
    return brevet


try:
    print(pubmed("data"))
except Exception as e:
    print(e)
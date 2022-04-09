class CleanAuthors():
    def removeNoneList(list):
        l = []
        for c in list:
            if c != '':
                l.append(c)
        return l


class CleanAffiliate():
    def cleanAffiliate(text):
        x = text.split(".\n")
        temp = []
        for i in range(len(x)):
            temp.append(x[i][2:])
        return temp

    def whereAreLocations(list):
        import nltk
        import spacy
        import locationtagger

        """# essential entity models downloads
        nltk.downloader.download('maxent_ne_chunker')
        nltk.downloader.download('words')
        nltk.downloader.download('treebank')
        nltk.downloader.download('maxent_treebank_pos_tagger')
        nltk.downloader.download('punkt')
        nltk.download('averaged_perceptron_tagger')"""
        #spacy.load('en_core_web_sm')

        for c in list:
            # extracting entities.
            place_entity = locationtagger.find_locations(text=c)

            location = {}
            c = []
            # getting all countries
            c.extend(place_entity.countries)
            if len(c) != 0:
                location["countries"] = c

            r = []
            # getting all states
            r.extend(place_entity.regions)
            if len(r)!= 0:
                location["regions"] = r

            cy = []
            # getting all cities
            cy.extend(place_entity.cities)
            if len(cy)!=0:
                location["cities"] = cy

        return location


class CleanJournal():
    def ExtractDateFromString(text):
        import re
        from datetime import datetime

        # searching string
        match_str = re.search(r'\d{4}', text)
        # computed date
        # feeding format
        res = datetime.strptime(match_str.group(), '%Y').date()
        # result
        return str(res)

    def getJournal(text):
        x = text.split(".")
        return x[0]

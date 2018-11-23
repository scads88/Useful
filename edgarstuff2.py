import requests
import bs4


_CIK_URI = 'http://www.sec.gov/cgi-bin/browse-edgar' \
           '?action=getcompany&CIK={s}&count=10&output=xml'


def get_cik(symbol):
    """
    Retrieves the CIK identifier of a given security from the SEC based on that
    security's market symbol (i.e. "stock ticker").
    :param symbol: Unique trading symbol (e.g. 'NVDA')
    :return: A corresponding CIK identifier (e.g. '1045810')
    """

    response = requests.get(_CIK_URI.format(s=symbol))
    page_data = bs4.BeautifulSoup(response.text, "html.parser")
    cik = page_data.companyinfo.cik.string
    return cik
print(get_cik("WMT"))
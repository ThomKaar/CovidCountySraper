# a list of dictionaries where the key countyName is paired with a countyName in CA
# and the key url is paired with a url to that county's covid stats on google news
urls = [
    {
        'countyName': 'San Luis Obispo',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2v0&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Los Angeles',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kpys&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'San Francisco',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fg%2F11g6njkk2y&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Alameda',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kpzy&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Contra Costa',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kq1l&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'San Diego',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2rj&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Riverside',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2q3&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'San Bernardino',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kvt9&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Orange',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0cb4j&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Sacramento',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0bxqq&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Santa Clara',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2xl&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Kern',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kv5t&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Fresno',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0kq39&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'San Joaquin',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2sr&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Ventura',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l38x&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Stanislaus',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l35x&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Tulare',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l380&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'San Mateo',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2vz&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Monterey',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2lk&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Santa Barbara',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2wt&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Solano',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l34j&gl=US&ceid=US%3Aen'
    },
    {
        'countyName': 'Merced',
        'url': 'https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0l2k7&gl=US&ceid=US%3Aen'
    }
]


# Given a string parse it to an integer
def parseInt(str):
    return int(str.replace(',', ''))
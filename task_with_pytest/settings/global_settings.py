from urllib.parse import urljoin

# URLs
WIKIPEDIA_URL = 'https://en.wikipedia.org/'
WIKIPEDIA_WIKI_POSTFIX = 'wiki/'
WEBSITES_PROGRAMMING_LANGUAGES_URL = urljoin(
    WIKIPEDIA_URL, WIKIPEDIA_WIKI_POSTFIX + 'Programming_languages_used_in_most_popular_websites'
)

# Timeouts
DEFAULT_PERFORMANCE_TIMEOUT = 5
SMALL_TIMEOUT = 2

# Constants
POPULARITY = 'popularity'

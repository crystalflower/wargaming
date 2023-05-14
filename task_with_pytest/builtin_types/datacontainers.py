from dataclasses import dataclass


@dataclass
class WebsiteProgrammingLanguages:
    websites: str
    frontend: str
    backend: str
    database: str
    popularity: int = None
    notes: str = None

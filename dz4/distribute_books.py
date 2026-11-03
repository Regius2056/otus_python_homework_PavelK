import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
BOOKS_FILE = BASE_DIR / 'books.csv'
USERS_FILE = BASE_DIR / 'users.json'
RESULT_FILE = BASE_DIR / 'result.json'


def read_books(path: Path) -> list[dict]:
    """Read books from CSV and convert them to the result format."""
    with path.open(encoding='utf-8-sig', newline='') as f:
        return [
            {
                'title': row['Title'],
                'author': row['Author'],
                'pages': int(row['Pages']),
                'genre': row['Genre'],
            }
            for row in csv.DictReader(f)
            if row.get('Title')
        ]


def read_users(path: Path) -> list[dict]:
    """Read users from JSON and keep only required fields."""
    with path.open(encoding='utf-8') as f:
        return [
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': [],
            }
            for user in json.load(f)
        ]


def distribute(books: list[dict], users: list[dict]) -> list[dict]:
    """Distribute books as evenly as possible; first users get the remainder."""
    base, extra = divmod(len(books), len(users))
    start = 0
    for i, user in enumerate(users):
        count = base + (1 if i < extra else 0)
        user['books'] = books[start:start + count]
        start += count
    return users


def main() -> None:
    result = distribute(read_books(BOOKS_FILE), read_users(USERS_FILE))
    with RESULT_FILE.open('w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()


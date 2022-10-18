from django.core.management.base import BaseCommand
import json
from books.models import Book


class Command(BaseCommand):
    help = u'Внесение данных из json-файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help=u'Путь к json-файлу')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for book in data:
            if book['model'] == 'books.book':
                instance = Book(id=book['pk'],
                                name=book['fields']['name'],
                                author=book['fields']['author'],
                                pub_date=book['fields']['pub_date'])
                instance.save()







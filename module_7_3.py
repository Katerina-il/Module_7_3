import io
from pprint import pprint

"""
Домашнее задание по теме "Оператор "with"
Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:

WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и 
записывать их в атрибут file_names в виде списка или кортежа.

"""

class WordsFinder:
    file_names = []
    file_names_tuple= ()

    def __init__(self, *files):
        self.file = files
        self.file_names.append(self.file)
        self.file_names_tuple += self.file

    def get_all_words(self):  # метод, который возвращает словарь {'file.txt': ['word1', 'word2']}
        all_words ={}

        for search_file in self.file_names_tuple: # Переберите названия файлов и открывайте каждый из них

            with open(search_file, 'r', encoding ='utf-8') as file:
                words = []
                lines_in_files = ""
                for line in file:
                    lines_in_files += (line + "\n").lower()
                def remove_string(string):
                    punc = {ord(',') : None, ord('.') : None, ord('='): None, ord('!'): None, ord('?'): None,
                            ord(';'): None, ord(':'): None, ord("—"): None, ord('-'): None} #ord(' - ') : None,
                    return string.translate(punc)
                lines_in_files = remove_string(lines_in_files)
                words = lines_in_files.split()
            all_words[search_file] = words
        return all_words

    def find(self, word):
        dict_words = {}
        for search_file in self.file_names_tuple: # Переберите названия файлов и открывайте каждый из них
            with open(search_file, 'r', encoding ='utf-8') as file:
                words = []
                lines_in_files = ""
                for line in file:
                    lines_in_files += (line + "\n").lower()
                def remove_string(string):
                    punc = {ord(',') : None, ord('.') : None, ord('='): None, ord('!'): None, ord('?'): None,
                            ord(';'): None, ord(':'): None, ord("—"): None, ord('-'): None} #ord(' - ') : None,
                    return string.translate(punc)
                lines_in_files = remove_string(lines_in_files)
                words = lines_in_files.split()

                for search_word in words:
                    if search_word.lower() == word.lower():
                        count = words.index(search_word) + 1
                        dict_words[search_file] = count

            return dict_words
        return dict_words
    #
    def count(self, word):
        all_words = {}
        count_word = {}

        for search_file in self.file_names_tuple:  # Переберите названия файлов и открывайте каждый из них
            count_word = {}

            with open (search_file, 'r', encoding='utf-8') as file:
                words = []
                lines_in_files = ""
                for line in file:
                    lines_in_files += (line + "\n").lower()

                def remove_string(string):
                    punc = {ord(','): None, ord('.'): None, ord('='): None, ord('!'): None, ord('?'): None,
                            ord(';'): None, ord(':'): None, ord("—"): None, ord('-'): None}
                    return string.translate(punc)
                lines_in_files = remove_string(lines_in_files)
                words = lines_in_files.split()
                all_words[search_file] = words
                count = 0
                for key, value in all_words.items ():
                    # count = 0
                    for search_value in value:
                        if search_value.lower() != word.lower():
                            count += 0

                        else:
                            count += 1
                            # print(count)
                            count_word[search_file] = count
        return count_word




finder2 = WordsFinder('test_file.txt')

print(finder2.file_names_tuple)
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder1.file_names_tuple)
print(finder1.get_all_words()) # Все слова
print(finder1.find('captain')) # 3 слово по счёту
print(finder1.count('captain')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))





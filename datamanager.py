import csv
from typing import List, Tuple


class DataManager:
    def __init__(self, name: str):
        self.name = name
        self.data = ''
        self.css_data = ''
        self.storage = f'{name}_table'
        self.carrier = f'{name}.txt'
        self.num_line = 0

    def __str__(self) -> str:
        '''site where from is data
           (not link, just name)'''
        return self.name

    def _data_unpacker(self) -> None:
        with open(self.carrier, "r+") as file:
            self.css_data = file.readline()
            file.truncate(0)  # !this need fix "kinda"

    def _data_check(self) -> bool:
        all_news = self.list_news()
        print(all_news[-1])
        self.num_line = int(all_news[-1][0])
        if self.data == '':
            return False
        return all_news[-1][-1] != self.data

    def _save_csv_data(self) -> None:
        with open(self.storage, "a", newline='') as file:
            writer = csv.writer(file)
            rows = [self.num_line + 1, self.data]
            writer.writerow(rows)

    def list_news(self) -> List[str]:
        '''
        return whole history of news that were downloaded as list
        '''

        lines_csv: List[str] = []
        with open(self.storage, 'r') as file:
            read = csv.reader(file)
            lines_csv = [row for row in read]
            print(lines_csv)
            return lines_csv

    def task_manager(self) -> Tuple[bool, str]:

        '''
        task manager for DataManager object
        returns data and true if there is some news
        returns bool: True if there is new update
        and returns str: witch is actual data/message;
        '''

        self._data_unpacker()
        self.data = self.css_data

        if self._data_check():
            self._save_csv_data()
            print(f'[INFO]: there is no new updated on {self.name}')
            return (True, self.data)
        else:
            print(f'[INFO]: new update on {self.name}')
            return (False, self.data)


def main() -> None:  # these are tests
    # cunt = DataManager('cnn')
    # cunt.data = '54454'
    # if cunt._data_check():
    # cunt._save_csv_data()

    donut = DataManager('minuta')
    donut.data = '7896'
    print(donut.data)
    if donut._data_check():
        donut._save_csv_data()

    liveua = DataManager('liveua')
    liveua.data = 'prauda'
    if liveua._data_check():
        liveua._save_csv_data()
        print('finished successfully')


if __name__ == '__main__':
    main()

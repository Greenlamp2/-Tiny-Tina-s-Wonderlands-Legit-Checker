import csv


class Items:
    def __init__(self):
        self.items = {}

    def load(self, filename, type):
        with open(filename, newline='\n') as file:
            reader = csv.reader(file, delimiter=',')
            header = next(reader)
            for row in reader:
                self.add(row, type)

    def add(self, row, type):
        item = Item(row, type)
        if not self.items.get(item.balance, None):
            self.items[item.balance] = []
        self.items[item.balance].append(item)

    def get_parts(self, balance):
        ret = {}
        for elm in self.items.get(balance, []):
            if not ret.get(elm.category, None):
                ret[elm.category] = []
            ret[elm.category].append(elm)
        return ret

    def get_category(self, item, part):
        for elm in self.items.get(item.balance_short, []):
            if elm.parts == part:
                return elm.category

    def is_in_category(self, item, part, category):
        all_parts = self.get_parts(item.balance_short)
        parts = all_parts.get(category, [])
        for elm in parts:
            if elm.parts == part:
                return True
        return False

    def get_min_max(self, item, category):
        all_parts = self.get_parts(item.balance_short)
        part = all_parts[category][0]
        return part.min_parts, part.max_parts

    def is_legit(self, item):
        item_parts = item.parts
        counts = {}
        parts_list = []
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            cat = self.get_category(item, part_name)
            good = self.is_in_category(item, part_name, cat)
            if good:
                if not counts.get(cat, None):
                    counts[cat] = 0
                counts[cat] = counts[cat] + 1
            parts_list.append(part_name)

        for key, value in counts.items():
            min, max = self.get_min_max(item, key)
            if value < min:
                print("{} for {} should be {} min but there is only {}".format(key, item.balance_short, min, value))
                return False
            if value > max:
                print("{} for {} should be {} max but there is {}".format(key, item.balance_short, max, value))
                return False

        if self.has_excluders(item.balance_short, parts_list):
            return False
        if not self.has_dependant(item.balance_short, parts_list):
            return False

        print("{} is legit".format(item.balance_short))
        return True

    def get_excluders(self, balance, target):
        parts = self.items[balance]
        for part in parts:
            if part.parts == target:
                return part.excluders
        return []

    def get_dependant(self, balance, target):
        parts = self.items[balance]
        for part in parts:
            if part.parts == target:
                return part.dependencies
        return []

    def has_excluders(self, balance, parts_target):
        for part in parts_target:
            excluders = self.get_excluders(balance, part)
            for partB in parts_target:
                if partB in excluders:
                    print('{} is a part excluded by {}'.format(partB, part))
                    return True
        return False

    def has_dependant(self, balance, parts_target):
        for part in parts_target:
            dependant = self.get_dependant(balance, part)
            if len(dependant) == 0:
                continue

            dep = False
            for partB in parts_target:
                if partB in dependant:
                    dep = True
                    break
            if not dep:
                print('{} is missing a depencies in {}'.format(part, ', '.join(dependant)))
                return False
        return True



class Item:
    def __init__(self, row, type):
        if type == "GUNS":
            self.manufacturer = row[0]
            self.gun_type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == "SHIELDS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        elif type == "PAULDRONS":
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        elif type == 'SPELLS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'RINGS':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'MELEE':
            self.name = row[0]
            self.type = row[1]
            self.rarity = row[2]
            self.balance = row[3].split('\\')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        else:
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance = row[2].split('\\')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []



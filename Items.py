import csv
import random

from ttw_save_editor import datalib
from ttw_save_editor.datalib import BL3Serial


class Items:
    def __init__(self):
        self.items = {}
        self.passive_skils = {
            "Rogue": {
                "Part_P_PassiveSkill_Rogue_01": 3,
                "Part_P_PassiveSkill_Rogue_02": 5,
                "Part_P_PassiveSkill_Rogue_03": 1,
                "Part_P_PassiveSkill_Rogue_04": 3,
                "Part_P_PassiveSkill_Rogue_05": 5,
                "Part_P_PassiveSkill_Rogue_06": 5,
                "Part_P_PassiveSkill_Rogue_07": 5,
                "Part_P_PassiveSkill_Rogue_08": 1,
                "Part_P_PassiveSkill_Rogue_10": 3,
                "Part_P_PassiveSkill_Rogue_12": 3,
                "Part_P_PassiveSkill_Rogue_13": 1,
                "Part_P_PassiveSkill_Rogue_14": 5,
                "Part_P_PassiveSkill_Rogue_15": 3,
                "Part_P_PassiveSkill_Rogue_17": 1,
            },
            "GunMage": {
                "Part_P_PassiveSkill_GunMage_01": 5,
                "Part_P_PassiveSkill_GunMage_02": 1,
                "Part_P_PassiveSkill_GunMage_08": 3,
                "Part_P_PassiveSkill_GunMage_09": 5,
                "Part_P_PassiveSkill_GunMage_13": 5,
                "Part_P_PassiveSkill_GunMage_14": 5,
                "Part_P_PassiveSkill_GunMage_15": 1,
                "Part_P_PassiveSkill_GunMage_16": 5,
                "Part_P_PassiveSkill_GunMage_17": 1,
                "Part_P_PassiveSkill_GunMage_18": 5,
                "Part_P_PassiveSkill_GunMage_19": 1,
                "Part_P_PassiveSkill_GunMage_20": 1,
                "Part_P_PassiveSkill_GunMage_21": 3,
            },
            "Necromancer": {
                "Part_P_PassiveSkill_Necromancer_01": 5,
                "Part_P_PassiveSkill_Necromancer_02": 5,
                "Part_P_PassiveSkill_Necromancer_03": 3,
                "Part_P_PassiveSkill_Necromancer_04": 3,
                "Part_P_PassiveSkill_Necromancer_05": 5,
                "Part_P_PassiveSkill_Necromancer_06": 1,
                "Part_P_PassiveSkill_Necromancer_08": 3,
                "Part_P_PassiveSkill_Necromancer_09": 1,
                "Part_P_PassiveSkill_Necromancer_10": 1,
                "Part_P_PassiveSkill_Necromancer_12": 5,
                "Part_P_PassiveSkill_Necromancer_13": 3,
                "Part_P_PassiveSkill_Necromancer_14": 5,
                "Part_P_PassiveSkill_Necromancer_15": 3,
                "Part_P_PassiveSkill_Necromancer_17": 1,
            },
            "Barbarian": {
                "Part_P_PassiveSkill_Barbarian_01": 5,
                "Part_P_PassiveSkill_Barbarian_02": 5,
                "Part_P_PassiveSkill_Barbarian_03": 3,
                "Part_P_PassiveSkill_Barbarian_04": 3,
                "Part_P_PassiveSkill_Barbarian_05": 5,
                "Part_P_PassiveSkill_Barbarian_06": 3,
                "Part_P_PassiveSkill_Barbarian_07": 3,
                "Part_P_PassiveSkill_Barbarian_08": 1,
                "Part_P_PassiveSkill_Barbarian_09": 3,
                "Part_P_PassiveSkill_Barbarian_11": 1,
                "Part_P_PassiveSkill_Barbarian_13": 5,
                "Part_P_PassiveSkill_Barbarian_14": 5,
                "Part_P_PassiveSkill_Barbarian_15": 1,
                "Part_P_PassiveSkill_Barbarian_17": 1,
            },
            "Ranger": {
                "Part_P_PassiveSkill_Ranger_01": 5,
                "Part_P_PassiveSkill_Ranger_02": 5,
                "Part_P_PassiveSkill_Ranger_03": 5,
                "Part_P_PassiveSkill_Ranger_04": 3,
                "Part_P_PassiveSkill_Ranger_05": 1,
                "Part_P_PassiveSkill_Ranger_06": 5,
                "Part_P_PassiveSkill_Ranger_07": 1,
                "Part_P_PassiveSkill_Ranger_09": 3,
                "Part_P_PassiveSkill_Ranger_10": 5,
                "Part_P_PassiveSkill_Ranger_11": 1,
                "Part_P_PassiveSkill_Ranger_13": 3,
                "Part_P_PassiveSkill_Ranger_14": 3,
                "Part_P_PassiveSkill_Ranger_15": 3,
                "Part_P_PassiveSkill_Ranger_17": 1,
            },
            "Knight": {
                "Part_P_PassiveSkill_Knight_03": 99,
                "Part_P_PassiveSkill_Knight_04": 99,
                "Part_P_PassiveSkill_Knight_14": 99,
                "Part_P_PassiveSkill_Knight_15": 99,
                "Part_P_PassiveSkill_Knight_19": 99,
                "Part_P_PassiveSkill_Knight_21": 99,
                "Part_P_PassiveSkill_Knight_22": 99,
                "Part_P_PassiveSkill_Knight_24": 99,
                "Part_P_PassiveSkill_Knight_25": 99,
                "Part_P_PassiveSkill_Knight_27": 99,
                "Part_P_PassiveSkill_Knight_28": 99,
                "Part_P_PassiveSkill_Knight_29": 99,
                "Part_P_PassiveSkill_Knight_30": 99,
            }
        }

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

    def get_category(self, balance_short, part):
        parts = self.items.get(balance_short, [])
        for index, elm in enumerate(parts):
            if elm.parts:
                part_name = elm.parts.replace('\\', '/').split('/')[-1]
                if part_name == part:
                    return elm.category
        return None

    def is_in_category(self, item, part, category):
        all_parts = self.get_parts(item.balance_short)
        parts = all_parts.get(category, [])
        for elm in parts:
            if elm.parts and elm.parts.replace('\\', '/').split('/')[-1] == part:
                return True
        return False

    def get_min_max(self, item, category):
        all_parts = self.get_parts(item.balance_short)
        to_sub = 0
        for elm in all_parts[category]:
            if not elm.parts:
                to_sub += 1
        part = all_parts[category][0]
        return part.min_parts-to_sub, part.max_parts

    def get_random_type(self):
        item_types = [
            (0, 58.14),
            (1, 23.26),
            (2, 17.44),
            (3, 1.16),
        ]
        pool = []
        for key, percent in item_types:
            occurence = int(percent * 100)
            for i in range(0, occurence):
                pool.append(key)

        n = random.randint(0, len(pool) - 1)
        return pool[n]

    def check_excluders(self, new_part, prev):
        whatihave = {}
        whatifear = {}
        for elm in prev:
            if elm.category not in whatihave:
                whatihave[elm.category] = []
            whatihave[elm.category].append(elm.parts)
        for elm in new_part.excluders:
            cat = self.get_category(new_part.balance, elm.replace('\\', '/').split('/')[-1])
            if cat not in whatifear:
                whatifear[cat] = []
            whatifear[cat].append(elm)

        for part in prev:
            for elm in part.excluders:
                cat = self.get_category(part.balance, elm.replace('\\', '/').split('/')[-1])
                if not cat:
                    rare = True
                    continue
                if cat not in whatifear:
                    whatifear[cat] = []
                if elm not in whatifear[cat]:
                    whatifear[cat].append(elm)

        multiple = ["MINOR STAT", "PASSIVE SKILL PARTS", "PLAYER STAT", "SPELL ENHANCEMENT", "AUGMENT"]
        if new_part.category in whatihave:
            if new_part.category not in multiple:
                if new_part.category not in whatifear:
                    whatifear[new_part.category] = [new_part.parts]
                else:
                    whatifear[new_part.category].append(new_part.parts)
        else:
            whatihave[new_part.category] = [new_part.parts]

        # return True if one value of whatihave is in whatineed for each key
        for key, value in whatifear.items():
            if key not in whatihave:
                continue
            not_found = True
            for elm in value:
                if elm in whatihave[key]:
                    not_found = False
                    break
            if not not_found:
                return False
        return True

    def check_included(self, new_part, prev):
        whatihave = {}
        rare = False
        for elm in prev:
            if elm.category not in whatihave:
                whatihave[elm.category] = []
            whatihave[elm.category].append(elm.parts)

        # for each parts, check if i got everything i need
        whatineed = {}
        for elm in new_part.dependencies:
            part_name = elm.replace('\\', '/').split('/')[-1]
            cat = self.get_category(new_part.balance, part_name)
            if not cat:
                rare = True
                continue
            if cat not in whatineed:
                whatineed[cat] = []
            whatineed[cat].append(elm)

        # return True if one value of whatihave is in whatineed for each key
        if len(whatineed.keys()) == 0 and rare:
            return False
        for cat, values in whatineed.items():
            if cat not in whatihave:
                return False
            to_check = whatihave[cat]
            found = False
            for value in values:
                if value in to_check:
                    found = True
                    break
            if not found:
                return False
        return True

    def check_amount(self, new_part, prev):
        parts_multiples = {}
        for elm in prev:
            multiple = ["MINOR STAT", "PASSIVE SKILL PARTS", "PLAYER STAT", "SPELL ENHANCEMENT", "AUGMENT"]
            if elm.category in multiple:
                if elm.category not in parts_multiples:
                    parts_multiples[elm.category] = []
                parts_multiples[elm.category].append(elm.parts)
        # check passive skill amount
        detail = {}
        if "PASSIVE SKILL PARTS" in parts_multiples:
            parts = parts_multiples["PASSIVE SKILL PARTS"]
            for part in parts:
                part_name = part.replace('\\', '/').split(".")[-1]
                character = part_name.split("PassiveSkill_")[1].split("_")[0]
                part_name_short = part_name.split("/")[-1]
                if character not in detail:
                    detail[character] = {}
                if part_name_short not in detail[character]:
                    detail[character][part_name_short] = 0
                detail[character][part_name_short] += 1
            for character, values in detail.items():
                to_check = self.passive_skils[character]
                for skill_name, value in values.items():
                    if value > to_check[skill_name]:
                        return False

        if "MINOR STAT" in parts_multiples:
            detail = {}
            parts = parts_multiples["MINOR STAT"]
            for part in parts:
                part_name = part.replace('\\', '/').split(".")[-1]
                part_name_short = part_name.split("/")[-1]
                if part_name_short not in detail:
                    detail[part_name_short] = 0
                detail[part_name_short] += 1
            for part_elm, value in detail.items():
                if value > 3:
                    return False
        return True

    def get_random_min_max(self, parts, min, max, prev=[], seed=None):
        def sort_fn(elm):
            return elm.parts
        if seed:
            random.seed(seed)
        ret = []
        pool = []
        for part in parts:
            if not part.parts:
                continue
            occurence = int((1.0 * part.weight) * 100)
            for i in range(0, occurence):
                pool.append(part)
        random.shuffle(pool)

        m = random.randint(min, max)
        if m == 0:
            return ret
        while len(ret) < m:
            if len(pool) == 0:
                return ret
            n = random.randint(0, len(pool) - 1)
            target = pool[n]
            if self.check_excluders(target, prev+ret) and self.check_included(target, prev+ret) and self.check_amount(target, prev+ret):
                ret.append(target)
                # print(target.parts)
            else:
                pool.sort(key=sort_fn)
                new_pool = [elm for elm in pool if elm.parts != target.parts]
                pool = new_pool
                random.shuffle(pool)
        return ret

    def get_legit_random_parts(self, item, seed=None):
        new_item_parts = []
        all_parts = self.get_parts(item.balance_short)
        for type, parts in all_parts.items():
            min, max = parts[0].min_parts, parts[0].max_parts
            res = self.get_random_min_max(parts, min, max, new_item_parts, seed)
            new_item_parts += res
        return new_item_parts

    def reverse_item_serial(self, serial_number):
        c = BL3Serial.decode_serial_base64(serial_number)
        datawrapper = datalib.DataWrapper()
        return datalib.BL3Serial(c, datawrapper)

    def get_serial_string(self, item):
        return item.get_serial_base64()

    def generate_random(self, original_item, seed=None):
        serial = original_item.get_serial_base64()
        item = self.reverse_item_serial(serial)
        legit = False
        while not legit:
            new_parts = self.get_legit_random_parts(item, seed)
            item.set_parts(new_parts)
            item_type = self.get_random_type()
            item.set_item_type(item_type)
            if self.is_legit(item):
                legit = True
            else:
                print(item.get_serial_base64())
                print("was not legit, generating another one, please wait.")
        return item

    def is_legit(self, item, silent=False):
        all_parts = self.get_parts(item.balance_short)
        item_parts = item.parts
        counts = {}
        parts_list_long = []
        cats = []
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            parts_list_long.append(part)
            cat = self.get_category(item.balance_short, part_name)
            if cat not in cats:
                cats.append(cat)
            if not cat:
                if not silent:
                    print("{} for {} is not a possible part".format(part_name, item.balance_short, cat))
                return False
            good = self.is_in_category(item, part_name, cat)
            if good:
                if not counts.get(cat, None):
                    counts[cat] = 0
                counts[cat] = counts[cat] + 1
            else:
                if not silent:
                    print("{} for {} is not a possible part as {}".format(part_name, item.balance_short, cat))
                return False

        # cats = [item for item in list(all_parts.keys()) if item not in cats]
        # for key in cats:
        #     min = all_parts[key][0].min_parts
        #     if min > 0:
        #         if not silent:
        #             print("{} for {} should be {} min but there is none".format(key, item.balance_short, min))
        #         return False

        for key, value in counts.items():
            min, max = self.get_min_max(item, key)
            if value < min:
                if not silent:
                    print("{} for {} should be {} min but there is only {}".format(key, item.balance_short, min, value))
                return False
            if value > max:
                if not silent:
                    print("{} for {} should be {} max but there is {}".format(key, item.balance_short, max, value))
                return False

        if self.has_excluders(item.balance_short, parts_list_long):
            return False
        if self.missing_dependant(item.balance_short, parts_list_long):
            return False
        if self.wrong_amount(item.balance_short, parts_list_long):
            return False

        if not silent:
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

    def has_wrong_clusters(self, balance, parts_target, silent=False):
        for part in parts_target:
            if "/PlayerStat/" not in part:
                continue
            for part2 in parts_target:
                if "/PlayerStat/" not in part2 or part == part2:
                    continue
                part_name = part.split("PlayerStat_")[1].split("_")[0]
                part2_name = part2.split("PlayerStat_")[1].split("_")[0]
                cluster = self.clusters[part_name]
                if part2_name in cluster:
                    if not silent:
                        print('{} is a passive stat in the same cluster as {}'.format(part_name, part2_name))
                    return False

    def wrong_amount(self, balance, parts_target):
        parts_multiples = {}
        for part in parts_target:
            part_name = part.replace('\\', '/')
            cat = self.get_category(balance, part_name.split(".")[-1])
            multiple = ["MINOR", "PASSIVE SKILL PARTS", "PLAYER STAT"]
            if cat in multiple:
                if cat not in parts_multiples:
                    parts_multiples[cat] = []
                parts_multiples[cat].append(part)
        # check passive skill amount
        detail = {}
        if "PASSIVE SKILL PARTS" in parts_multiples:
            parts = parts_multiples["PASSIVE SKILL PARTS"]
            for part in parts:
                part_name = part.replace('\\', '/').split(".")[-1]
                character = part_name.split("PassiveSkill_")[1].split("_")[0]
                if character not in detail:
                    detail[character] = {}
                if part_name not in detail[character]:
                    detail[character][part_name] = 0
                detail[character][part_name] += 1
            for character, values in detail.items():
                to_check = self.passive_skils[character]
                for skill_name, value in values.items():
                    if value > to_check[skill_name]:
                        print("{} part is limited to {} but there is {} for {}".format(skill_name, to_check[skill_name], value, balance))
                        return True

        if "MINOR" in parts_multiples:
            detail = {}
            parts = parts_multiples["MINOR"]
            for part in parts:
                part_name = part.replace('\\', '/').split(".")[-1]
                if part_name not in detail:
                    detail[part_name] = 0
                detail[part_name] += 1
            for part_elm, value in detail.items():
                if value > 3:
                    print("{} part is limited to 3 but there is {} for {}".format(skill_name, value, balance))
                    return True
        return False

    def missing_dependant(self, balance, parts_target):
        whatihave = {}

        for part in parts_target:
            part_name = part.replace('\\', '/')
            cat = self.get_category(balance, part_name.split(".")[-1])
            if cat not in whatihave:
                whatihave[cat] = []
            whatihave[cat].append(part.split(".")[0])

        # for each parts, check if i got everything i need
        for part in parts_target:
            part_name = part.replace('\\', '/')
            dependencies = self.get_dependant(balance, part_name.split(".")[0])
            whatineed = {}
            rare = False
            for elm in dependencies:
                cat = self.get_category(balance, elm.replace('\\', '/').split('/')[-1])
                if not cat:
                    rare = True
                    continue
                if cat not in whatihave:
                    print("Missing {} parts needed for {}".format(cat, balance))
                    return True
                if cat not in whatineed:
                    whatineed[cat] = []
                whatineed[cat].append(elm)

            if len(whatineed.keys()) == 0 and rare:
                return True
            for cat, values in whatineed.items():
                if cat not in whatihave:
                    return True
                to_check = whatihave[cat]
                found = False
                for value in values:
                    if value in to_check:
                        found = True
                        break
                if not found:
                    print("Missing {} for {} on {}".format(value, part, cat))
                    return True
        return False

    def has_excluders(self, balance, parts_target):
        whatihave = {}
        whatifear = {}
        for part in parts_target:
            part_name = part.replace('\\', '/')
            cat = self.get_category(balance, part_name.split(".")[-1])
            if cat not in whatihave:
                whatihave[cat] = []
            whatihave[cat].append(part.split(".")[0])
            excluders = self.get_excluders(balance, part_name.split(".")[0])
            for elm in excluders:
                cat = self.get_category(balance, elm.replace('\\', '/').split('/')[-1])
                if not cat:
                    continue
                if cat not in whatifear:
                    whatifear[cat] = []
                whatifear[cat].append(elm.split(".")[-1])

        for key, value in whatifear.items():
            if key not in whatihave:
                continue
            not_found = True
            for elm in value:
                if elm in whatihave[key]:
                    not_found = False
                    print("{} is in conflict as {}".format(elm, key))
                    break
            if not not_found:
                return True
        return False

class Item:
    def __init__(self, row, type):
        if type == "GUNS":
            self.manufacturer = row[0]
            self.gun_type = row[1]
            self.rarity = row[2]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
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
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
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
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
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
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
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
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
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
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[4]
            self.min_parts = int(row[5])
            self.max_parts = int(row[6])
            self.weight = float(row[7])
            self.parts = row[8] if row[8] != "None" else None
            self.dependencies = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
            self.excluders = [e.strip() for e in row[10].split(',')] if row[10] != "" else []
        elif type == 'AMULETS':
            self.name = row[0]
            self.rarity = row[1]
            self.balance_long = row[2]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []
        else:
            self.manufacturer = row[0]
            self.rarity = row[1]
            self.balance_long = row[3]
            self.balance = self.balance_long.replace('\\', '/').split('/')[-1]
            self.category = row[3]
            self.min_parts = int(row[4])
            self.max_parts = int(row[5])
            self.weight = float(row[6])
            self.parts = row[7] if row[7] != "None" else None
            self.dependencies = [e.strip() for e in row[8].split(',')] if row[8] != "" else []
            self.excluders = [e.strip() for e in row[9].split(',')] if row[9] != "" else []

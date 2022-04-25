import csv
import random

from ttw_save_editor import datalib
from ttw_save_editor.datalib import BL3Serial


class Items:
    def __init__(self):
        self.items = {}
        self.clusters_raw = [
            [
                "MoveSpeed",
                "CompanionCritChance",
                "SkillCritChance",
            ], [
                "WardMax",
                "WardDelay",
                "WardRegenRate",
                "HealthMax",
                "HealthRegen",
            ], [
                "AllDamage",
                "SkillDamage",
            ], [
                "GunCritChance",
                "SpellCritChance",
                "MeleeCritChance",
            ], [
                "GunDamage",
                "SpellDamage",
                "MeleeDamage",
            ], [
                "CompanionDamage",
                "SplashDamage",
                "FireRate",
            ]
        ]
        self.passives_raw = {
            "Graveborn": {
                "Mortal Vessel": "Passive_01",
                "Dark Pact": "Passive_02",
                "Faithful Thralls": "Passive_03",
                "Sanguine Sacrament": "Passive_04",
                "Essence Drain": "Passive_05",
                "Punishment": "Passive_06",
                "Dark Hydra": "Passive_08",
                "Dread Covenant": "Passive_09",
                "Lord of Edges": "Passive_10",
                "Blast Gasp": "Passive_12",
                "Ascension": "Passive_13",
                "Stain of the Soul": "Passive_14",
                "Harvest": "Passive_15",
                "Morhaim's Blessing": "Passive_17",
            },
            "Barbarian": {
                "Ancestral Frost": "Passive_01",
                "Savagery": "Passive_02",
                "Unyielding": "Passive_03",
                "Ice Breaker": "Passive_04",
                "The Old Ways": "Passive_05",
                "Instinct": "Passive_06",
                "Cold Snap": "Passive_07",
                "Unarmored Defense": "Passive_08",
                "Blood Frenzy": "Passive_09",
                "Blood of the Fallen": "Passive_11",
                "Iron Squall": "Passive_13",
                "Ancient Fury": "Passive_14",
                "Relentless Rage": "Passive_15",
                "Blast Chill": "Passive_17",
            },
            "Ranger": {
                "Bounty of the Hunt": "Passive_01",
                "Kindred Heart": "Passive_02",
                "Eagle Eye": "Passive_03",
                "Quiver of Holding": "Passive_04",
                "Headhunter": "Passive_05",
                "Bullseye": "Passive_06",
                "Medicinal Mushroom": "Passive_07",
                "Windrunner": "Passive_09",
                "Affinity": "Passive_10",
                "Spore Cloud": "Passive_11",
                "Wrath of Nature": "Passive_13",
                "Thrill of the Hunt": "Passive_14",
                "Called Shot": "Passive_15",
                "Play the Angles": "Passive_17",
            },
            "Clawbringer": {
                "Oath of Fire": "Passive_03",
                "Friend to Flame": "Passive_04",
                "Radiance": "Passive_14",
                "Dedication": "Passive_15",
                "Oath of Thunder": "Passive_19",
                "Storm Smite": "Passive_21",
                "Rebuke": "Passive_22",
                "Blasthamut's Favor": "Passive_24",
                "Dragon Aura": "Passive_25",
                "Awe": "Passive_27",
                "Indomitable": "Passive_28",
                "Fire Bolt": "Passive_29",
                "Storm Breath": "Passive_30",
            }
        }
        self.can_roll = {
            "Barbarian": [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            "Clawbringer": [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            "Graveborn": [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            "Spellshot": [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            "Ranger": [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            "Rogue": [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        }
        self.combos_raw = {
            "Barbarian": {
                "Clawbringer": ["Savagery", "Blast Chill", "Dragon Aura"],
                "Graveborn": ["Ancient Fury", "Unyielding", "Blast Gasp"],
                "Spellshot": ["Ancestral Frost", "Ice Breaker", "Imbued Weapon"],
                "Ranger": ["Ice Breaker", "Cold Snap", "Affinity"],
                "Rogue": ["Iron Squall", "The Old Ways", "Follow Up"],
            },
            "Clawbringer": {
                "Barbarian": ["Rebuke", "Oath of Thunder", "Iron Squall"],
                "Graveborn": ["Friend to Flame", "Oath of Fire", "Harvest"],
                "Spellshot": ["Radiance", "Dedication", "Mage Armor"],
                "Ranger": ["Blasthamut's Favor", "Oath of Fire", "Called Shot"],
                "Rogue": ["Awe", "Oah of Thunder", "Nimble Fingers"],
            },
            "Graveborn": {
                "Barbarian": ["Mortal Vessel", "Ascension", "Blood Frenzy"],
                "Clawbringer": ["Essence Drain", "Blast Gasp", "Dragon Aura"],
                "Spellshot": ["Essence Drain", "Ascension", "War Caster"],
                "Ranger": ["Faithful Thralls", "Dark Hydra", "Thrill of the Hunt"],
                "Rogue": ["Dark Pact", "Stain of the Soul", "Contagion"],
            },
            "Spellshot": {
                "Barbarian": ["Just Warming Up", "High Thread Count", "Instinct"],
                "Clawbringer": ["Just Warming Up", "Font of Mana", "Awe"],
                "Graveborn": ["Spell Sniper", "Font of Mana", "Stain of the Soul"],
                "Ranger": ["High Thread Count", "Prestidigitation", "Windrunner"],
                "Rogue": ["Spell Sniper", "Double Knot", "A Thousand Cuts"],
            },
            "Ranger": {
                "Barbarian": ["Bounty of the Hunt", "Wrath of Nature", "Iron Squall"],
                "Clawbringer": ["Kindred Heart", "Bullseye", "Friend to Flame"],
                "Graveborn": ["Kindred Heart", "Windrunner", "Harvest"],
                "Spellshot": ["Called Shot", "Eagle Eye", "Imbued Weapon"],
                "Rogue": ["Bullseye", "Eagle Eye", "A Thousand Cuts"],
            },
            "Rogue": {
                "Barbarian": ["Haste", "Swift Death", "Cold Snap"],
                "Clawbringer": ["Exploit Their Weakness", "Potent Poisons", "Dragon Aura"],
                "Graveborn": ["Arsenal", "Sneak Attack", "Lord of Edges"],
                "Spellshot": ["Nimble Fingers", "Arsenal", "Magic Bullets"],
                "Ranger": ["Swift Death", "Follow Up", "Windrunner"],
            },
        }
        self.clusters = {}
        self.compute_clusters()

    def compute_clusters(self):
        for cluster in self.clusters_raw:
            for elm in cluster:
                for elm2 in cluster:
                    if elm == elm2:
                        continue
                    if elm not in self.clusters:
                        self.clusters[elm] = []
                    self.clusters[elm].append(elm2)

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
        parts = self.items.get(item.balance_short, [])
        for elm in parts:
            if elm.parts and elm.parts.replace('\\', '/').split('/')[-1] == part:
                return elm.category

    def is_in_category(self, item, part, category):
        all_parts = self.get_parts(item.balance_short)
        parts = all_parts.get(category, [])
        for elm in parts:
            if elm.parts and elm.parts.replace('\\', '/').split('/')[-1] == part:
                return True
        return False

    def get_min_max(self, item, category):
        all_parts = self.get_parts(item.balance_short)
        part = all_parts[category][0]
        return part.min_parts, part.max_parts

    def get_random_part(self, part_list):
        pool = []
        for part in part_list:
            if not part.parts:
                continue
            occurence = int(1.0 * part.weight * 100)
            for i in range(0, occurence):
                pool.append(part)
        n = random.randint(0, len(pool) - 1)
        return pool[n]

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

    def get_legit_random_parts(self, item):
        item_parts = item.parts
        new_item_parts = []
        all_parts = self.get_parts(item.balance_short)
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            category = self.get_category(item, part_name)
            possible_parts = all_parts[category]
            new_part = self.get_random_part(possible_parts)
            new_item_parts.append(new_part)
        return new_item_parts

    def reverse_item_serial(self, serial_number):
        c = BL3Serial.decode_serial_base64(serial_number)
        datawrapper = datalib.DataWrapper()
        return datalib.BL3Serial(c, datawrapper)

    def get_serial_string(self, item):
        return item.get_serial_base64()

    def generate_random(self, item):
        original_item = self.reverse_item_serial(item.get_serial_base64())
        legit = False
        while not legit:
            new_parts = self.get_legit_random_parts(original_item)
            item.set_parts(new_parts)
            item_type = self.get_random_type()
            item.set_item_type(item_type)
            if self.is_legit(item, silent=True):
                legit = True
        return item

    def is_legit(self, item, silent=False):
        item_parts = item.parts
        counts = {}
        parts_list = []
        parts_list_long = []
        for part, id in item_parts:
            part_name = part.split('.')[-1]
            parts_list_long.append(part)
            cat = self.get_category(item, part_name)
            good = self.is_in_category(item, part_name, cat)
            if good:
                if not counts.get(cat, None):
                    counts[cat] = 0
                counts[cat] = counts[cat] + 1
            else:
                if not silent:
                    print("{} for {} is not a possible part".format(part_name, item.balance_short))
                return False
            if part_name in parts_list \
                    and "Minor" not in part_name \
                    and "_Enh_" not in part_name \
                    and "_PassiveSkill_" not in part_name:
                if not silent:
                    print("{} for {} is present more than once".format(part_name, item.balance_short))
                return False
            parts_list.append(part_name)

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

        if self.has_excluders(item.balance_short, parts_list):
            return False
        if not self.has_dependant(item.balance_short, parts_list):
            return False

        if self.has_wrong_clusters(parts_list_long):
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

    def has_wrong_clusters(self, parts_target):
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
                    print('{} is a parssive stat in the same cluster as{}'.format(part_name, part2_name))
                    return False

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

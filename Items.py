import csv
import random

from ttw_save_editor import datalib
from ttw_save_editor.datalib import BL3Serial


class Items:
    def __init__(self):
        self.items = {}
        self.clusters = {}
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
            "Rogue": {
                "Follow Up": "Passive_01",
                "Sneak Attack": "Passive_02",
                "Alchemical Agent": "Passive_03",
                "Nimble Finger": "Passive_04",
                "Swift Death": "Passive_05",
                "Potent Poisons": "Passive_06",
                "Arsenal": "Passive_07",
                "Shadow Step": "Passive_08",
                "Haste": "Passive_10",
                "Contagion": "Passive_12",
                "Elusive": "Passive_13",
                "A Thousand Cuts": "Passive_14",
                "Exploit Weakness": "Passive_15",
                "Executioner's Blade": "Passive_17",
            },
            "GunMage": {
                "Font of Mana": "Passive_01",
                "Glass Cannon": "Passive_02",
                "Double Knot": "Passive_08",
                "Spell Sniper": "Passive_09",
                "Imbued Weapon": "Passive_13",
                "Prestidigitation": "Passive_14",
                "Sever the Thread": "Passive_15",
                "Just Warming Up": "Passive_16",
                "High Thread Count": "Passive_17",
                "War Caster": "Passive_18",
                "One Slot, One Kill": "Passive_19",
                "Mage Armor": "Passive_20",
                "Magic Bullets": "Passive_21",
            },
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
            "Necromancer": {
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
        self.combos = {}
        self.combos_raw = {
            "Barbarian": {
                "Necromancer": ["Savagery", "Blast Chill", "Dragon Aura"],
                "Graveborn": ["Ancient Fury", "Unyielding", "Blast Gasp"],
                "GunMage": ["Ancestral Frost", "Ice Breaker", "Imbued Weapon"],
                "Ranger": ["Ice Breaker", "Cold Snap", "Affinity"],
                "Rogue": ["Iron Squall", "The Old Ways", "Follow Up"],
            },
            "Necromancer": {
                "Barbarian": ["Rebuke", "Oath of Thunder", "Iron Squall"],
                "Graveborn": ["Friend to Flame", "Oath of Fire", "Harvest"],
                "GunMage": ["Radiance", "Dedication", "Mage Armor"],
                "Ranger": ["Blasthamut's Favor", "Oath of Fire", "Called Shot"],
                "Rogue": ["Awe", "Oath of Thunder", "Nimble Finger"],
            },
            "Graveborn": {
                "Barbarian": ["Mortal Vessel", "Ascension", "Blood Frenzy"],
                "Necromancer": ["Essence Drain", "Blast Gasp", "Dragon Aura"],
                "GunMage": ["Essence Drain", "Ascension", "War Caster"],
                "Ranger": ["Faithful Thralls", "Dark Hydra", "Thrill of the Hunt"],
                "Rogue": ["Dark Pact", "Stain of the Soul", "Contagion"],
            },
            "GunMage": {
                "Barbarian": ["Just Warming Up", "High Thread Count", "Instinct"],
                "Necromancer": ["Just Warming Up", "Font of Mana", "Awe"],
                "Graveborn": ["Spell Sniper", "Font of Mana", "Stain of the Soul"],
                "Ranger": ["High Thread Count", "Prestidigitation", "Windrunner"],
                "Rogue": ["Spell Sniper", "Double Knot", "A Thousand Cuts"],
            },
            "Ranger": {
                "Barbarian": ["Bounty of the Hunt", "Wrath of Nature", "Iron Squall"],
                "Necromancer": ["Kindred Heart", "Bullseye", "Friend to Flame"],
                "Graveborn": ["Kindred Heart", "Windrunner", "Harvest"],
                "GunMage": ["Called Shot", "Eagle Eye", "Imbued Weapon"],
                "Rogue": ["Bullseye", "Eagle Eye", "A Thousand Cuts"],
            },
            "Rogue": {
                "Barbarian": ["Haste", "Swift Death", "Cold Snap"],
                "Necromancer": ["Exploit Weakness", "Potent Poisons", "Dragon Aura"],
                "Graveborn": ["Arsenal", "Sneak Attack", "Lord of Edges"],
                "GunMage": ["Nimble Finger", "Arsenal", "Magic Bullets"],
                "Ranger": ["Swift Death", "Follow Up", "Windrunner"],
            },
        }
        self.can_roll = {
            "Rogue": [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
            "GunMage": [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            "Graveborn": [1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
            "Barbarian": [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
            "Ranger": [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            "Necromancer": [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        }
        self.levels = {
            "Rogue": [3, 5, 1, 3, 5, 5, 5, 1, 3, 3, 1, 5, 3, 1],
            "GunMage": [5, 1, 3, 5, 5, 5, 1, 5, 1, 5, 1, 1, 3],
            "Graveborn": [5, 5, 3, 3, 5, 1, 3, 1, 1, 5, 3, 5, 3, 1],
            "Barbarian": [5, 5, 3, 3, 5, 3, 3, 1, 3, 1, 5, 5, 1, 1],
            "Ranger": [5, 5, 5, 3, 1, 5, 1, 3, 5, 1, 3, 3, 3, 1],
            "Necromancer": [],
        }
        self.base_weights = {
            "light": 0,
            "medium": 0,
            "heavy": 0,
        }
        self.class_weights = {
            "GunMage": "Light",
            "Ranger": "Medium",
            "Rogue": "Medium",
            "Barbarian": "Heavy",
            "Necromancer": "Medium",
        }
        self.spread = {
            "Legendary": 5,
        }

        self.compute_clusters()
        self.compute_skill_combos()

    def compute_clusters(self):
        for cluster in self.clusters_raw:
            for elm in cluster:
                for elm2 in cluster:
                    if elm == elm2:
                        continue
                    if elm not in self.clusters:
                        self.clusters[elm] = []
                    self.clusters[elm].append(elm2)

    def compute_skill_combos(self):
        self.combos = {}
        for characterA in self.combos_raw:
            for characterB in self.combos_raw[characterA]:
                skills = self.combos_raw[characterA][characterB]
                skillA = skills[0]
                skillA_key = self.passives_raw[characterA][skillA]
                skillB = skills[1]
                skillB_key = self.passives_raw[characterA][skillB]
                skillC = skills[2]
                skillC_key = self.passives_raw[characterB][skillC]
                if characterA not in self.combos:
                    self.combos[characterA] = {}
                self.combos[characterA][characterB] = [skillA_key, skillB_key, skillC_key]

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
            if part_name in parts_list \
                    and "Minor" not in part_name \
                    and "_Enh_" not in part_name \
                    and "_Aug_" not in part_name \
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

        # if self.has_wrong_clusters(item.balance_short, parts_list_long):
        #     return False
        if "/Pauldron" in item.balance:
            if self.has_wrong_pauldron_stats(item.balance_short, parts_list_long):
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

    def has_wrong_clusters(self, balance, parts_target):
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
                    print('{} is a passive stat in the same cluster as {}'.format(part_name, part2_name))
                    return False

    def has_wrong_pauldron_stats(self, balance, parts_target):
        characterA = None
        characterB = None
        weightA = None
        weightB = None
        combo = None
        unique_part = 0
        rarity = None
        count_part = 0
        skills = []
        overrides = []
        for part in parts_target:
            if "/Class/Part" in part:
                characterA = part.split("Primary_")[1].split(".")[0]
            if "/Class/Secondary/Part" in part:
                characterB = part.split("Secondary_")[1].split(".")[0]
            if "/Base/Part_" in part:
                weightA = part.split("Base_")[1].split(".")[0]
            if "/Base_Secondary/Part_" in part:
                weightB = part.split("Base_Secondary_")[1].split(".")[0]
            if "/SkillCombos/" in part:
                combo = part.split("SkillCombo_")[1].split("_0")[0]
            if "/_Uniques/" in part:
                unique_part += 1
            if "/Rarity/" in part:
                rarity = part.split("Rarity_")[-1].split("_")[-1]
            if "/SkillParts/" in part:
                count_part += 1
            if "/SkillParts/" in part:
                skill = part.split("PassiveSkill_")[1].split(".")[0]
                skills.append("{}_Passive_{}".format(skill.split("_")[0], skill.split("_")[1]))
            if "/PlayerStat/" in part:
                override = part.split("PlayerStat_")[1].split(".")[0]
                overrides.append(override.split("_")[0])
                # skills.append([skill.split("_")[0], "Passive_{}".format(skill.split("_")[1])])

        if self.class_weights[characterA] != weightA:
            print('{} should have a base part {} but got {}'.format(characterA, self.class_weights[characterA], weightA))
            return False
        if self.class_weights[characterB] != weightB:
            print('{} should have a base part {} but got {}'.format(characterB, self.class_weights[characterB], weightB))
            return False
        if combo != "{}_{}".format(characterA, characterB):
            print('skill combo should be {}_{} but is {}'.format(characterA, characterB, combo))
            return False
        if unique_part > 1:
            print("There is more than 1 unique part")
            return False
        if self.spread[rarity] != count_part:
            print('Amount of skill part should be {} but is {}'.format(self.spread[rarity], count_part))
            return False

        for part in overrides:
            for part2 in overrides:
                if part == part2:
                    continue
                cluster = self.clusters[part]
                if part2 in cluster:
                    print('{} is a passive stat in the same cluster as {}'.format(part, part2))
                    return False

        skill_counts = {}
        for skill in skills:
            t = self.combos[characterA][characterB]
            possible_skills = [
                "{}_{}".format(characterA, t[0]),
                "{}_{}".format(characterA, t[1]),
                "{}_{}".format(characterB, t[2]),
            ]
            if skill not in skill_counts:
                skill_counts[skill] = 1
            else:
                skill_counts[skill] += 1

            if skill not in possible_skills:
                print("{} should not be present with {} as primary and {} as secondary".format(skill, characterA, characterB))

        for key, value in skill_counts.items():
            character = key.split("_")[0]
            passive = "Passive_{}".format(key.split("Passive_")[1])
            index = self.get_index_passive_raw(character, passive)

            if not self.can_roll[character][index]:
                print("{} should not be present on a mod class for {}".format(key, character))

            a = self.levels[character]
            if value > self.levels[character][index]:
                print("{} can be max level {} but is {}".format(key, self.levels[character][index], value))


    def get_index_passive_raw(self, character, passive):
        for i, key in enumerate(self.passives_raw[character]):
            value = self.passives_raw[character][key]
            if value == passive:
                return i
        return None

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

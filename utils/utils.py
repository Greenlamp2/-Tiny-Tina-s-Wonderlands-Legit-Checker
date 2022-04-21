class Constants:
    @staticmethod
    def get_classes_list():
        ret = []
        for key in Constants.classes.keys():
            ret.append(key)
        return ret

    @staticmethod
    def get_class_key(class_name):
        for key, value in Constants.classes.items():
            if value == class_name:
                return key

    classes = {
         "None": "",
         "Brr-zerker": "/Game/PlayerCharacters/Barbarian/_Shared/_Design/SkillTree/AbilityTree_Branch_Barbarian.AbilityTree_Branch_Barbarian",
         "Spellshot": "/Game/PlayerCharacters/GunMage/_Shared/_Design/SkillTree/AbilityTree_Branch_GunMage.AbilityTree_Branch_GunMage",
         "Clawbringer": "/Game/PlayerCharacters/KnightOfTheClaw/_Shared/_Design/SkillTree/AbilityTree_Branch_DragonCleric.AbilityTree_Branch_DragonCleric",
         "Graveborn": "/Game/PlayerCharacters/Necromancer/_Shared/_Design/SkillTree/AbilityTree_Branch_Necromancer.AbilityTree_Branch_Necromancer",
         "Spore Warden": "/Game/PlayerCharacters/Ranger/_Shared/_Design/SkillTree/AbilityTree_Branch_Ranger.AbilityTree_Branch_Ranger",
         "Stabbomancer": "/Game/PlayerCharacters/Rogue/_Shared/_Design/SkillTree/AbilityTree_Branch_Rogue.AbilityTree_Branch_Rogue",
    }

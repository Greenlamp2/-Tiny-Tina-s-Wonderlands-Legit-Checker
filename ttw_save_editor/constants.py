
# CRC32 table used to compute weapon customization hashes in the profile.  Many
# thanks to Gibbed, yet again, for supplying this!
_weapon_cust_crc32_table = [
        0x00000000, 0x04C11DB7, 0x09823B6E, 0x0D4326D9, 0x130476DC, 0x17C56B6B, 0x1A864DB2, 0x1E475005,
        0x2608EDB8, 0x22C9F00F, 0x2F8AD6D6, 0x2B4BCB61, 0x350C9B64, 0x31CD86D3, 0x3C8EA00A, 0x384FBDBD,
        0x4C11DB70, 0x48D0C6C7, 0x4593E01E, 0x4152FDA9, 0x5F15ADAC, 0x5BD4B01B, 0x569796C2, 0x52568B75,
        0x6A1936C8, 0x6ED82B7F, 0x639B0DA6, 0x675A1011, 0x791D4014, 0x7DDC5DA3, 0x709F7B7A, 0x745E66CD,
        0x9823B6E0, 0x9CE2AB57, 0x91A18D8E, 0x95609039, 0x8B27C03C, 0x8FE6DD8B, 0x82A5FB52, 0x8664E6E5,
        0xBE2B5B58, 0xBAEA46EF, 0xB7A96036, 0xB3687D81, 0xAD2F2D84, 0xA9EE3033, 0xA4AD16EA, 0xA06C0B5D,
        0xD4326D90, 0xD0F37027, 0xDDB056FE, 0xD9714B49, 0xC7361B4C, 0xC3F706FB, 0xCEB42022, 0xCA753D95,
        0xF23A8028, 0xF6FB9D9F, 0xFBB8BB46, 0xFF79A6F1, 0xE13EF6F4, 0xE5FFEB43, 0xE8BCCD9A, 0xEC7DD02D,
        0x34867077, 0x30476DC0, 0x3D044B19, 0x39C556AE, 0x278206AB, 0x23431B1C, 0x2E003DC5, 0x2AC12072,
        0x128E9DCF, 0x164F8078, 0x1B0CA6A1, 0x1FCDBB16, 0x018AEB13, 0x054BF6A4, 0x0808D07D, 0x0CC9CDCA,
        0x7897AB07, 0x7C56B6B0, 0x71159069, 0x75D48DDE, 0x6B93DDDB, 0x6F52C06C, 0x6211E6B5, 0x66D0FB02,
        0x5E9F46BF, 0x5A5E5B08, 0x571D7DD1, 0x53DC6066, 0x4D9B3063, 0x495A2DD4, 0x44190B0D, 0x40D816BA,
        0xACA5C697, 0xA864DB20, 0xA527FDF9, 0xA1E6E04E, 0xBFA1B04B, 0xBB60ADFC, 0xB6238B25, 0xB2E29692,
        0x8AAD2B2F, 0x8E6C3698, 0x832F1041, 0x87EE0DF6, 0x99A95DF3, 0x9D684044, 0x902B669D, 0x94EA7B2A,
        0xE0B41DE7, 0xE4750050, 0xE9362689, 0xEDF73B3E, 0xF3B06B3B, 0xF771768C, 0xFA325055, 0xFEF34DE2,
        0xC6BCF05F, 0xC27DEDE8, 0xCF3ECB31, 0xCBFFD686, 0xD5B88683, 0xD1799B34, 0xDC3ABDED, 0xD8FBA05A,
        0x690CE0EE, 0x6DCDFD59, 0x608EDB80, 0x644FC637, 0x7A089632, 0x7EC98B85, 0x738AAD5C, 0x774BB0EB,
        0x4F040D56, 0x4BC510E1, 0x46863638, 0x42472B8F, 0x5C007B8A, 0x58C1663D, 0x558240E4, 0x51435D53,
        0x251D3B9E, 0x21DC2629, 0x2C9F00F0, 0x285E1D47, 0x36194D42, 0x32D850F5, 0x3F9B762C, 0x3B5A6B9B,
        0x0315D626, 0x07D4CB91, 0x0A97ED48, 0x0E56F0FF, 0x1011A0FA, 0x14D0BD4D, 0x19939B94, 0x1D528623,
        0xF12F560E, 0xF5EE4BB9, 0xF8AD6D60, 0xFC6C70D7, 0xE22B20D2, 0xE6EA3D65, 0xEBA91BBC, 0xEF68060B,
        0xD727BBB6, 0xD3E6A601, 0xDEA580D8, 0xDA649D6F, 0xC423CD6A, 0xC0E2D0DD, 0xCDA1F604, 0xC960EBB3,
        0xBD3E8D7E, 0xB9FF90C9, 0xB4BCB610, 0xB07DABA7, 0xAE3AFBA2, 0xAAFBE615, 0xA7B8C0CC, 0xA379DD7B,
        0x9B3660C6, 0x9FF77D71, 0x92B45BA8, 0x9675461F, 0x8832161A, 0x8CF30BAD, 0x81B02D74, 0x857130C3,
        0x5D8A9099, 0x594B8D2E, 0x5408ABF7, 0x50C9B640, 0x4E8EE645, 0x4A4FFBF2, 0x470CDD2B, 0x43CDC09C,
        0x7B827D21, 0x7F436096, 0x7200464F, 0x76C15BF8, 0x68860BFD, 0x6C47164A, 0x61043093, 0x65C52D24,
        0x119B4BE9, 0x155A565E, 0x18197087, 0x1CD86D30, 0x029F3D35, 0x065E2082, 0x0B1D065B, 0x0FDC1BEC,
        0x3793A651, 0x3352BBE6, 0x3E119D3F, 0x3AD08088, 0x2497D08D, 0x2056CD3A, 0x2D15EBE3, 0x29D4F654,
        0xC5A92679, 0xC1683BCE, 0xCC2B1D17, 0xC8EA00A0, 0xD6AD50A5, 0xD26C4D12, 0xDF2F6BCB, 0xDBEE767C,
        0xE3A1CBC1, 0xE760D676, 0xEA23F0AF, 0xEEE2ED18, 0xF0A5BD1D, 0xF464A0AA, 0xF9278673, 0xFDE69BC4,
        0x89B8FD09, 0x8D79E0BE, 0x803AC667, 0x84FBDBD0, 0x9ABC8BD5, 0x9E7D9662, 0x933EB0BB, 0x97FFAD0C,
        0xAFB010B1, 0xAB710D06, 0xA6322BDF, 0xA2F33668, 0xBCB4666D, 0xB8757BDA, 0xB5365D03, 0xB1F740B4,
        ]
def inventory_path_hash(object_path):
    """
    Computes the hashes used in the profile for weapon customizations and the golden key
    count.  Possibly used for other things, too.  Many thanks to Gibbed, yet again, for this!
    """
    global _weapon_cust_crc32_table
    if '.' not in object_path:
        object_path = '{}.{}'.format(object_path, object_path.split('/')[-1])

    # TODO: Gibbed was under the impression that these were checksummed in
    # UTF-16, but the hashes all match for me when using latin1/utf-8.
    object_full = object_path.upper().encode('latin1')
    crc32 = 0
    for char in object_full:
        crc32 = (_weapon_cust_crc32_table[(crc32 ^ (char >> 0)) & 0xFF] ^ (crc32 >> 8)) & 0xFFFFFFFF
        crc32 = (_weapon_cust_crc32_table[(crc32 ^ (char >> 8)) & 0xFF] ^ (crc32 >> 8)) & 0xFFFFFFFF
    return crc32

# Inventory Slots
(WEAPON1, WEAPON2, WEAPON3, WEAPON4, SHIELD, SPELL, MELEE, Pauldrons, SPELL2, Amulet, RING1, RING2) = range(12)
slot_to_eng = {
        WEAPON1: 'Weapon 1',
        WEAPON2: 'Weapon 2',
        WEAPON3: 'Weapon 3',
        WEAPON4: 'Weapon 4',
        SHIELD: 'Shield',
        SPELL: 'Spell',
        MELEE: 'Melee',
        Pauldrons: 'Pauldrons',
        SPELL2: 'Spell 2',
        Amulet: 'Amulet',
        RING1: 'RING 1',
        RING2: 'RING 2',
}
slotobj_to_slot = {
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon1.BPInvSlot_Weapon1': WEAPON1,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon2.BPInvSlot_Weapon2': WEAPON2,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon3.BPInvSlot_Weapon3': WEAPON3,
        '/Game/Gear/Weapons/_Shared/_Design/InventorySlots/BPInvSlot_Weapon4.BPInvSlot_Weapon4': WEAPON4,
        '/Game/Gear/SpellMods/_Shared/_Design/A_Data/BPInvSlot_SpellMod.BPInvSlot_SpellMod': SPELL,
        '/Game/Gear/SpellMods/_Shared/_Design/A_Data/BPInvSlot_SecondSpellMod.BPInvSlot_SecondSpellMod': SPELL2,
        '/Game/Gear/Shields/_Design/A_Data/BPInvSlot_Shield.BPInvSlot_Shield': SHIELD,
        '/Game/Gear/Melee/_Shared/_Design/A_Data/BPInvSlot_Melee.BPInvSlot_Melee': MELEE,
        '/Game/Gear/Pauldrons/_Shared/_Design/A_Data/InvSlot_Pauldron.InvSlot_Pauldron': Pauldrons,
        '/Game/Gear/Amulets/_Shared/_Design/A_Data/InvSlot_Amulet.InvSlot_Amulet': Amulet,
        '/Game/Gear/Rings/_Shared/Design/A_Data/InvSlot_Ring_1.InvSlot_Ring_1': RING1,
        '/Game/Gear/Rings/_Shared/Design/A_Data/InvSlot_Ring_2.InvSlot_Ring_2': RING2,
        }
slot_to_slotobj = {v: k for k, v in slotobj_to_slot.items()}

# Classes
(Spellshot, Clawbringer, Stabbomancer, Graveborn, SporeWarden) = range(5)
class_to_eng = {
        Spellshot: 'Spellshot',
        Clawbringer: 'Clawbringer',
        Stabbomancer: 'Stabbomancer',
        Graveborn: 'Graveborn',
        SporeWarden: 'Spore Warden',
        }
classobj_to_class = {
    '/Game/PlayerCharacters/GunMage/_Shared/_Design/SkillTree/AbilityTree_Branch_GunMage.AbilityTree_Branch_GunMage': Spellshot,
    '/Game/PlayerCharacters/KnightOfTheClaw/_Shared/_Design/SkillTree/AbilityTree_Branch_DragonCleric.AbilityTree_Branch_DragonCleric': Clawbringer,
    '/Game/PlayerCharacters/Ranger/_Shared/_Design/SkillTree/AbilityTree_Branch_Ranger.AbilityTree_Branch_Ranger': SporeWarden,
    '/Game/PlayerCharacters/Rogue/_Shared/_Design/SkillTree/AbilityTree_Branch_Rogue.AbilityTree_Branch_Rogue': Stabbomancer,
    '/Game/PlayerCharacters/Necromancer/_Shared/_Design/SkillTree/AbilityTree_Branch_Necromancer.AbilityTree_Branch_Necromancer': Graveborn,
}

mission_to_name = {
    '/game/missions/plot/mission_plot00.mission_plot00_c': '',
    '/game/missions/plot/mission_plot01.mission_plot01_c': '',
    '/game/missions/side/overworld/overworld/aknifeattheirbacks/mission_ow_aknifeattheirbacks.mission_ow_aknifeattheirbacks_c': '',
    '/game/missions/plot/mission_plot02.mission_plot02_c': '',
    '/game/missions/side/zone_1/intro/mission_ratquestpt1.mission_ratquestpt1_c': '',
    '/game/missions/plot/mission_plot04.mission_plot04_c': '',
    '/game/missions/side/zone_1/intro/mission_ratquestpt2.mission_ratquestpt2_c': '',
    '/game/missions/major/goblin/mission_gtfo.mission_gtfo_c': '',
    '/game/missions/side/overworld/overworld/inmyimage/mission_ow_inmyimage.mission_ow_inmyimage_c': '',
    '/game/missions/side/overworld/overworld/ab1_minersproblem/mission_ow_ab1_minersproblem.mission_ow_ab1_minersproblem_c': '',
    '/game/missions/side/overworld/overworld/fumblingaround/mission_ow_fumblingaround.mission_ow_fumblingaround_c': '',
    '/game/missions/side/overworld/overworld/itfellfromtheskies/mission_ow_itfellfromtheskies.mission_ow_itfellfromtheskies_c': '',
    '/game/missions/major/goblin/mission_gtfop2.mission_gtfop2_c': '',
    '/game/missions/side/zone_1/goblin/mission_murderhobos.mission_murderhobos_c': '',
    '/game/missions/side/zone_1/goblin/mission_smithscharade.mission_smithscharade_c': '',
    '/game/missions/side/zone_1/mushroom/mission_claptrapgrenade.mission_claptrapgrenade_c': '',
    '/game/missions/side/zone_1/mushroom/mission_blueones.mission_blueones_c': '',
    '/game/missions/side/zone_1/mushroom/mission_minstrelmetal.mission_minstrelmetal_c': '',
    '/game/missions/side/zone_1/mushroom/mission_toothfairy.mission_toothfairy_c': '',
    '/game/missions/side/zone_1/hubtown/mission_innerdemons.mission_innerdemons_c': '',
    '/game/missions/plot/mission_plot05.mission_plot05_c': '',
    '/game/missions/side/overworld/overworld/blessedbethysword/mission_ow_blessedbethysword.mission_ow_blessedbethysword_c': '',
    '/game/missions/plot/mission_plot06.mission_plot06_c': '',
    '/game/missions/side/overworld/overworld/thelegendarybow/mission_ow_thelegendarybow.mission_ow_thelegendarybow_c': '',
    '/game/missions/side/overworld/overworld/ab2_miraclegrow/mission_ow_ab2_miraclegrow.mission_ow_ab2_miraclegrow_c': '',
    '/game/missions/side/zone_2/seabed/mission_sharkpearls.mission_sharkpearls_c': '',
    '/game/missions/side/zone_2/seabed/mission_dyingwish.mission_dyingwish_c': '',
    '/game/missions/plot/mission_plot07.mission_plot07_c': '',
    '/game/missions/side/overworld/overworld/visionofdeception/mission_ow_visionofdeception.mission_ow_visionofdeception_c': '',
    '/game/missions/major/pirate/mission_crookedeyephil.mission_crookedeyephil_c': '',
    '/game/missions/side/overworld/overworld/clericallylost/mission_ow_clericallylost.mission_ow_clericallylost_c': '',
    '/game/missions/side/zone_2/pirate/mission_littlepookie.mission_littlepookie_c': '',
    '/game/missions/side/zone_2/pirate/mission_whaletale.mission_whaletale_c': '',
    '/game/missions/side/zone_2/pirate/mission_jaggedtoothcrew.mission_jaggedtoothcrew_c': '',
    '/game/missions/side/zone_2/pirate/mission_piratelife.mission_piratelife_c': '',
    '/game/missions/side/overworld/overworld/ibelieveicantouchthesky/mission_ow_ibelieveicantouchthesky.mission_ow_ibelieveicantouchthesky_c': '',
    '/game/missions/side/zone_2/abyss/mission_curseofthetwistedsisters.mission_curseofthetwistedsisters_c': '',
    '/game/missions/side/zone_2/abyss/mission_diplomacy.mission_diplomacy_c': '',
    '/game/missions/plot/mission_plot08.mission_plot08_c': '',
    '/game/missions/major/beanstalk/mission_skybound.mission_skybound_c': '',
    '/game/missions/side/zone_3/climb/mission_lavagoodtime.mission_lavagoodtime_c': '',
    '/game/missions/side/zone_2/beanstalk/mission_derat.mission_derat_c': '',
    '/game/missions/side/zone_2/beanstalk/mission_elderwyvern.mission_elderwyvern_c': '',
    '/game/missions/side/zone_2/beanstalk/mission_ronrivote.mission_ronrivote_c': '',
    '/game/missions/side/overworld/overworld/crabythepet/mission_ow_crabythepet.mission_ow_crabythepet_c': '',
    '/game/missions/plot/mission_plot09.mission_plot09_c': '',
    '/game/missions/side/zone_3/climb/mission_monsterlover.mission_monsterlover_c': '',
    '/game/missions/side/zone_3/sands/mission_bluehatcult.mission_bluehatcult_c': '',
    '/game/missions/side/zone_1/sewers/mission_cloggageofthedammed.mission_cloggageofthedammed_c': '',
    '/game/missions/major/oasis/mission_doomed.mission_doomed_c': '',
    '/game/missions/side/zone_3/climb/mission_ancientpowers.mission_ancientpowers_c': '',
    '/game/missions/side/zone_3/climb/mission_ancientpowerscombat1.mission_ancientpowerscombat1_c': '',
    '/game/missions/side/zone_3/climb/mission_ancientpowerscombat2.mission_ancientpowerscombat2_c': '',
    '/game/missions/side/zone_3/climb/mission_ancientpowersdreadlord.mission_ancientpowersdreadlord_c': '',
    '/game/missions/side/overworld/overworld/pocketsandstorm/mission_ow_pocketsandstorm.mission_ow_pocketsandstorm_c': '',
    '/game/missions/side/overworld/overworld/eyelostit/mission_ow_eyelostit.mission_ow_eyelostit_c': '',
    '/game/missions/side/overworld/overworld/ab3_solarcream/mission_ow_ab3_solarcream.mission_ow_ab3_solarcream_c': '',
    '/game/missions/side/zone_3/oasis/mission_lowtideboil.mission_lowtideboil_c': '',
    '/game/missions/side/zone_3/sands/mission_elementalbeer.mission_elementalbeer_c': '',
    '/game/missions/plot/mission_plot10.mission_plot10_c': '',
    '/game/missions/plot/mission_plot11.mission_plot11_c': '',
    '/game/missions/side/overworld/overworld/destructionrainsfromtheheaven/mission_ow_destructionrainsfromtheheaven.mission_ow_destructionrainsfromtheheaven_c': '',
}

# XP
max_level = 40
required_xp_list = [
    0,          # lvl 1
    358,        # lvl 2
    1241,       # lvl 3
    2850,       # lvl 4
    5376,       # lvl 5
    8997,       # lvl 6
    13886,      # lvl 7
    20208,      # lvl 8
    28126,      # lvl 9
    37798,      # lvl 10
    49377,      # lvl 11
    63016,      # lvl 12
    78861,      # lvl 13
    97061,      # lvl 14
    117757,     # lvl 15
    141092,     # lvl 16
    167206,     # lvl 17
    196238,     # lvl 18
    228322,     # lvl 19
    263595,     # lvl 20
    302190,     # lvl 21
    344238,     # lvl 22
    389873,     # lvl 23
    439222,     # lvl 24
    492414,     # lvl 25
    549578,     # lvl 26
    610840,     # lvl 27
    676325,     # lvl 28
    746158,     # lvl 29
    820463,     # lvl 30
    899363,     # lvl 31
    982980,     # lvl 32
    1071435,    # lvl 33
    1164850,    # lvl 34
    1263343,    # lvl 35
    1367034,    # lvl 36
    1476041,    # lvl 37
    1590483,    # lvl 38
    1710476,    # lvl 39
    1836137,    # lvl 40
]
max_supported_level = len(required_xp_list)

# Currencies
(MONEY, MOON) = range(2)
currency_to_eng = {
        MONEY: 'Money',
        MOON: 'Moon orbs',
        }
currency_to_curhash = {
        MONEY: 618814354,
        MOON: 3679636065
        }
curhash_to_currency = {v: k for k, v in currency_to_curhash.items()}


# Ammo
(AMMO_AR, AMMO_GRENADE, AMMO_HEAVY, AMMO_PISTOL, AMMO_SMG, AMMO_SHOTGUN, AMMO_SNIPER, AMMO_SPELL) = range(8)
ammo_to_eng = {
        AMMO_AR: 'AR',
        AMMO_GRENADE: 'Grenade',
        AMMO_HEAVY: 'Heavy',
        AMMO_PISTOL: 'Pistol',
        AMMO_SMG: 'SMG',
        AMMO_SHOTGUN: 'Shotgun',
        AMMO_SNIPER: 'Sniper',
        AMMO_SPELL: 'Spell',
        }
ammoobj_to_ammo = {
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_AssaultRifle.Resource_Ammo_AssaultRifle': AMMO_AR,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Grenade.Resource_Ammo_Grenade': AMMO_GRENADE,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Heavy.Resource_Ammo_Heavy': AMMO_HEAVY,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Pistol.Resource_Ammo_Pistol': AMMO_PISTOL,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_SMG.Resource_Ammo_SMG': AMMO_SMG,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Shotgun.Resource_Ammo_Shotgun': AMMO_SHOTGUN,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Sniper.Resource_Ammo_Sniper': AMMO_SNIPER,
        '/Game/GameData/Weapons/Ammo/Resource_Ammo_Spell.Resource_Ammo_Spell': AMMO_SPELL,
        }


# Golden Keys
goldenkey_category = '/Game/Gear/_Shared/_Design/InventoryCategories/InventoryCategory_GoldenKey'
goldenkey_hash = inventory_path_hash(goldenkey_category)

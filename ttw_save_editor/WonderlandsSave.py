import struct

import google
from google.protobuf import json_format

from ttw_save_editor.constants import slotobj_to_slot, required_xp_list, classobj_to_class, class_to_eng, MONEY, MOON, \
    curhash_to_currency, slot_to_eng, mission_to_name, ammoobj_to_ammo, ammo_to_eng, currency_to_curhash
from ttw_save_editor import OakShared_pb2, OakSave_pb2, datalib
from ttw_save_editor.WonderlandsItem import WonderlandsEquipSlot, WonderlandsItem

MissionState = OakSave_pb2.MissionStatusPlayerSaveGameData.MissionState

class WonderlandsSave(object):
    _prefix_magic = bytearray([
        0x71, 0x34, 0x36, 0xB3, 0x56, 0x63, 0x25, 0x5F,
        0xEA, 0xE2, 0x83, 0x73, 0xF4, 0x98, 0xB8, 0x18,
        0x2E, 0xE5, 0x42, 0x2E, 0x50, 0xA2, 0x0F, 0x49,
        0x87, 0x24, 0xE6, 0x65, 0x9A, 0xF0, 0x7C, 0xD7,
        ])

    _xor_magic = bytearray([
        0x7C, 0x07, 0x69, 0x83, 0x31, 0x7E, 0x0C, 0x82,
        0x5F, 0x2E, 0x36, 0x7F, 0x76, 0xB4, 0xA2, 0x71,
        0x38, 0x2B, 0x6E, 0x87, 0x39, 0x05, 0x02, 0xC6,
        0xCD, 0xD8, 0xB1, 0xCC, 0xA1, 0x33, 0xF9, 0xB6,
        ])

    def __init__(self, filename, debug=False):
        self.filename = filename
        self.datawrapper = datalib.DataWrapper()
        with open(filename, 'rb') as df:
            header = df.read(4)
            assert(header == b'GVAS')

            self.sg_version = self._read_int(df)
            if debug:
                print('Savegame version: {}'.format(self.sg_version))
            self.pkg_version = self._read_int(df)
            if debug:
                print('Package version: {}'.format(self.pkg_version))
            self.engine_major = self._read_short(df)
            self.engine_minor = self._read_short(df)
            self.engine_patch = self._read_short(df)
            self.engine_build = self._read_int(df)
            if debug:
                print('Engine version: {}.{}.{}.{}'.format(
                    self.engine_major,
                    self.engine_minor,
                    self.engine_patch,
                    self.engine_build,
                    ))
            self.build_id = self._read_str(df)
            if debug:
                print('Build ID: {}'.format(self.build_id))
            self.fmt_version = self._read_int(df)
            if debug:
                print('Custom Format Version: {}'.format(self.fmt_version))
            fmt_count = self._read_int(df)
            if debug:
                print('Custom Format Data Count: {}'.format(fmt_count))
            self.custom_format_data = []
            for _ in range(fmt_count):
                guid = self._read_guid(df)
                entry = self._read_int(df)
                if debug:
                    print(' - GUID {}: {}'.format(guid, entry))
                self.custom_format_data.append((guid, entry))
            self.sg_type = self._read_str(df)
            if debug:
                print('Savegame type: {}'.format(self.sg_type))
            remaining_data_len = self._read_int(df)
            data = bytearray(df.read(remaining_data_len))

            # Decrypt
            for i in range(len(data)-1, -1, -1):
                if i < 32:
                    b = WonderlandsSave._prefix_magic[i]
                else:
                    b = data[i - 32]
                b ^= WonderlandsSave._xor_magic[i % 32]
                data[i] ^= b

            # Make sure that was all there was
            last = df.read()
            assert(len(last) == 0)

            # Parse protobufs
            self.import_protobuf(data)

    def import_protobuf(self, data):
        """
        Given raw protobuf data, load it into ourselves so
        that we can work with it.  This also sets up a few
        convenience vars for our later use
        """

        # Now parse the protobufs
        self.save = OakSave_pb2.Character()
        try:
            self.save.ParseFromString(data)
        except google.protobuf.message.DecodeError as e:
            raise Exception('Unable to parse savegame (did you pass a profile, instead?): {}'.format(e)) from None

        # Some sanity checks, since this is a potentially problematic
        # operation.
        assert(self.save.IsInitialized())
        assert(len(self.save.UnknownFields()) == 0)

        # Do some data processing so that we can wrap things APIwise
        # First: Items
        self.items = [WonderlandsItem(i, self.datawrapper) for i in self.save.inventory_items]
        self.equipslots = {}
        for e in self.save.equipped_inventory_list:
            equip = WonderlandsEquipSlot(e)
            slot = slotobj_to_slot[equip.get_obj_name()]
            self.equipslots[slot] = equip


    def _read_int(self, df):
        return struct.unpack('<I', df.read(4))[0]

    def _write_int(self, df, value):
        df.write(struct.pack('<I', value))

    def _read_short(self, df):
        return struct.unpack('<H', df.read(2))[0]

    def _write_short(self, df, value):
        df.write(struct.pack('<H', value))

    def _read_str(self, df):
        datalen = self._read_int(df)
        if datalen == 0:
            return None
        elif datalen == 1:
            return ''
        else:
            value = df.read(datalen)
            return value[:-1].decode('utf-8')

    def _write_str(self, df, value):
        if value is None:
            self._write_int(df, 0)
        elif value == '':
            self._write_int(df, 1)
        else:
            data = value.encode('utf-8') + b'\0'
            self._write_int(df, len(data))
            df.write(data)

    def _read_guid(self, df):
        data = df.read(16)
        return data

    def _write_guid(self, df, value):
        df.write(value)

    def get_char_name(self):
        """
        Returns the character name
        """
        return self.save.preferred_character_name

    def set_char_name(self, new_name):
        """
        Sets the character name
        """
        self.save.preferred_character_name = new_name

    def get_savegame_id(self):
        """
        Returns the savegame ID (not sure if this is important at all)
        """
        return self.save.save_game_id

    def set_savegame_id(self, new_id):
        """
        Sets the savegame ID (not sure if this is important at all)
        """
        self.save.save_game_id = new_id

    def get_savegame_guid(self):
        """
        Returns the savegame GUID
        """
        return self.save.save_game_guid

    def set_savegame_guid(self, new_id):
        """
        Sets the savegame GUID (not sure if this is important at all)
        """
        self.save.save_game_guid = new_id

    def get_xp(self):
        """
        Returns the character's XP
        """
        return self.save.experience_points

    def get_consitution(self):
        return self.save.hero_points_save_data.constitution
        # return self.get_hero_points('constitution')

    def get_dexterity(self):
        return self.save.hero_points_save_data.dexterity
        # return self.get_hero_points('dexterity')

    def get_intelligence(self):
        return self.save.hero_points_save_data.intelligence
        # return self.get_hero_points('intelligence')

    def get_luck(self):
        return self.save.hero_points_save_data.luck
        # return self.get_hero_points('luck')

    def get_strength(self):
        return self.save.hero_points_save_data.strength
        # return self.get_hero_points('strength')

    def get_wisdom(self):
        return self.save.hero_points_save_data.wisdom
        # return self.get_hero_points('wisdom')

    def set_first_class(self, new_class):
        self.save.ability_data.dual_class_save_data.primary_branch_path = new_class

    def set_second_class(self, new_class):
        self.save.ability_data.dual_class_save_data.slotted_secondary_branch_path = new_class

    def get_first_class(self):
        return self.save.ability_data.dual_class_save_data.primary_branch_path

    def get_second_class(self):
        return self.save.ability_data.dual_class_save_data.slotted_secondary_branch_path

    # def get_hero_points(self, point_type):
    #     return self.save.hero_points_save_data[point_type]

    def set_appearance(self, appearance):
        for elm in appearance:
            self.save.custom_float_customizations.append(OakSave_pb2.CustomFloatCustomizationSaveGameData(
                name=elm.name,
                value=elm.value,
            ))

    def set_appearance2(self, appearance):
        for elm in appearance:
            self.save.selected_customizations.append(elm)

    def get_appearance(self):
        return self.save.custom_float_customizations

    def get_appearance2(self):
        return self.save.selected_customizations

    def set_backstory(self, backstory):
        self.save.hero_points_save_data.player_aspect_data_path = backstory

    def get_backstory(self):
        return self.save.hero_points_save_data.player_aspect_data_path

    def get_level(self):
        """
        Returns the character's level
        """
        xp = self.get_xp()
        cur_lvl = 0
        for req_xp_lvl in required_xp_list:
            if xp >= req_xp_lvl:
                cur_lvl += 1
            else:
                return cur_lvl
        return cur_lvl

    def get_primary_class(self, eng=False):
        """
        Returns the class of this character.  By default it will be a constant,
        but if `eng` is `True` it will be an English label instead.
        """
        classval = classobj_to_class[self.save.ability_data.dual_class_save_data.primary_branch_path]
        if eng:
            return class_to_eng[classval]
        return classval

    def get_secondary_class(self, eng=False):
        """
        Returns the class of this character.  By default it will be a constant,
        but if `eng` is `True` it will be an English label instead.
        """
        if not self.save.ability_data.dual_class_save_data.slotted_secondary_branch_path:
            return "Not yet unlocked"
        classval = classobj_to_class[self.save.ability_data.dual_class_save_data.slotted_secondary_branch_path]
        if eng:
            return class_to_eng[classval]
        return classval

    def get_currency(self, currency_type):
        """
        Returns the amount of currency of the given type
        """
        for cat_save_data in self.save.inventory_category_list:
            if cat_save_data.base_category_definition_hash in curhash_to_currency:
                if currency_type == curhash_to_currency[cat_save_data.base_category_definition_hash]:
                    return cat_save_data.quantity
        return 0

    def get_discovery(self):
        data = self.save.discovery_data.discovered_level_info
        first = data[0]
        infos = first.discovered_area_info
        a = infos[0]
        return None

    def get_playthroughs_completed(self):
        """
        Returns the number of playthroughs completed
        """
        return self.save.playthroughs_completed

    def get_pt_active_mission_lists(self, eng=False):
        """
        Returns a list of active missions for each Playthrough.  Missions will
        be in their object name by default, or their English names if `eng` is
        `True`.
        """
        return self.get_pt_mission_lists(MissionState.MS_Active, eng)

    def get_pt_completed_mission_lists(self, eng=False):
        """
        Returns a list of completed missions for each Playthrough.  Missions will
        be in their object name by default, or their English names if `eng` is
        `True`.
        """
        return self.get_pt_mission_lists(MissionState.MS_Complete, eng)

    def get_pt_mission_lists(self, mission_status, eng=False):
        """
        Returns a list of missions in the given `mission_status`, for each
        Playthrough.  Missions will be in their object name by default, or
        their English names if `eng` is `True`.
        """
        to_ret = []
        for pt in self.save.mission_playthroughs_data:
            active_missions = []
            for mission in pt.mission_list:
                if mission.status == mission_status:
                    mission_name = mission.mission_class_path
                    if eng:
                        if mission_name.lower() in mission_to_name:
                            mission_name = mission_to_name[mission_name.lower()]
                        else:
                            mission_name = '(Unknown mission: {})'.format(mission_name)
                    active_missions.append(mission_name)
            to_ret.append(active_missions)
        return to_ret

    def get_money(self):
        """
        Returns the amount of money we have
        """
        return self.get_currency(MONEY)

    def get_moon_orb(self):
        """
        Returns the amount of money we have
        """
        return self.get_currency(MOON)

    def get_equip_slot(self, slot):
        """
        Returns the BL3EquipSlot object in the specified `slot`.
        """
        if slot in self.equipslots:
            return self.equipslots[slot]
        return None

    def get_items(self):
        """
        Returns a list of the character's inventory items, as BL3Item objects.
        """
        return self.items

    def get_item_at(self, target):
        for e in self.save.equipped_inventory_list:
            equip = WonderlandsEquipSlot(e)
            slot = slotobj_to_slot[equip.get_obj_name()]
            if slot == target:
                slot_id = equip.get_inventory_idx()
                return self.get_items()[slot_id]
        return None

    def get_equipped_items(self, eng=False):
        """
        Returns a dict containing the slot and the equipped item.  The slot will
        be a constant by default, or an English label if `eng` is `True`
        """
        to_ret = {}
        for (key, equipslot) in self.equipslots.items():
            if eng:
                key = slot_to_eng[key]
            if equipslot.get_inventory_idx() >= 0:
                to_ret[key] = self.items[equipslot.get_inventory_idx()]
            else:
                to_ret[key] = None
        return to_ret

    def get_ammo_counts(self, eng=False):
        """
        Returns a dict containing the Ammo type and count.  The ammo type key will
        be a constant by default, or an English label if `eng` is `True`.
        """
        to_ret = {}
        for pool in self.save.resource_pools:
            # In some cases, Eridium can show up as an ammo type.  Related to the
            # Fabricator, presumably.  Anyway, just ignore it.
            if 'Eridium' in pool.resource_path:
                continue
            key = ammoobj_to_ammo[pool.resource_path]
            if eng:
                key = ammo_to_eng[key]
            to_ret[key] = int(pool.amount)
        return to_ret

    def save_to(self, filename):
        """
        Saves ourselves to a new filename
        """
        with open(filename, 'wb') as df:

            # Header info
            df.write(b'GVAS')
            self._write_int(df, self.sg_version)
            self._write_int(df, self.pkg_version)
            self._write_short(df, self.engine_major)
            self._write_short(df, self.engine_minor)
            self._write_short(df, self.engine_patch)
            self._write_int(df, self.engine_build)
            self._write_str(df, self.build_id)
            self._write_int(df, self.fmt_version)
            self._write_int(df, len(self.custom_format_data))
            for guid, entry in self.custom_format_data:
                self._write_guid(df, guid)
                self._write_int(df, entry)
            self._write_str(df, self.sg_type)

            # Turn our parsed protobuf back into data
            data = bytearray(self.save.SerializeToString())

            # Encrypt
            for i in range(len(data)):
                if i < 32:
                    b = self._prefix_magic[i]
                else:
                    b = data[i - 32]
                b ^= self._xor_magic[i % 32]
                data[i] ^= b

            # Write out to the file
            self._write_int(df, len(data))
            df.write(data)

    def save_json_to(self, filename):
        """
        Saves a JSON version of our protobuf to the specfied filename
        """
        with open(filename, 'w') as df:
            df.write(json_format.MessageToJson(self.save,
                including_default_value_fields=True,
                preserving_proto_field_name=True,
            ))

    def import_json(self, json_str):
        """
        Given JSON data, convert to protobuf and load it into ourselves so
        that we can work with it.  This also sets up a few convenience vars
        for our later use
        """
        message = google.protobuf.json_format.Parse(json_str, OakSave_pb2.Character())
        self.import_protobuf(message.SerializeToString())

    def set_currency(self, currency_type, new_value):
        """
        Sets a new currency value
        """

        # Update an existing value, if we have it
        for cat_save_data in self.save.inventory_category_list:
            if cat_save_data.base_category_definition_hash in curhash_to_currency:
                if currency_type == curhash_to_currency[cat_save_data.base_category_definition_hash]:
                    cat_save_data.quantity = new_value
                    return

        # Add a new one, if we don't
        self.save.inventory_category_list.append(OakShared_pb2.InventoryCategorySaveData(
            base_category_definition_hash=currency_to_curhash[currency_type],
            quantity=new_value,
            ))

    def set_money(self, amount):
        self.set_currency(MONEY, amount)

    def generate_random_item(self, original_item, count):
        for i in range(0, count):
            new_item_raw = WonderlandsItem.add_random(original_item)
            print("[{}] creating {}".format(i, new_item_raw.get_serial_base64()))
            new_item = self.create_new_item(new_item_raw.get_serial_number())
            self.add_item(new_item)

    def create_new_item(self, item_serial):
        """
        Creates a new item from the given binary `item_serial`, which can later
        be added to our item list.
        """

        # Okay, I have no idea what this pickup_order_index attribute is about, but let's
        # make sure it's unique anyway.  It might be related to ordering when picking
        # up multiple items at once, which would probably make it more useful for auto-pick-up
        # items like money and ammo...
        max_pickup_order = 0
        for item in self.items:
            if item.get_pickup_order_idx() > max_pickup_order:
                max_pickup_order = item.get_pickup_order_idx()

        # Create the item and return it
        new_item = WonderlandsItem.create(self.datawrapper,
                serial_number=item_serial,
                pickup_order_idx=max_pickup_order+1,
                is_favorite=True,
                )
        return new_item

    def add_item(self, new_item):
        """
        Adds a new `new_item` (BL3Item object) to our item list.  Returns the item's
        new index in our item list.
        """

        # Add the item to the protobuf
        self.save.inventory_items.append(new_item.protobuf)

        # The protobuf reference that we append to the protobuf list
        # ends up *not* being the one that's actually used when we
        # save, so if we want to be able to alter it later (say, below
        # when levelling up items), we have to grab a fresh reference
        # to it.
        new_item.protobuf = self.save.inventory_items[-1]

        # Now update our internal items list and return
        self.items.append(new_item)
        return len(self.items)-1

    def add_new_item(self, item_serial):
        """
        Adds a new item to our item list using the binary `item_serial`.
        Returns a tuple containing the new BL3Item object itself, and its
        new index in our item list.
        """
        new_item = self.create_new_item(item_serial)
        return (new_item, self.add_item(new_item))

    def add_new_item_encoded(self, item_serial_b64):
        """
        Adds a new item to our item list using the base64-encoded (and
        "BL3()"-wrapped) `item_serial_b64`.  Returns a tuple containing the
        new BL3Item object itself, and its new index in our item list.
        """
        return self.add_new_item(datalib.BL3Serial.decode_serial_base64(item_serial_b64))

    def clone_PT(self, target_save):
        target_save.set_char_name(self.get_char_name())
        target_save.set_savegame_id(self.get_savegame_id())
        target_save.set_savegame_guid(self.get_savegame_guid())
        target_save.set_first_class(self.get_first_class())
        target_save.set_second_class(self.get_second_class())
        target_save.set_appearance(self.get_appearance())
        target_save.set_appearance2(self.get_appearance2())
        target_save.set_backstory(self.get_backstory())
        self.save = target_save.save

    def transfertEnchant(self, slot_target, slot_enchant):
        target = self.get_item_at(slot_target)
        enchant = self.get_item_at(slot_enchant)
        gparts = enchant.generic_parts
        target.set_generic_parts(gparts)
        self.add_new_item(target.get_serial_number())

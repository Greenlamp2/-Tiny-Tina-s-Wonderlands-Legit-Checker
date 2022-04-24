from Items import Items
from ttw_save_editor import OakSave_pb2, OakShared_pb2, datalib
from ttw_save_editor.datalib import BL3Serial


class WonderlandsItem(datalib.BL3Serial):
    """
    Pretty thin wrapper around the protobuf object for an item.  We're
    ignoring `development_save_data` entirely since it doesn't seem to
    be present in actual savegames.

    No idea what `pickup_order_index` is, though it might just have
    something to do with the ordering when you're picking up multiple
    things at once (in which case it's probably only really useful for
    things like money and ammo).
    """

    def __init__(self, protobuf, datawrapper):
        self.protobuf = protobuf
        super().__init__(self.protobuf.item_serial_number, datawrapper)

    @staticmethod
    def reverse_item_serial(serial_number):
        c = BL3Serial.decode_serial_base64(serial_number)
        datawrapper = datalib.DataWrapper()
        return datalib.BL3Serial(c, datawrapper)

    @staticmethod
    def add_random(item):
        original_item = WonderlandsItem.reverse_item_serial(item.get_serial_base64())
        db = Items()
        db.load('export/gun_balances_long.csv', "GUNS")
        db.load('export/shield_balances_long.csv', "SHIELDS")
        db.load('export/pauldron_balances_long.csv', "PAULDRONS")
        db.load('export/spell_balances_long.csv', "SPELLS")
        db.load('export/ring_balances_long.csv', "RINGS")
        db.load('export/amulet_balances_long.csv', "AMULETS")
        db.load('export/melee_balances_long.csv', "MELEE")
        new_parts = db.generate_random(item)
        item.set_parts(new_parts)
        item.set_item_type(3)
        if db.is_legit(item, silent=True):
            return item
        else:
            print("it was not legit, generating a new one")
            return WonderlandsItem.add_random(original_item)

    @staticmethod
    def create(datawrapper, serial_number, pickup_order_idx, skin_path='', is_seen=True, is_favorite=False, is_trash=False):
        """
        Creates a new item with the specified serial number, pickup_order_idx, and skin_path.
        """

        # Start constructing flags
        flags = 0
        if is_seen:
            flags |= 0x1

        # Favorite and Trash are mutually-exclusive
        if is_favorite:
            flags |= 0x2
        elif is_trash:
            flags |= 0x4

        # Now do the creation
        return WonderlandsItem(OakShared_pb2.OakInventoryItemSaveGameData(
                item_serial_number=serial_number,
                pickup_order_index=pickup_order_idx,
                flags=flags,
                ), datawrapper)

    def get_pickup_order_idx(self):
        return self.protobuf.pickup_order_index

    def _update_superclass_serial(self):
        """
        Action to take when our serial number gets updated.  In this case,
        setting the serial back into the protobuf.
        """
        self.protobuf.item_serial_number = self.serial

class WonderlandsEquipSlot(object):
    """
    Real simple wrapper for a BL3 equipment slot.

    We touch this in a couple of different ways, so it felt like maybe we should
    wrap it up a bit.  We don't touch trinkets at all so I haven't wrapped any
    of that stuff.

    All these getters/setters are rather un-Pythonic; should be using
    some decorations for that instead.  Alas!
    """

    def __init__(self, protobuf):
        self.protobuf = protobuf

    @staticmethod
    def create(index, obj_name, enabled=True, trinket_name=''):
        return WonderlandsEquipSlot(OakSave_pb2.EquippedInventorySaveGameData(
            inventory_list_index=index,
            enabled=enabled,
            slot_data_path=obj_name,
            trinket_data_path=trinket_name,
            ))

    def get_inventory_idx(self):
        """
        Gets the inventory index that we're pointing to
        """
        return self.protobuf.inventory_list_index

    def set_inventory_idx(self, new_idx):
        """
        Sets the inventory index that we're pointing to
        """
        self.protobuf.inventory_list_index = new_idx

    def enabled(self):
        """
        Returns whether we're enabled or not
        """
        return self.protobuf.enabled

    def set_enabled(self, enabled=True):
        """
        Sets our enabled state
        """
        self.protobuf.enabled = enabled

    def get_obj_name(self):
        """
        Returns our path object name
        """
        return self.protobuf.slot_data_path
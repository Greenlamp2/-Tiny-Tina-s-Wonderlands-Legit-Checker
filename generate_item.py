import os

from Items import Items
from ttw_save_editor.WonderlandsItem import WonderlandsItem
from ttw_save_editor.WonderlandsSave import WonderlandsSave

if __name__ == '__main__':
    db = Items()
    db.load('export/gun_balances_long.csv', "GUNS")
    db.load('export/shield_balances_long.csv', "SHIELDS")
    db.load('export/pauldron_balances_long.csv', "PAULDRONS")
    db.load('export/spell_balances_long.csv', "SPELLS")
    db.load('export/ring_balances_long.csv', "RINGS")
    db.load('export/amulet_balances_long.csv', "AMULETS")
    db.load('export/melee_balances_long.csv', "MELEE")

    serial = "TTW(BQAAAABMOYC7JioAgTKAeEREJqAAAAAA)"
    item = WonderlandsItem.reverse_item_serial(serial)
    new_item = WonderlandsItem.add_random(item)

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    save_a = WonderlandsSave(os.path.join(__location__, "saves_test/9.sav"))
    save_a.generate_random_item(item, 1)
    save_a.save_to("saves_test/9.sav")

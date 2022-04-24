from Items import Items
from ttw_save_editor.WonderlandsItem import WonderlandsItem

if __name__ == '__main__':
    db = Items()
    db.load('export/gun_balances.csv', "GUNS")
    db.load('export/shield_balances.csv', "SHIELDS")
    db.load('export/pauldron_balances.csv', "PAULDRONS")
    db.load('export/spell_balances.csv', "SPELLS")
    db.load('export/ring_balances.csv', "RINGS")
    db.load('export/amulet_balances.csv', "AMULETS")
    db.load('export/melee_balances.csv', "MELEE")

    serial = "TTW(BQAAAAA7kIA745WggIKuqaIsOpIg1PBYMsODgBAAAAAAAKCMAQEB)"
    item = WonderlandsItem.reverse_item_serial(serial)
    is_legit = db.is_legit(item)
import os

from Items import Items
from ttw_save_editor.WonderlandsSave import WonderlandsSave

if __name__ == '__main__':
    db = Items()
    db.load('export/gun_balances.csv', "GUNS")
    db.load('export/shield_balances.csv', "SHIELDS")
    db.load('export/pauldron_balances.csv', "PAULDRONS")
    db.load('export/spell_balances.csv', "SPELLS")
    db.load('export/ring_balances.csv', "RINGS")
    db.load('export/amulet_balances.csv', "AMULETS")
    db.load('export/melee_balances.csv', "MELEE")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    save_a = WonderlandsSave(os.path.join(__location__, "saves_test/1.sav"))
    items = save_a.get_items()
    for item in items:
        # print(item.get_serial_base64())
        balance = item.balance
        all_parts = db.get_parts(item.balance_short)
        if not all_parts:
            print("--- No data about {}".format(item.balance_short))
            continue
        is_legit = db.is_legit(item)
        if not is_legit:
            print("--------------------------------> {} is not legit <--------------------------------".format(item.balance_short))

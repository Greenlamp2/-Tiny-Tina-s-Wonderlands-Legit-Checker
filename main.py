import os

from Items import Items
from ttw_save_editor.WonderlandsSave import WonderlandsSave

if __name__ == '__main__':
    db = Items()
    db.load('db/gun_balances.csv', "GUNS")
    db.load('db/shield_balances.csv', "SHIELDS")
    db.load('db/com_balances.csv', "PAULDRONS")
    db.load('db/spell_balances.csv', "SPELLS")
    db.load('db/ring_balances.csv', "RINGS")
    db.load('db/amulet_balances.csv', "AMULETS")
    db.load('db/melee_balances.csv', "MELEE")

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    save_a = WonderlandsSave(os.path.join(__location__, "saves_test/1.sav"))
    items = save_a.get_items()
    for item in items:
        balance = item.balance
        all_parts = db.get_parts(item.balance_short)
        if not all_parts:
            print("--- No data about {}".format(item.balance_short))
            continue
        is_legit = db.is_legit(item)
        if is_legit:
            print("{} is legit".format(item.balance_short))
        else:
            print("--------------------------------> {} is not legit <--------------------------------".format(item.balance_short))

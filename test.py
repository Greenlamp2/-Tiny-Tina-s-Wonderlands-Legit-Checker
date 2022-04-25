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

    # db.reverse_item_serial("SERIAL"),
    # items = [
    #     db.reverse_item_serial("TTW(BQAAAACcc4C6Kwbhh5oMMJCeCj+o4UhPWJGFFSedJEcSnEKqRDMYCAAAAAAA)"),
    #     db.reverse_item_serial("TTW(BQAAAAAH74C6KgbBh4oEEHAeDHfLwUjmnIuluViag1GgnDSDgQAAAAAAAA==)"),
    #     db.reverse_item_serial("TTW(BQAAAACZY4A6AQXBh4oEEHAeDHfLoTXmnIslFueaI9FEFjWDgQAAAAAAAA==)"),
    #     db.reverse_item_serial("TTW(BQAAAAD37YC6AwXBh4oMMJCeCn2rQTZPWGFFFlmcFJERFjWDgQAAAAAAAA==)"),
    #     db.reverse_item_serial("TTW(BQAAAADVOoA6AQXBh4oMMHCeC33DobVR8lOllVZaKVHEEDWDgQAAAAAAAA==)"),
    #     db.reverse_item_serial("TTW(BQAAAABK1YC6Kwbhh5oMMJCeCj+o4UhPZJGFFSdZUUmjr3IKSDMYCAAAAAAA)"),
    #     db.reverse_item_serial("TTW(BQAAAABmvoC6KgbBh4oMMJCeCn2rwUhPnJRFFlmcFHFFEDWDgQAAAAAIAA==)"),
    # ]
    items = [
        db.reverse_item_serial("TTW(BQAAAACKJIA7LAbhh4oMGFAeCnWzQclRYrkvllBaGskYzaaDgQAAAAAY)"),
    ]

    for item in items:
        balance = item.balance
        all_parts = db.get_parts(item.balance_short)
        if not all_parts:
            print("--- No data about {}".format(item.balance_short))
            continue
        is_legit = db.is_legit(item)
        if not is_legit:
            print("--------------------------------> {} is not legit <--------------------------------".format(item.balance_short))

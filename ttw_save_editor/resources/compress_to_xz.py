import json
import lzma

if __name__ == '__main__':
    balance_name_mapping = "balance_name_mapping.json"
    balance_name_json = None
    output_balance_name_mapping = "balance_name_mapping.json.xz"

    balance_to_inv_key = "balance_to_inv_key.json"
    balance_to_inv_json = None
    output_balance_to_inv_key = "balance_to_inv_key.json.xz"

    with open(balance_name_mapping, 'r') as file:
        balance_name_json = json.load(file)

    # Output to compressed JSON
    with lzma.open(output_balance_name_mapping, 'wt') as odf:
        json.dump(balance_name_json, odf, separators=(',', ':'))

    with open(balance_to_inv_key, 'r') as file:
        balance_to_inv_json = json.load(file)

    # Output to compressed JSON
    with lzma.open(output_balance_to_inv_key, 'wt') as odf:
        json.dump(balance_to_inv_json, odf, separators=(',', ':'))

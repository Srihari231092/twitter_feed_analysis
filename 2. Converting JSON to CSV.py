import os
import pandas as pd
import json


def main():
    print(os.getcwd())
    fpath = os.path.join(os.getcwd(), "all_uni_data.json")
    all_uni_data = pd.read_json(fpath, lines=True)
    all_uni_data.to_csv(os.path.join(os.getcwd(), "all_uni_data.csv"))


if __name__ == "__main__":
    main()

from pathlib import Path
import tomllib

import pandas as pd


env_file = '.env_file'

def envfile():
    return Path(env_file)


def filename():
    with open(envfile(), "rb") as file:
        data = tomllib.load(file)
    return Path(data["file"]).expanduser()

def zipfilename():
    with open(envfile(), "rb") as file:
        data = tomllib.load(file)
    return Path(data["zipfile"]).expanduser()

def csvfile():
    with open(envfile(), "rb") as file:
        data = tomllib.load(file)
    return data["csvfile"]


def read_df():
    return pd.read_csv(filename())

def read_df_zip():
    import zipfile
    with zipfile.ZipFile(zipfilename()) as zipf:
        with zipf.open(csvfile()) as csv:
            df = pd.read_csv(csv)
            return df

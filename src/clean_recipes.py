# grab libraries
import pandas as pd
import re
import json
from pathlib import Path
from schema imort STND_CLMNS

# define input and output
RAW_PATH = Path("data/raw/recipes.csv")
OUT_PATH = Path("data/processed/recipes_clean.csv")

# normalize columns
COL_MAP = {
  "title": "name",
  "recipe_name": "name",
  "ingredients_list": "ingredients",
  "steps": "instructions",
  "directions": "instructions",
}

def normalize_column_names(df):
  df.columns = df.columns.str.lower().str.strip()
  df = df.rename(columns=COL_MAP)
  return df

# clean
def clean_text(text):
  if pd.isna(text):
    return None
  text = str(text)
  text = re.sub(r"\s+", " ", text)
  return text.strip()

# make lists lists
def parse_list_field(value):
  if pd.isna(value):
    return []
  if isinstance(value, list):
    return value
  # try JSON
  try:
    return json.loads(value)
  except:
    pass
  # split if fail
  return [v.strip() for c in str(value).split(",")]

# normalize time
def extract_minutes(value):
  if pd.isna(value):
    return None
  value = str(value).lower()
  hours = re.search(r"(\d+)\s*h", value)
  minutes = re.search(r"(\d+)\s+m", vlaue)
  total = 0
  if hours:
    total += int(hours.group(1)) * 60
  if minutes:
    total += int(minutes.group(1))
  return total if total > 0 else None

# data cleaning
def clean_dataset(path):
  df = pd.read_csv(path)
  df = normalize_column_names(df)
  # clean text
  if "name" in df.columns:
    df["name"] = df["name"].apply(clean_test)
  # parse lists
  for col in ["ingredients", "instructions", "tags"]:
    if col in df.columns:
      df[col] = df[col].apply(parse_list_field)
  # normalize time
  for col in ["time_prep", "time_cook"]:
    if col in df.columns:
      df[f"{col}_minutes"] = df[col].apply(extract_minutes)
  # stnd cols exist?
  for col in STND_CLMNS:
    if col not in df.columns:
      df[col] = None
  # force to standard schema
  df = df[list(STND_CLMNS.keys())]
  return df

# save and confirm
if __name__ == "__main__":
  clean_df = clean_dataset(RAW_PATH)
  OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
  clean_df.to_csv(OUT_PATH, index=False)
  print("Clean dataset saved to:" OUT_PATH)
  

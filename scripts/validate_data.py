from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
raw = pd.read_csv(ROOT / 'Diwali_Sales_Data.csv', encoding='unicode_escape')
expected = {'User_ID', 'Cust_name', 'Product_ID', 'Gender', 'Age Group', 'Age', 'Marital_Status', 'State', 'Zone', 'Occupation', 'Product_Category', 'Orders', 'Amount', 'Status', 'unnamed1'}
assert set(raw.columns) == expected, f'Unexpected columns: {set(raw.columns) - expected}'
assert len(raw) == 11251, f'Unexpected raw row count: {len(raw)}'
assert int(raw.duplicated().sum()) == 8, f'Unexpected duplicate count: {int(raw.duplicated().sum())}'
assert int(raw.isna().sum().sum()) == 22514, f'Unexpected missing-cell count: {int(raw.isna().sum().sum())}'
clean = raw.drop(columns=['Status', 'unnamed1']).dropna().copy()
clean['Amount'] = pd.to_numeric(clean['Amount'], errors='coerce').astype(int)
assert len(clean) == 11239, f'Unexpected clean row count: {len(clean)}'
assert clean['Amount'].notna().all(), 'Amount contains non-numeric values.'
assert (clean['Amount'] >= 0).all(), 'Amount contains negative values.'
assert int(clean['Amount'].sum()) == 106249129, f'Unexpected clean amount: {int(clean["Amount"].sum())}'
print('Diwali validation passed')
print(f'raw_rows={len(raw)} clean_rows={len(clean)} clean_amount={int(clean["Amount"].sum())}')

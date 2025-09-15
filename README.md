# 📊 Pandas Learning Repository

This repository contains my learning notes and practice code for **Pandas**, a Python library for data analysis and manipulation.

---

## 🔹 What is Pandas?
[Pandas](https://pandas.pydata.org/) is a powerful open-source library built on top of NumPy. It provides easy-to-use data structures and tools for working with structured (tabular) data.

- **Series** → One-dimensional labeled array (like a single column in Excel).
- **DataFrame** → Two-dimensional labeled data structure with rows & columns (like a spreadsheet or SQL table).

---

## 📂 Repository Structure
- **main.py** → All practice code (Series, DataFrames, filtering, aggregation, cleaning, etc.)
- **data.csv** → Sample dataset for practice.
- **pokemon.json** → Pokémon dataset used for JSON reading examples.

---

## 📝 Topics Covered

### 1. Series
- Creating a Series from lists, dicts, arrays.
- Using `.loc` (label-based) and `.iloc` (position-based) indexing.
- Filtering values with conditions.
- Updating values in a Series.

### 2. DataFrame
- Creating DataFrames from dictionaries.
- Adding rows and columns dynamically.
- Reading external files (`.csv`, `.json`).
- Selecting rows & columns using:
  - `df["col"]`
  - `df.loc[]` (label-based selection)
  - `df.iloc[]` (position-based selection)

### 3. Selection
- Selecting single/multiple columns.
- Selecting rows by index/labels.
- Slicing DataFrames (inclusive for `loc`, exclusive for `iloc`).
- Exercises with Pokémon dataset.

### 4. Filtering
- Applying conditions on DataFrames.
- Examples: filtering tall Pokémon, legendary Pokémon, or type-based Pokémon.

### 5. Aggregation
- Using aggregation functions: `mean()`, `sum()`, `min()`, `max()`, `count()`.
- Column-wise and row-wise aggregation.
- Grouping with `groupby()`.

### 6. Data Cleaning
Steps followed:
1. **Drop irrelevant columns** → `df.drop(columns=[])`
2. **Handle missing values** → `dropna()`, `fillna()`
3. **Fix inconsistent values** → `replace()`
4. **Standardize text** → `.str.lower()`, `.str.upper()`
5. **Fix data types** → `astype()`
6. **Remove duplicates** → `drop_duplicates()`

---

## ▶️ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/Ayushkr77/pandas.git

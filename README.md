# Diwali Sales Analysis

A Python exploratory analysis of **11,251 retail orders** used to understand customer behavior, regional demand, and product-category opportunities during the Diwali sales period.

> **Portfolio focus:** data cleaning, exploratory analysis, customer segmentation, regional comparison, and retail recommendations.

## Business objective

Retail teams need to understand who buys, where demand is concentrated, and which categories deserve attention during seasonal campaigns. This project converts transaction-level sales data into customer and product insights.

## Dataset and quality

The dataset contains 11,251 rows and 15 columns. It includes 8 duplicate rows, 12 missing Amount values, and fully empty Status and unnamed1 fields. The notebook removes unused fields, handles missing values, checks duplicates, and prepares the data for grouped comparisons.

## Visual evidence

![Top product categories by order count](images/diwali_top_categories.png)

## Verified descriptive findings

Female customers account for 7,842 of 11,251 orders. The 26–35 age group is the largest observed segment with 4,543 orders. Uttar Pradesh, Maharashtra, and Karnataka are the three largest observed states by order count. Clothing and Apparel, Food, and Electronics and Gadgets are the three largest observed product categories by order count.

These are descriptive order-volume findings. They should not be interpreted as causal explanations of customer behavior without additional spend, margin, or experimental analysis.

## Analytical workflow

The notebook inspects the dataset schema, missing values, duplicates, and unused columns; cleans field names and prepares categorical and numeric fields; compares orders and sales patterns across gender, age group, state, occupation, and product category; visualizes segment differences; and translates the strongest observed patterns into campaign and assortment questions.

## Business recommendations

Prioritize the 26–35 segment in seasonal campaign testing while comparing conversion and average order value rather than relying on order count alone. Use state-level demand patterns to guide regional inventory and targeted promotions. Compare category performance using revenue and margin in addition to order volume before making assortment decisions. Preserve a documented data-quality checklist so blank fields and duplicate rows do not distort comparisons.

## Tools and repository contents

Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook

The repository contains Diwali_Sales_Data.csv, Diwali_Sales_Analysis.ipynb, and the verified chart preview at images/diwali_top_categories.png.

## Run locally

Clone the repository, install pandas, numpy, matplotlib, seaborn, and jupyter, and open Diwali_Sales_Analysis.ipynb in Jupyter Notebook.

## Limitations and next steps

The project is descriptive EDA. A stronger decision model would add profit or margin, average order value, cohort comparisons, statistical uncertainty, and a clearly defined campaign outcome. The next extension would be customer segmentation or an A/B-test design for seasonal targeting.

---

*Part of Mayank Srivastava's Data Analyst portfolio.*

import pandas as pd
import logging
import matplotlib.pyplot as plt
from extraxt import extract_csv


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='transform.log',
    filemode='a'
)


# 📥 Step 1: Extract CSV
df = extract_csv()


# 🧠 Transformation Tasks


# 🔧 Step 2: Transform class
# class Transform:
#     def __init__(self, df):
#         self.df = df
# # 🧩 1. Outlier Handling
# # Goal: Cap extreme values that could skew analysis or modeling.
#     def outlier_handling(self):
#         for col in ['rev_util', 'monthly_inc', 'debt_ratio', 'late_30_59', 'late_60_89', 'late_90']:
#             cap = self.df[col].quantile(0.99)
#             self.df[col] = self.df[col].clip(upper=cap)
#         return self.df

# # Plot histograms for rev_util, monthly_inc, debt_ratio, late_30_59, late_60_89, late_90
#     def histogram(self):
#         cols = ['rev_util', 'monthly_inc', 'debt_ratio', 'late_30_59', 'late_60_89', 'late_90']
#         self.df[cols].hist(figsize=(12, 10), bins=30)
#         plt.suptitle("Histograms of Key Features (After Outlier Handling)")
#         plt.tight_layout()
#         plt.show()



#     # print(plot_df)
# #Cap values at 99th percentile using df[col] = df[col].clip(upper=cap)

# # 🧱 2. Feature Engineering

# # Goal: Derive useful new columns.

# # total_late = late_30_59 + late_60_89 + late_90
#     def total_late(self):
#         self.df['total_late'] = (
#             self.df['late_30_59'] + self.df['late_60_89'] + self.df['late_90']
#         )


# # credit_burden = debt_ratio × monthly_inc

#     def credit_burden(self):
#         self.df['credit_burden'] = self.df['debt_ratio'] * self.df['monthly_inc']
#         return self.df
    
# #     high_risk = 1 if dlq_2yrs > 0 else 0
#     def high_risk(self):
#         self.df['high_risk'] = self.df['dlq_2yrs'] > 0
#         # If you want string 'True'/'False' instead of boolean True/False, do:
#         self.df['high_risk'] = self.df['dlq_2yrs'].apply(lambda x: 'True' if x > 0 else 'False')
#         return self.df
# # 📊 3. Binning / Bucketing

# # Goal: Convert numeric into categorical features.

# # Bin age into age groups: 20s, 30s, 40s, etc.
#     def age_binning(self):
#     # Bin age into fixed bins (20s, 30s, 40s, ...)
#         bins = [0, 29, 39, 49, 59, 69, 100]  # age ranges
#         labels = ['20s', '30s', '40s', '50s', '60s', '70+']  # labels for bins
#         self.df['age_group'] = pd.cut(self.df['age'], bins=bins, labels=labels, right=True)
#         return self.df
# #     Use pd.qcut to bucket monthly_inc into Low, Mid, High, Very High

#     def monthly_inc_binning(self):
#         # Bucket monthly_inc into 4 quantiles: Low, Mid, High, Very High
#         labels = ['Low', 'Mid', 'High', 'Very High']
#         self.df['monthly_inc_group'] = pd.qcut(self.df['monthly_inc'], q=4, labels=labels)
#         return self.df

class Transform:
    def __init__(self, df):
        self.df = df

    def outlier_handling(self):
        for col in ['rev_util', 'monthly_inc', 'debt_ratio', 'late_30_59', 'late_60_89', 'late_90']:
            cap = self.df[col].quantile(0.99)
            self.df[col] = self.df[col].clip(upper=cap)
        return self  # return self, not self.df

    def total_late(self):
        self.df['total_late'] = (
            self.df['late_30_59'] + self.df['late_60_89'] + self.df['late_90']
        )
        return self

    def credit_burden(self):
        self.df['credit_burden'] = self.df['debt_ratio'] * self.df['monthly_inc']
        return self

    def high_risk(self):
        self.df['high_risk'] = self.df['dlq_2yrs'].apply(lambda x: 'True' if x > 0 else 'False')
        return self

    def get_df(self):
        return self.df



# ⚖️ 4. Normalization

# Goal: Scale features for ML.

#     Apply MinMaxScaler to:

#         rev_util

#         monthly_inc

#         debt_ratio

# 📌 5. Handling Special Values

# Goal: Identify anomalies in logically important columns.

# Count rows where monthly_inc is 0

#     Decide: Keep, replace with median, or create a binary flag column like is_income_zero

# 🧼 6. Column Cleaning

# Goal: Drop or rename unnecessary columns (for ML or analysis).

# Drop individual late columns if using total_late

# Rename open_credit to num_open_credit_lines (for clarity, optional)


# 🚀 Step 3: Run
if __name__ == '__main__':
    transformer = Transform(df)
    cleaned_df = (
    transformer
    .outlier_handling()
    .total_late()
    .credit_burden()
    .high_risk()
)
    
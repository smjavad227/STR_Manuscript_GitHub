import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

print("📊 شروع تحلیل تکاملی...")

# 1. خواندن داده‌های conserved motifs
conserved_df = pd.read_csv('results/evolutionary_conservation_analysis/tables/conserved_motifs.csv')
print(f"✅ تعداد موتیف‌های حفاظت‌شده: {len(conserved_df)}")
print(f"🔢 ستون‌های موجود: {list(conserved_df.columns)}")

# 2. خواندن forbidden motifs candidates
forbidden_candidates_df = pd.read_csv('results/evolutionary_conservation_analysis/tables/forbidden_motifs_candidates.csv') 
print(f"\n✅ تعداد forbidden motifs candidates: {len(forbidden_candidates_df)}")
print("\nنمونه‌ای از داده‌ها:")
print(forbidden_candidates_df.head(10))

# 3. افزودن ستون contains_CG
conserved_df['contains_CG'] = conserved_df['motif'].str.contains('CG')
forbidden_candidates_df['contains_CG'] = forbidden_candidates_df['motif'].str.contains('CG')

# 4. تحلیل conservation برای CG vs non-CG motifs
print("\n📊 **تحلیل Conservation Scores:**")
print("="*50)

# الف) در conserved motifs
cg_conserved = conserved_df[conserved_df['contains_CG']]['conservation_score']
non_cg_conserved = conserved_df[~conserved_df['contains_CG']]['conservation_score']

print(f"🔬 **Conserved Motifs:**")
print(f"   CG motifs: {len(cg_conserved)} موتیف، میانگین conservation: {cg_conserved.mean():.3f}")
print(f"   Non-CG motifs: {len(non
_cg_conserved)} موتیف، میانگین conservation: {non_cg_conserved.mean():.3f}")

# ب) در forbidden candidates
cg_forbidden = forbidden_candidates_df[forbidden_candidates_df['contains_CG']]['conservation_score']
non_cg_forbidden = forbidden_candidates_df[~forbidden_candidates_df['contains_CG']]['conservation_score']

print(f"\n🚫 **Forbidden Candidates:**")
print(f"   CG motifs: {len(cg_forbidden)} موتیف")
print(f"   Non-CG motifs: {len(non_cg_forbidden)} موتیف")

# 5. بررسی Top Forbidden Candidates
print("\n🎯 **Forbidden Candidates از تحلیل تکاملی:**")
for i, row in forbidden_candidates_df.iterrows():
    cg_status = "✅ CG" if row['contains_CG'] else "❌ Non-CG"
    print(f"{i+1}. {row['motif']} (طول: {row['length']}bp) - Conservation: {row['conservation_score']:.3f} - {cg_status}")

print("\n✅ تحلیل اولیه کامل شد!")

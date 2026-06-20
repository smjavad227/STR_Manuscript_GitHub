#!/usr/bin/env python3
"""
STR Data Analyzer for XCI_STR Project
"""

import os
import pandas as pd
import glob
import numpy as np
from pathlib import Path
import re

def parse_trf_dat_file(dat_file):
    """Parse TRF .dat file and extract STR information"""
    data = []
    try:
        with open(dat_file, 'r') as f:
            lines = f.readlines()
        
        # Skip header lines (first 15 lines)
        for i, line in enumerate(lines[15:], start=16):
            line = line.strip()
            if not line:
                continue
                
            # Split by whitespace
            parts = re.split(r'\s+', line)
            if len(parts) >= 15:
                try:
                    # Extract chromosome name from filename
                    filename = Path(dat_file).name
                    chrom_match = re.search(r'chr[0-9XY]+', filename, re.IGNORECASE)
                    chrom = chrom_match.group() if chrom_match else filename
                    
                    entry = {
                        'chromosome': chrom,
                        'start': int(parts[0]),
                        'end': int(parts[1]),
                        'period': int(parts[2]),
                        'copies': float(parts[3]),
                        'consensus_size': int(parts[4]),
                        'percent_matches': float(parts[5]),
                        'percent_indels': float(parts[6]),
                        'score': int(parts[7]),
                        'entropy': float(parts[8]),
                        'repeat_pattern': parts[14] if len(parts) > 14 else '',
                        'source_file': filename
                    }
                    data.append(entry)
                except (ValueError, IndexError) as e:
                    print(f"  Warning: Error parsing line {i}: {e}")
                    continue
    except Exception as e:
        print(f"  Error reading {dat_file}: {e}")
    
    return data

def main():
    print("="*60)
    print("STR Data Analysis for XCI_STR Project")
    print("="*60)
    
    # Look for .dat files in multiple locations
    dat_locations = [
        '.',  # Current directory
        'results/',
        'results/chr1/',
        'results/chr8/', 
        'results/chr19/',
        'results/chr21/',
        'results/phase1_trf/'
    ]
    
    all_dat_files = []
    for location in dat_locations:
        if os.path.exists(location):
            dat_files = glob.glob(os.path.join(location, '*.dat'))
            if dat_files:
                print(f"Found {len(dat_files)} .dat files in {location}")
                all_dat_files.extend(dat_files)
    
    if not all_dat_files:
        print("\n❌ ERROR: No .dat files found!")
        print("Looking in: " + ", ".join(dat_locations))
        return
    
    print(f"\n✅ Total .dat files found: {len(all_dat_files)}")
    
    # Create analysis_results directory
    os.makedirs('analysis_results', exist_ok=True)
    
    # Process all .dat files
    all_data = []
    processed_files = 0
    
    for dat_file in all_dat_files:
        filename = os.path.basename(dat_file)
        print(f"Processing {filename}...", end='')
        
        data = parse_trf_dat_file(dat_file)
        if data:
            all_data.extend(data)
            processed_files += 1
            print(f" ✓ ({len(data)} STRs)")
        else:
            print(" ✗ (no data or error)")
    
    if not all_data:
        print("\n❌ No data extracted from any .dat file!")
        return
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    print(f"\n✅ Successfully extracted {len(df)} STR regions from {processed_files} files")
    
    # Calculate additional metrics
    df['length'] = df['end'] - df['start'] + 1
    df['copy_number'] = df['copies']
    df['period_length'] = df['period']
    
    # Save all data
    output_file = 'analysis_results/all_str_data.csv'
    df.to_csv(output_file, index=False)
    print(f"📁 Saved all data to {output_file}")
    
    # 1. Basic statistics per chromosome
    print("\n" + "="*60)
    print("1. BASIC STATISTICS PER CHROMOSOME")
    print("="*60)
    
    if 'chromosome' in df.columns:
        # Group by chromosome
        chromosomes = sorted(df['chromosome'].unique())
        print(f"Chromosomes found: {', '.join(chromosomes)}")
        
        basic_stats = df.groupby('chromosome').agg({
            'length': ['count', 'mean', 'std', 'min', 'max', 'median'],
            'period': ['mean', 'std'],
            'copies': ['mean', 'std'],
            'score': ['mean', 'std'],
            'entropy': ['mean', 'std']
        }).round(3)
        
        # Flatten column names
        basic_stats.columns = ['_'.join(col).strip() for col in basic_stats.columns.values]
        basic_stats = basic_stats.reset_index()
        
        basic_stats_file = 'analysis_results/basic_statistics.csv'
        basic_stats.to_csv(basic_stats_file, index=False)
        print(f"📁 Saved basic statistics to {basic_stats_file}")
        
        # Print summary
        print("\nSummary by chromosome:")
        print("-" * 80)
        print(f"{'Chrom':<10} {'Count':<8} {'Mean Length':<12} {'Mean Period':<12} {'Mean Copies':<12}")
        print("-" * 80)
        for idx, row in basic_stats.iterrows():
            chrom = row['chromosome']
            count = row['length_count']
            mean_len = row['length_mean']
            mean_period = row['period_mean']
            mean_copies = row['copies_mean']
            print(f"{chrom:<10} {count:<8} {mean_len:<12.1f} {mean_period:<12.1f} {mean_copies:<12.2f}")
    
    # 2. Compare X chromosome with autosomes
    print("\n" + "="*60)
    print("2. X CHROMOSOME vs AUTOSOMES COMPARISON")
    print("="*60)
    
    # Identify X chromosome and autosomes
    x_chroms = [c for c in df['chromosome'].unique() if 'X' in str(c).upper()]
    autosomes = [c for c in df['chromosome'].unique() if c not in x_chroms and re.match(r'chr\d+', str(c), re.IGNORECASE)]
    
    if x_chroms and autosomes:
        print(f"X chromosome(s): {', '.join(x_chroms)}")
        print(f"Autosomes: {', '.join(autosomes)}")
        
        x_data = df[df['chromosome'].isin(x_chroms)]
        auto_data = df[df['chromosome'].isin(autosomes)]
        
        print(f"\nX chromosome STRs: {len(x_data):,}")
        print(f"Autosome STRs: {len(auto_data):,}")
        
        # Create comparison table
        comparison_data = []
        metrics = ['length', 'period', 'copies', 'score', 'entropy']
        
        for metric in metrics:
            x_mean = x_data[metric].mean()
            x_std = x_data[metric].std()
            auto_mean = auto_data[metric].mean()
            auto_std = auto_data[metric].std()
            
            # Calculate fold change
            if auto_mean != 0:
                fold_change = x_mean / auto_mean
            else:
                fold_change = np.nan
            
            comparison_data.append({
                'metric': metric,
                'x_mean': x_mean,
                'x_std': x_std,
                'auto_mean': auto_mean,
                'auto_std': auto_std,
                'fold_change': fold_change,
                'percent_difference': ((x_mean - auto_mean) / auto_mean * 100) if auto_mean != 0 else np.nan
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        comparison_file = 'analysis_results/x_vs_autosomes_comparison.csv'
        comparison_df.to_csv(comparison_file, index=False)
        print(f"\n📁 Saved comparison to {comparison_file}")
        
        # Print comparison
        print("\nComparison (X vs Autosomes):")
        print("-" * 80)
        print(f"{'Metric':<15} {'X Mean':<12} {'Auto Mean':<12} {'Fold Change':<12} {'% Diff':<10}")
        print("-" * 80)
        for idx, row in comparison_df.iterrows():
            metric = row['metric']
            x_mean = row['x_mean']
            auto_mean = row['auto_mean']
            fold_change = row['fold_change']
            percent_diff = row['percent_difference']
            
            print(f"{metric:<15} {x_mean:<12.3f} {auto_mean:<12.3f} {fold_change:<12.3f} {percent_diff:<10.1f}")
    
    # 3. Additional analyses
    print("\n" + "="*60)
    print("3. ADDITIONAL ANALYSES")
    print("="*60)
    
    # Period distribution
    period_counts = df['period'].value_counts().sort_index()
    period_file = 'analysis_results/period_distribution.csv'
    period_counts.to_csv(period_file)
    print(f"📁 Period distribution saved to {period_file}")
    
    # Top repeat patterns
    top_patterns = df['repeat_pattern'].value_counts().head(20)
    patterns_file = 'analysis_results/top_repeat_patterns.csv'
    top_patterns.to_csv(patterns_file)
    print(f"📁 Top repeat patterns saved to {patterns_file}")
    
    # Create summary report
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print(f"\n📊 Total STR regions analyzed: {len(df):,}")
    print(f"📁 Results saved in 'analysis_results/' directory:")
    print("   - all_str_data.csv (all extracted STR data)")
    print("   - basic_statistics.csv (statistics per chromosome)")
    print("   - x_vs_autosomes_comparison.csv (X vs autosomes comparison)")
    print("   - period_distribution.csv (distribution of repeat periods)")
    print("   - top_repeat_patterns.csv (most common repeat patterns)")
    
    # Quick statistical test
    if x_chroms and autosomes and len(x_data) > 5 and len(auto_data) > 5:
        from scipy import stats
        
        print("\n📈 Statistical tests (X vs Autosomes):")
        print("-" * 40)
        
        for metric in ['length', 'copies', 'score']:
            try:
                t_stat, p_value = stats.ttest_ind(
                    x_data[metric].dropna(),
                    auto_data[metric].dropna(),
                    equal_var=False
                )
                
                significance = ""
                if p_value < 0.001:
                    significance = "***"
                elif p_value < 0.01:
                    significance = "**"
                elif p_value < 0.05:
                    significance = "*"
                
                print(f"{metric:<15} t={t_stat:.3f}, p={p_value:.4f} {significance}")
            except:
                pass

if __name__ == "__main__":
    main()

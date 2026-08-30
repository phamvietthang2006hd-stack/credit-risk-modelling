import pandas as pd
import matplotlib.pyplot as plt

def nan_plot_values_count(df: pd.DataFrame, dataset: str, threshold: float = 50.0):
    nan_df = pd.DataFrame({
        'column': df.columns,
        'missing_count': df.isna().sum().to_numpy()
    })

    nan_df['missing_rate'] = nan_df['missing_count'] / len(df) * 100  
    nan_df = nan_df[nan_df['missing_count'] > 0].sort_values('missing_rate', ascending=False).reset_index(drop=True)

    height = max(6, len(nan_df) * 0.15)
    _, ax = plt.subplots(figsize=(14, height))

    colors = plt.cm.Blues(nan_df['missing_rate'] / nan_df['missing_rate'].max())
    ax.bar(nan_df['column'], nan_df['missing_rate'], color=colors)

    ax.set_xlabel('Columns', fontsize=12)
    ax.set_ylabel('Missing rate (%)', fontsize=12)
    ax.set_title(f'Missing Rate by Column of Dataset {dataset}', fontsize=15, fontweight='bold')
    
    ax.tick_params(axis='x', labelsize=9, rotation=90)
    ax.tick_params(axis='y', labelsize=10)
    ax.axhline(y=threshold, linestyle='--', color='red')
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    
    ax.set_axisbelow(True)    
    plt.tight_layout()
    plt.show()
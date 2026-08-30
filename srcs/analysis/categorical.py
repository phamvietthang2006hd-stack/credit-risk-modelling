import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def categorical_data_analyzer(
        df: pd.DataFrame,
        dataset: str,
        column: str,
        target: str = 'TARGET',
):

    # Assert 
    assert column in df.columns, f"{column} is not in {dataset}"

    # Summary Dataframe
    summary = df.groupby(column)[target].agg(
        Total_count='count',
        Default_count='sum',
        Rate='mean'
    ).reset_index()

    summary['Rate'] = np.round(summary['Rate'] * 100, 2)

    # Statical 
    print('-' * 100)
    print(summary)
    print('-' * 100)

    height = max(4, len(summary) * 0.5)
    fig, ax = plt.subplots(1,2, figsize=(20,height))

    # CDF for quantity of each category
    cate_quant = summary.sort_values(by='Total_count', ascending=True).reset_index(drop=True)
    colors = plt.cm.tab20(np.linspace(0, 1, len(cate_quant)))
    bars = ax[0].barh(cate_quant[column], cate_quant['Total_count'], color=colors)
    ax[0].set_title(f"Total Count", fontsize=11, fontweight='bold')
    ax[0].set_xlabel("Quantity", fontsize=9)
    ax[0].set_ylabel("Category", fontsize=9)
    ax[0].bar_label(bars, padding=3, fontsize=7)

    # CDF for rate of default per category
    default_rate = summary.sort_values(by='Rate', ascending=True).reset_index(drop=True)
    colors_rate = plt.cm.tab20(np.linspace(0, 1, len(default_rate)))
    bars = ax[1].barh(default_rate[column], default_rate['Rate'], color=colors_rate)
    ax[1].set_title(f"rate", fontsize=11, fontweight='bold')
    ax[1].set_xlabel('Rate (%)', fontsize=9)
    ax[1].set_ylabel('Category', fontsize=9)
    ax[1].bar_label(bars, labels=[f"{x:.1f}" for x in default_rate['Rate']], padding=3, fontsize=7)

    fig.suptitle(f"{dataset}: {column}", fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()
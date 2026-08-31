import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def numerical_data_analyzer(
        df: pd.DataFrame, 
        dataset: str, 
        column: str,
        target: str = 'TARGET', 
        percentiles: list[float] = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99],
    ):
    assert column in df.columns, f"Column {column} is not in {dataset}"
    data = df.copy()
    # Percentiles
    print('-' * 100)
    print(data[column].describe(percentiles=percentiles))
    print('-' * 100)
    
    fig, ax = plt.subplots(1, 3, figsize=(13, 8))

    # Violin plot
    sns.violinplot(data=data, x=target, y=column, ax=ax[0], linewidth=1, legend=False)
    ax[0].set_title('Violin plot', fontsize=11, fontweight='bold')
    ax[0].set_xlabel(target, fontsize=9)
    ax[1].set_ylabel(column, fontsize=9)

    # Box plot
    sns.boxplot(data=data,x=target, y=column, ax=ax[1], linewidth=1, legend=False)
    ax[1].set_title('Box_plot', fontsize=11, fontweight='bold')
    ax[1].set_xlabel(target, fontsize=9)
    ax[1].set_ylabel(column, fontsize=9)

    # Dist plot
    sns.kdeplot(data=data[data[target] == 0], x=column, label='Non-defaulter', color='black', ax=ax[2])
    sns.kdeplot(data=data[data[target] == 1], x=column, label='Defaulter', color='red', ax=ax[2])
    ax[2].set_title('PDF', fontsize=11, fontweight='bold')
    ax[2].set_xlabel('Density', fontsize=9)
    ax[2].set_ylabel(column, fontsize=9)
    ax[2].legend()

    fig.suptitle(f"{dataset}: {column}", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()
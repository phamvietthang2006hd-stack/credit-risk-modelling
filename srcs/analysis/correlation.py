import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from phik.phik import phik_matrix
from typing import Optional
import numpy as np


class CorrelationAnalyzer:
    """
    Correlation analysis utility.
    - Pearson correlation for numerical features.
    - Phi-K correlation for categorical features.
    - Top features correlated with TARGET.
    - Heatmap visualization.
    """

    def __init__(self,df: pd.DataFrame, target: str = "TARGET"):
        self.df = df.copy()
        self.target = target
        self.pearson_matrix: Optional[pd.DataFrame] = None
        self.phik_matrix: Optional[pd.DataFrame] = None

    def pearson_corr(self, columns: Optional[list[str]] = None) -> pd.DataFrame:

        if columns is None:
            columns = self.df.select_dtypes(include="number").columns.tolist()
        self.pearson_matrix = self.df[columns].corr(method="pearson")

        return self.pearson_matrix

    def phi_k_corr(self, columns: Optional[list[str]] = None) -> pd.DataFrame:
        if columns is None:
            columns = self.df.columns.tolist()
        else:
            columns = columns.copy()

        if self.target in self.df.columns and self.target not in columns:
            columns.append(self.target)

        num_cols = self.df[columns].select_dtypes(include=["number"]).columns.difference([self.target]).tolist()

        self.phik_matrix = phik_matrix(self.df[columns],interval_cols=num_cols)

        return self.phik_matrix
    
    def top_target_phi_k(self, top_n: int = 10, columns: Optional[list[str]] = None) -> pd.Series:
    
        self.phik_matrix = self.phi_k_corr(columns=columns)

        assert self.phik_matrix is not None, "phik_matrix is not initialized"

        target_corr = self.phik_matrix[self.target].drop(self.target).sort_values(ascending=False)

        return target_corr.head(top_n)

    @staticmethod
    def plot_heatmap(
        corr_matrix: pd.DataFrame,
        title: str,
        figsize: tuple[int, int] = (12, 10),
        cmap: str = "Blues",
        x_rotation: int = 90
    ):

        plt.figure(figsize=figsize)
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, vmin=-1, vmax=1, center=0, cmap=cmap,mask = mask, cbar=True, linewidths=0.5, linecolor="white", linewidth=0.5)
        plt.xticks(rotation=x_rotation, ha="right", fontsize=9)
        plt.yticks(rotation=0, fontsize=9)
        plt.title(title, fontsize=14, fontweight="bold", pad=15)
        plt.tight_layout()
        plt.show()
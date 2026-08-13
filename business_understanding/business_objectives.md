# Business Objectives

## 1. Business Context

Home Credit operates in the consumer lending sector, where the fundamental business problem is to extend credit to customers who are capable of repaying their loans while controlling the financial losses arising from customers who experience payment difficulties.

The `Home Credit Default Risk` dataset is explicitly constructed around this problem. The competition asks participants to predict how capable an applicant is of repaying a loan. The primary application table contains one record per loan application, while additional tables contain information about the applicant's previous applications, credit bureau history, installment payments, credit-card balances, and cash-loan balances.

The business problem is therefore not simply a generic binary-classification problem. It is a **credit risk assessment problem** in which information available around the loan application is used to estimate the probability that the applicant will subsequently experience payment difficulties.

---

## 2. Primary Business Objective

The primary business objective of this project is:

> **Develop an interpretable credit risk scorecard that estimates the probability that a loan applicant will experience payment difficulties after receiving a loan, enabling the lender to distinguish relatively low-risk applicants from high-risk applicants and support more informed credit decisions.**

Formally, for an applicant $i$, the model estimates:

$$
P(Y_i = 1 \mid X_i)
$$

where:

- $X_i$ represents information available about applicant $i$ at or before the credit decision point.
- $Y_i = 1$ represents the occurrence of the defined adverse repayment outcome.
- $P(Y_i = 1 \mid X_i)$ represents the estimated probability of payment difficulties.

In the Home Credit dataset, the primary target variable is `TARGET`:

$$
TARGET =
\begin{cases}
1, & \text{client has payment difficulties} \\
0, & \text{otherwise}
\end{cases}
$$

The dataset therefore provides a directly observable historical outcome that can be used to construct a supervised credit-risk model. citeturn0search12

---

## 3. Business Problem to Be Solved

The project addresses the following operational decision problem:

$$
\text{Applicant Information}
\rightarrow
\text{Risk Estimation}
\rightarrow
\text{Risk Classification / Score}
\rightarrow
\text{Credit Decision Support}
$$

The model is intended to answer:

> **Given the information available about an applicant at the time of credit assessment, how likely is this applicant to experience payment difficulties?**

This probability can subsequently support different credit policies, such as:

- approving relatively low-risk applicants;
- subjecting higher-risk applicants to additional assessment;
- reducing the amount of credit offered to high-risk applicants;
- applying differentiated pricing where appropriate;
- rejecting applications whose estimated risk exceeds an established risk appetite.

These actions are consistent with the broader business objective associated with the Home Credit problem: identifying applicants likely to have difficulty paying installments so that lending decisions can be adjusted according to risk. citeturn0search13

The project itself does **not** attempt to reproduce Home Credit's actual proprietary underwriting policy. The dataset does not provide sufficient information to reconstruct the complete real-world decision process. Instead, the project develops a standalone analytical credit-risk scorecard based on the information contained in the publicly available dataset.

---

## 4. Business Objectives Derived from the Dataset

### 4.1 Estimate Applicant-Level Probability of Payment Difficulty

The first objective is to estimate an applicant's probability of experiencing payment difficulties.

The model should produce a continuous risk estimate:

$$
\hat{p}_i = P(TARGET_i = 1 \mid X_i)
$$

rather than only a hard binary decision.

This is important because credit risk is fundamentally continuous. Two applicants classified as `high risk` may have substantially different probabilities of default, and the probability estimate can subsequently be mapped into risk bands or scorecard points.

The output of the model should therefore support:

$$
\text{Applicant} \rightarrow \text{Probability of Payment Difficulty}
$$

rather than merely:

$$
\text{Applicant} \rightarrow \{0,1\}
$$

---

### 4.2 Rank Applicants According to Credit Risk

A second objective is to produce a risk ranking that separates applicants with relatively low predicted risk from applicants with relatively high predicted risk.

Ideally:

$$
\hat{p}_{A} < \hat{p}_{B}
$$

should imply that applicant $A$ is estimated to have lower repayment risk than applicant $B$.

This ranking is operationally important because lenders do not necessarily make decisions using a single universal probability threshold. Applicants can instead be segmented into different risk bands according to the lender's risk appetite.

For example:

$$
\text{Low Risk}
\rightarrow
\text{Medium Risk}
\rightarrow
\text{High Risk}
$$

The exact cut-off values are outside the scope of the dataset and must be regarded as policy decisions rather than values that can be inferred directly from the machine-learning model.

---

### 4.3 Reduce the Risk of Financial Loss from Poor Lending Decisions

A central economic rationale for credit scoring is that approving a customer who subsequently cannot repay can generate financial losses for the lender.

Conceptually:

$$
\text{Expected Loss}
\approx
PD \times LGD \times EAD
$$

where:

- $PD$ = Probability of Default;
- $LGD$ = Loss Given Default;
- $EAD$ = Exposure at Default.

The Home Credit dataset primarily supports estimation of the **probability component** of this framework. It does not contain sufficient information to build a complete production-grade expected-loss model covering reliable $LGD$ and $EAD$ estimation.

Therefore, this project should **not** claim to directly optimize expected loss.

Its narrower objective is:

$$
\text{Improve identification of applicants with elevated repayment risk}
$$

which can subsequently contribute to better risk-adjusted lending decisions.

---

### 4.4 Avoid Excessive Rejection of Creditworthy Applicants

Credit risk management is not equivalent to maximizing the number of rejected applicants.

Rejecting every applicant with non-zero risk would eliminate credit losses but would also eliminate profitable lending opportunities.

The relevant business trade-off is:

$$
\text{Risk Reduction}
\quad \leftrightarrow \quad
\text{Credit Availability}
$$

Therefore, the model should distinguish between applicants who are genuinely associated with elevated repayment risk and applicants who can reasonably be considered lower risk.

This means that model evaluation should not focus exclusively on identifying positive cases. The ability to rank and discriminate between different levels of risk is also important.

---

### 4.5 Identify the Main Drivers of Credit Risk

The project has a secondary but important business objective: identify which applicant characteristics and historical financial indicators are associated with payment difficulties.

The objective is to understand relationships of the form:

$$
X_j \rightarrow P(TARGET=1)
$$

where $X_j$ represents an explanatory variable or derived feature.

Potential drivers may include information concerning:

- demographic characteristics;
- employment and income;
- credit history;
- previous loan applications;
- existing credit exposure;
- payment behavior;
- installment history;
- credit-card utilization;
- cash-loan history;
- previous repayment difficulties.

The dataset contains multiple tables specifically providing historical credit and repayment information, allowing the project to investigate risk from both current application characteristics and historical financial behavior. citeturn0search12

This objective is particularly important for a traditional scorecard because a useful scorecard should not merely produce predictions; its variables and their directional relationships with risk should also be interpretable.

---

## 5. Credit Scorecard Objective

The final modeling objective is to translate estimated credit risk into a scorecard-oriented representation.

Conceptually:

$$
\text{Applicant Characteristics}
\rightarrow
\text{Risk Probability}
\rightarrow
\text{Credit Score}
$$

A higher score should correspond to lower estimated credit risk, while a lower score should correspond to higher estimated credit risk.

A conventional scorecard can be represented through a relationship such as:

$$
Score = Offset - Factor \times \ln(Odds)
$$

where the odds are defined according to the chosen good/bad convention.

The exact score scaling, including the selected `Score at Odds` and `Points to Double the Odds`, is a modeling-design decision and is not specified by the Home Credit dataset itself.

Therefore, the project objective is to demonstrate the construction of a **credit-risk scorecard framework**, rather than reproduce an official Home Credit scoring system.

---

## 6. Model Decision Objective

The model should ultimately support a policy-oriented decision framework:

$$
\hat{PD}
\rightarrow
\text{Risk Band}
\rightarrow
\text{Decision Policy}
$$

A conceptual policy may be represented as:

$$
\hat{PD} < \tau_1
\Rightarrow
\text{Lower-risk segment}
$$

$$
\tau_1 \leq \hat{PD} < \tau_2
\Rightarrow
\text{Intermediate-risk segment}
$$

$$
\hat{PD} \geq \tau_2
\Rightarrow
\text{Higher-risk segment}
$$

where $\tau_1$ and $\tau_2$ are policy thresholds.

However, these thresholds must not be presented as empirically established Home Credit policies. They are hypothetical thresholds used to demonstrate how a risk model can support lending decisions.

---

## 7. Business Success Criteria

The project will consider the business objective successfully addressed when the resulting scorecard:

1. **Discriminates between lower-risk and higher-risk applicants.**

2. **Produces meaningful applicant-level risk estimates.**

3. **Ranks applicants according to estimated repayment risk.**

4. **Uses only information that would be available at the defined credit decision point.**

5. **Provides interpretable relationships between applicant characteristics and estimated risk.**

6. **Can translate model output into an understandable risk score or risk band.**

7. **Demonstrates a realistic trade-off between identifying risky applicants and retaining potentially creditworthy applicants.**

8. **Shows acceptable predictive performance on data that was not used to train the model.**

---

## 8. Business Metrics

The business objectives imply several classes of evaluation metrics.

### 8.1 Discrimination

The model should be able to rank risky applicants above safer applicants.

Primary metrics:

$$
ROC\text{-}AUC
$$

and, where appropriate for the imbalanced target:

$$
PR\text{-}AUC
$$

The project should place particular emphasis on ranking quality rather than accuracy alone.

---

### 8.2 Risk Concentration

The portfolio should exhibit increasing observed bad rates as predicted risk increases.

For risk bands $B_1,\ldots,B_k$:

$$
BadRate(B_1) < BadRate(B_2) < \cdots < BadRate(B_k)
$$

when the bands are ordered from lowest to highest predicted risk.

This is a key business interpretation of a scorecard: higher-risk score bands should contain a greater concentration of adverse outcomes.

---

### 8.3 Calibration

The predicted probability should approximately correspond to the observed frequency of payment difficulties.

For a sufficiently large group $G$:

$$
\frac{1}{|G|}
\sum_{i \in G} \hat{p}_i
\approx
\frac{1}{|G|}
\sum_{i \in G} TARGET_i
$$

Good discrimination without calibration is insufficient if the model's output is interpreted as an actual probability of risk.

---

### 8.4 Stability

Model performance and risk ordering should remain reasonably stable across relevant validation samples and applicant segments.

The project should therefore examine:

- train/validation/test performance;
- risk-band bad rates;
- feature distributions;
- population stability where appropriate;
- performance across meaningful applicant segments.

---

## 9. Business Objective Boundaries

The following objectives are explicitly **outside the scope** of what can be justified directly from the Home Credit dataset and the project definition.

### 9.1 Direct Profit Maximization

The project will not claim to maximize lender profit because the dataset does not provide all components required for a reliable profit optimization framework, such as complete pricing, funding cost, recovery, and lifetime profitability information.

### 9.2 Full Expected-Loss Modeling

The project focuses primarily on estimating repayment risk. It does not attempt to construct a complete:

$$
PD \times LGD \times EAD
$$

framework.

### 9.3 Automated Real-World Loan Approval

The scorecard is a decision-support model for analytical and portfolio-risk purposes. It is not a production underwriting system.

### 9.4 Regulatory Approval

The project does not claim regulatory compliance or production readiness. Regulatory requirements concerning fairness, adverse-action explanations, model governance, validation, documentation, and monitoring would require substantially more work than is contained in this project.

### 9.5 Causal Inference

The model identifies predictive associations between applicant characteristics and repayment outcomes.

It does **not** establish that changing a particular characteristic would causally change the probability of default.

For example:

$$
P(TARGET=1 \mid X_j)
$$

does not imply:

$$
do(X_j=x) \Rightarrow P(TARGET=1)
$$

Therefore, feature importance must not be interpreted as causal impact.

---

## 10. Final Business Objective Statement

The project can be summarized by the following business objective:

> **Use historical Home Credit application and credit-behavior data to develop an interpretable credit risk scorecard that estimates the probability of future payment difficulties, ranks applicants by relative credit risk, identifies the principal predictors of repayment risk, and demonstrates how risk estimates can support differentiated lending decisions while balancing credit-risk reduction against the retention of potentially creditworthy applicants.**

The resulting analytical chain is:

$$
\text{Historical Applicant Data}
\rightarrow
\text{Feature Engineering}
\rightarrow
\text{Probability of Payment Difficulty}
\rightarrow
\text{Risk Ranking}
\rightarrow
\text{Scorecard}
\rightarrow
\text{Risk Segmentation}
\rightarrow
\text{Decision Support}
$$

This definition keeps the project aligned with the actual target and information structure supplied by the Home Credit Default Risk dataset, while avoiding claims about business capabilities that the dataset cannot substantiate.

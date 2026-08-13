# Assumptions

This project is built under a set of explicit assumptions about the data, business context, target definition, and modelling process. These assumptions define the conditions under which the resulting credit scorecard is considered valid.

## 1. Business Assumptions

### 1.1 Credit risk is measurable from historical application and repayment behaviour

The project assumes that historical customer and application characteristics contain sufficient information to distinguish between relatively lower-risk and higher-risk borrowers.

The model therefore learns the relationship between observable borrower characteristics at the time of credit assessment and subsequent credit performance.

### 1.2 Historical behaviour is informative about future credit risk

The project assumes that patterns observed in historical data remain sufficiently representative of the population and lending environment relevant to the modelling period.

This assumption is necessary because a scorecard is fundamentally a predictive model:

$$
P(\text{Bad} \mid X)
$$

where $X$ represents information available at the time of credit assessment.

If the underlying population, lending policy, macroeconomic environment, or borrower behaviour changes substantially, model performance may deteriorate.

### 1.3 The target variable represents a meaningful definition of credit risk

The project assumes that the selected binary target variable provides a reasonable operational definition of "bad" versus "good" credit performance.

The target must represent an economically meaningful adverse credit outcome rather than merely a statistical distinction.

The exact bad/good definition will be established during target definition and must remain consistent throughout model development and evaluation.

### 1.4 The model is intended to support credit-risk assessment, not replace credit policy

The scorecard is assumed to be one component of a credit decision process.

A model score indicates estimated risk; it does not independently determine whether an application should be approved or rejected.

Credit policy, affordability requirements, regulatory constraints, and operational considerations are outside the predictive model itself.

## 2. Data Assumptions

### 2.1 Predictors are available at the decision point

A fundamental assumption is that model features represent information that would actually be available when the credit decision is made.

Variables that become available only after the decision point must not be used as predictors.

This prevents **data leakage**, where information about future events inadvertently enters the model.

### 2.2 Historical data contains sufficient information for model development

The dataset is assumed to contain:

- a sufficiently large number of observations;
- a meaningful number of bad cases;
- relevant borrower/application characteristics;
- an identifiable target variable;
- sufficient variation in predictor values.

If these conditions are not satisfied, model estimates may be unstable or statistically unreliable.

### 2.3 Missing values are informative only when supported by the data

Missingness is not automatically assumed to represent a particular borrower characteristic.

Missing-value treatment must therefore be determined empirically and documented.

Depending on the variable, missingness may be handled through:

- explicit missing categories;
- imputation;
- grouping/binning;
- exclusion of variables with excessive or problematic missingness.

### 2.4 Extreme values and invalid observations are treated as data-quality issues

Outliers are not automatically considered genuine borrower behaviour.

The project assumes that data-quality analysis can distinguish plausible extreme observations from clearly invalid values.

Examples include impossible ages, invalid income values, or inconsistent categorical codes.

### 2.5 Variables with excessive sparsity or insufficient discriminatory information may be excluded

Not every available variable is assumed to be useful for the scorecard.

Variables may be removed because of:

- excessive missingness;
- near-zero variance;
- unstable relationship with the target;
- insufficient predictive power;
- excessive cardinality;
- data leakage;
- unacceptable instability across samples.

## 3. Temporal Assumptions

### 3.1 The observation period precedes the performance period

For each modelling observation, predictor information must originate from the observation window, while the target outcome is observed during a subsequent performance window.

Conceptually:

$$
\text{Observation Window} \rightarrow T_0 \rightarrow \text{Performance Window}
$$

where $T_0$ is the reference or decision point.

This temporal ordering is essential for preventing future information from entering the predictors.

### 3.2 The observation window contains only information available before or at $T_0$

The model must not use information generated after the decision point.

For example, if the performance window covers 12 months after $T_0$, repayment behaviour occurring during those 12 months cannot be used to construct predictors for the same observation.

### 3.3 The performance window is sufficiently long to observe the defined bad event

The performance window must provide enough time for the selected definition of default or bad performance to materialize.

If the performance window is too short, some borrowers who would eventually become bad may incorrectly appear as good.

### 3.4 Observations require sufficient outcome maturity

An observation should only be included in model development when its required performance window has been sufficiently observed.

Applications whose performance period has not yet matured should not be treated as confirmed good observations merely because no bad event has been observed yet.

## 4. Sampling Assumptions

### 4.1 Development and validation samples are representative of the same underlying population

The train, validation, and test samples are assumed to originate from sufficiently comparable populations.

Performance differences between samples should therefore primarily reflect model generalization rather than completely different customer populations.

### 4.2 Temporal splitting is preferred when feasible

Because credit risk is inherently time-dependent, a temporal validation strategy is assumed to provide a more realistic estimate of future model performance than a purely random split.

The final validation design should therefore respect the chronological structure of the data where the dataset permits it.

### 4.3 Class imbalance is expected

Credit-risk datasets generally contain substantially more good observations than bad observations.

The project assumes that class imbalance is a property of the problem rather than a reason to distort the underlying population.

Evaluation should therefore emphasize metrics appropriate for imbalanced classification and credit-risk modelling.

## 5. Modelling Assumptions

### 5.1 The scorecard should prioritize interpretability

The project assumes that the model must be understandable to analysts and business stakeholders.

A traditional scorecard framework based on:

$$
\text{Variable}
\rightarrow
\text{Binning}
\rightarrow
\text{WOE}
\rightarrow
\text{Logistic Regression}
\rightarrow
\text{Score}
$$

is therefore considered appropriate.

### 5.2 Predictor effects should be sufficiently stable and interpretable

The relationship between a transformed predictor and the probability of bad performance is assumed to be sufficiently stable to support scorecard development.

Where appropriate, variables should exhibit interpretable and reasonably monotonic relationships with risk after binning and transformation.

### 5.3 Multicollinearity should be controlled

Highly correlated variables may provide redundant information and produce unstable regression coefficients.

The project therefore assumes that correlation analysis, VIF analysis, or other appropriate diagnostics can be used to identify and control excessive multicollinearity.

### 5.4 Model performance is not determined by a single metric

No single metric is assumed to be sufficient for evaluating the scorecard.

Evaluation should consider several dimensions, including:

- discriminatory power;
- calibration;
- stability;
- ranking performance;
- business usefulness;
- interpretability.

Typical statistical measures include **ROC-AUC**, **KS statistic**, and calibration-related measures.

## 6. Scorecard Assumptions

### 6.1 Higher scores correspond to lower estimated credit risk

The final scorecard is assumed to be oriented so that an increase in score corresponds to a decrease in estimated probability of bad performance.

The relationship should be explicitly verified rather than assumed from the numerical implementation.

### 6.2 Score points are a transformation of predicted risk

The credit score is not an independent predictive model.

It is a transformation of the estimated odds or probability of bad performance into a more interpretable numerical scale.

A common formulation is:

$$
Score = Offset + Factor \times \ln(Odds)
$$

where the direction and definition of odds must be specified consistently.

### 6.3 The score scale is arbitrary but must be internally consistent

The absolute numerical value of a score has no inherent meaning.

What matters is the mapping between score, odds/probability of bad performance, and the chosen reference points such as **Score at Odds** and **Points to Double the Odds**.

## 7. Stability Assumptions

### 7.1 Predictor distributions are not expected to change arbitrarily

The project assumes that the distribution of important predictors will remain reasonably stable between the development population and future populations.

Population Stability Index (PSI) or equivalent distributional diagnostics may be used to assess this assumption.

### 7.2 Model relationships are assumed to remain sufficiently stable

Even if predictor distributions remain stable, the relationship between predictors and bad performance can change.

Therefore, stability assessment should consider both:

1. changes in the distribution of input variables; and
2. changes in predictive performance or risk relationships.

### 7.3 The project does not assume permanent model validity

A scorecard is not assumed to remain valid indefinitely.

Its validity is conditional on the population, product, credit policy, economic environment, and data-generating process remaining sufficiently comparable to the development context.

## 8. Limitations of the Assumptions

These assumptions are modelling conditions, not guarantees.

Violations may arise from:

- changes in lending policy;
- changes in customer composition;
- economic shocks;
- changes in default behaviour;
- changes in data collection;
- missing or incorrectly recorded variables;
- selection bias;
- sample-selection effects;
- target-definition limitations.

Any major assumption violation should be documented because it affects the interpretation and generalizability of the scorecard.
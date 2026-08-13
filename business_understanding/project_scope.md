# Project Scope

## 1. Project Overview

This project develops an interpretable **credit risk scorecard** using the Home Credit dataset.

The primary objective is to reproduce the core analytical workflow used in traditional credit-scorecard development:

$$
\text{Business Understanding}
\rightarrow
\text{Data Understanding}
\rightarrow
\text{Data Preparation}
\rightarrow
\text{Feature Engineering}
\rightarrow
\text{WOE/IV}
\rightarrow
\text{Logistic Regression}
\rightarrow
\text{Scorecard}
\rightarrow
\text{Validation}
$$

The project focuses on the statistical and risk-modelling aspects of scorecard development rather than production deployment.

## 2. In Scope

### 2.1 Business Understanding

The project includes:

- defining the credit-risk problem;
- defining the modelling objective;
- defining the target/bad-event concept;
- establishing business-oriented evaluation metrics;
- documenting assumptions;
- defining project boundaries.

### 2.2 Data Understanding

The project includes:

- dataset structure analysis;
- identification of relevant tables and variables;
- descriptive statistics;
- target distribution analysis;
- missing-value analysis;
- categorical and numerical variable analysis;
- outlier and data-quality analysis;
- preliminary relationship analysis between predictors and target.

### 2.3 Data Preparation

The project includes:

- handling missing values;
- handling invalid observations;
- treatment of extreme values where justified;
- categorical variable consolidation where necessary;
- removal of unsuitable variables;
- construction of a modelling dataset;
- prevention of target leakage.

### 2.4 Feature Engineering

The project includes feature engineering relevant to credit-risk modelling.

Potential transformations include:

- aggregation of related variables;
- ratio variables;
- age or tenure-related variables;
- financial burden indicators;
- utilization or affordability-related indicators;
- domain-relevant transformations supported by the available data.

Feature engineering will be restricted to information that would be available at the modelling reference point.

### 2.5 Variable Screening

The project includes systematic variable screening using criteria such as:

- missingness;
- cardinality;
- variance;
- univariate discriminatory power;
- Information Value (IV);
- correlation;
- multicollinearity;
- business interpretability;
- stability.

Variables that fail predefined criteria may be excluded from subsequent modelling.

### 2.6 Weight of Evidence and Information Value

The project includes implementation and analysis of:

- variable binning;
- fine classing;
- coarse classing;
- Weight of Evidence (WOE);
- Information Value (IV);
- monotonicity assessment;
- bin merging;
- treatment of special and missing values.

The purpose is to transform raw variables into representations suitable for an interpretable scorecard.

### 2.7 Logistic Regression Scorecard Model

The core predictive model will be **logistic regression**.

The modelling process includes:

- model specification;
- variable selection;
- coefficient interpretation;
- multicollinearity diagnostics;
- statistical significance analysis where appropriate;
- model discrimination;
- model calibration;
- comparison of candidate model specifications.

The final model should prioritize interpretability and statistical defensibility rather than maximizing predictive complexity.

### 2.8 Scorecard Construction

The project includes conversion of the final logistic regression model into a traditional points-based scorecard.

This includes:

- defining the score scale;
- selecting a base score;
- defining base odds;
- defining points to double the odds;
- calculating characteristic points;
- constructing the final scorecard;
- mapping score ranges to estimated risk.

### 2.9 Model Validation

Validation includes:

- train/validation/test evaluation where appropriate;
- preferably chronological validation where the data structure permits;
- ROC-AUC;
- KS statistic;
- discriminatory-power analysis;
- calibration analysis;
- score distribution analysis;
- bad-rate analysis by score band;
- model stability analysis.

### 2.10 Model Interpretation

The project includes interpretation of:

- coefficient signs and magnitudes;
- WOE transformations;
- variable-level risk relationships;
- score contribution by characteristic;
- score-band risk;
- model strengths and limitations.

The final result should be explainable to a technically literate business or risk audience.

### 2.11 Documentation

The project includes documentation of:

- business assumptions;
- data assumptions;
- modelling decisions;
- feature transformations;
- variable-selection criteria;
- scorecard methodology;
- validation results;
- limitations;
- conclusions.

A final project report and supporting analytical notebooks/scripts are within scope.

### 2.12 Optional Dashboard

A lightweight dashboard may be included to demonstrate:

- score distribution;
- bad-rate by score band;
- variable-level risk patterns;
- model performance;
- scorecard characteristics.

The dashboard is considered a presentation layer rather than a production application.

## 3. Out of Scope

### 3.1 Production Deployment

The project does not include:

- production API development;
- real-time scoring infrastructure;
- cloud deployment;
- model-serving architecture;
- container orchestration;
- production databases;
- CI/CD pipelines.

### 3.2 Model Monitoring and Retraining

The project does not implement a production-grade:

- model monitoring system;
- automated drift detection;
- automated performance monitoring;
- automated retraining pipeline;
- champion/challenger framework.

Stability analysis may be performed offline as part of model validation, but this is not equivalent to production monitoring.

### 3.3 Advanced Machine Learning as the Primary Model

The project does not make complex machine-learning models the primary modelling approach.

Models such as:

- XGBoost;
- LightGBM;
- Random Forest;
- neural networks;
- deep learning;

are outside the core scope.

They may only be used as supplementary benchmarks if necessary.

The final scorecard remains based on an interpretable logistic-regression framework.

### 3.4 Causal Inference

The project is predictive rather than causal.

It does not attempt to establish causal relationships such as:

> "Increasing income by X causes default probability to decrease by Y."

Observed relationships are interpreted as predictive associations within the modelling population.

### 3.5 Real Credit Policy Implementation

The project does not implement an actual lender's:

- approval policy;
- rejection rules;
- affordability policy;
- pricing strategy;
- credit-limit assignment;
- collections strategy.

The scorecard estimates credit risk; it does not constitute a complete credit decision engine.

### 3.6 Regulatory Certification

The project is educational and portfolio-oriented.

It does not constitute a regulatory-approved credit model and does not attempt to satisfy the complete governance requirements of a regulated financial institution, including formal:

- model validation;
- model risk governance;
- regulatory approval;
- audit certification;
- fairness/compliance certification.

### 3.7 External Macroeconomic Modelling

Macroeconomic variables such as:

- GDP;
- unemployment;
- inflation;
- interest rates;

are outside the core scope unless explicitly incorporated as an extension.

The primary modelling dataset will remain the Home Credit data.

### 3.8 Real-World Production Data Integration

The project does not integrate with:

- banking core systems;
- credit bureau APIs;
- transaction databases;
- real-time customer information;
- external identity systems.

## 4. Scope Boundary

The project can be summarized as:

> **An end-to-end analytical development of an interpretable credit risk scorecard, from business problem definition through scorecard construction and offline validation, using the Home Credit dataset.**

The project ends at the point where a validated, documented, interpretable scorecard has been produced.

The following production lifecycle is explicitly excluded:

$$
\text{Deployment}
\rightarrow
\text{Production Monitoring}
\rightarrow
\text{Automated Retraining}
\rightarrow
\text{Production Governance}
$$

This boundary keeps the project focused on the core competencies of credit-risk modelling:

**target definition, temporal data design, feature engineering, binning, WOE/IV, logistic regression, scorecard scaling, validation, and risk interpretation.**
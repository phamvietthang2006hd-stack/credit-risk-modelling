:::writing{variant="document" id="58321" title="Problem Definition"}
# Problem Definition

## 1. Problem Statement

The objective of this project is to develop a credit risk scoring model that estimates the probability that a loan applicant will experience a defined adverse credit outcome within a specified performance window after loan origination.

The model is intended to support credit decision-making by distinguishing applicants with relatively different levels of credit risk based on information available at or before the time of application.

More specifically, given the information available for an applicant at the decision point \(T_0\), the model estimates:

\[
P(Y=1 \mid X_{T_0})
\]

where:

- \(X_{T_0}\) represents the applicant's observable characteristics and historical information available at or before \(T_0\).
- \(Y=1\) represents the occurrence of the predefined bad-credit outcome during the performance window following \(T_0\).
- \(P(Y=1 \mid X_{T_0})\) represents the applicant's estimated probability of default or other defined adverse credit event.

The core problem is therefore a supervised binary classification problem under a temporal constraint: the model must use only information that would have been available when the credit decision was made, while the target outcome is observed only after that decision.

## 2. Decision Context

In a lending environment, a financial institution must decide whether an applicant should be granted credit and, potentially, under what risk-based terms.

The fundamental difficulty is that the applicant's future repayment behavior is unknown at the time of application. Historical applicant characteristics, previous credit behavior, financial information, and other observable variables can be used as proxies for future creditworthiness.

A credit scorecard attempts to transform these observable characteristics into a quantitative measure of credit risk that can be used to rank applicants from lower-risk to higher-risk populations.

This project focuses on the predictive component of that problem: estimating future credit risk from information available at the time of credit assessment.

## 3. Prediction Target

The prediction target is a binary credit-risk outcome:

- **Good:** the applicant does not experience the predefined adverse credit event during the performance window.
- **Bad:** the applicant experiences the predefined adverse credit event during the performance window.

For the Home Credit dataset, the target variable is based on the dataset's provided credit-risk outcome definition.

The exact operational definition of "bad" must be established before model development and applied consistently throughout dataset construction, model training, validation, and evaluation.

## 4. Observation and Performance Timing

The problem is explicitly temporal.

Let:

- \(T_0\) = the credit decision / loan application point.
- Observation Window = the historical period from which explanatory variables are collected.
- Performance Window = the future period during which the applicant's repayment outcome is observed.

The model must satisfy the following information constraint:

\[
X \subseteq \mathcal{I}_{\leq T_0}
\]

where \(\mathcal{I}_{\leq T_0}\) denotes information available on or before the decision point.

The target is determined from information occurring after \(T_0\):

\[
Y = f(\mathcal{I}_{>T_0})
\]

This separation is critical because using information generated after \(T_0\) to construct model features would introduce target leakage and would make the model unsuitable for genuine credit decisioning.

## 5. Input Data

The model will use applicant-level information available at or before the credit decision point.

Potential information categories include:

- Demographic and personal characteristics
- Employment and income-related information
- Existing credit obligations
- Previous credit application history
- Previous repayment behavior
- Loan characteristics
- Historical financial indicators
- Aggregated information derived from historical credit records

The Home Credit dataset provides multiple related tables containing application-level and historical credit information. These sources may require appropriate temporal aggregation and feature construction before being used by the predictive model.

## 6. Expected Model Output

The primary model output is an estimated probability of the applicant being classified as "bad":

\[
PD_i = P(Y_i=1 \mid X_i)
\]

where \(PD_i\) denotes the estimated probability of default for applicant \(i\).

This probability can subsequently be transformed into a credit score or risk band for decision-making purposes.

The scorecard representation is therefore considered a downstream representation of the underlying credit-risk probability rather than the fundamental prediction target itself.

## 7. Scope of the Problem

This project addresses the development and evaluation of a traditional credit risk scorecard using structured historical credit data.

The scope includes:

- Defining the credit-risk prediction problem.
- Constructing a temporally valid modeling dataset.
- Performing exploratory analysis of credit-risk characteristics.
- Developing predictive features from available historical information.
- Building and evaluating credit-risk classification models.
- Developing a scorecard representation where appropriate.
- Evaluating model discrimination, calibration, stability, and business-relevant performance.
- Interpreting the relationship between applicant characteristics and predicted credit risk.

The project does not attempt to reproduce a complete production lending system.

In particular, the following are outside the primary scope:

- Real-time credit decision APIs
- Production deployment
- Automated model retraining pipelines
- Production monitoring infrastructure
- Full loan-pricing optimization
- Collections optimization
- Portfolio-level capital or regulatory modeling

## 8. Problem Formulation

The problem can be formally represented as follows.

Given a population of applicants:

\[
D = \{(X_i,Y_i)\}_{i=1}^{N}
\]

where \(X_i\) contains information available at the credit decision point and \(Y_i \in \{0,1\}\) represents the subsequent credit outcome, the objective is to learn a function:

\[
f: X \rightarrow [0,1]
\]

such that:

\[
\hat{P}_i = f(X_i)
\]

provides a useful estimate of the probability that applicant \(i\) will experience the defined adverse credit outcome during the performance window.

The quality of the model is evaluated not only by predictive discrimination but also by whether the predictions are temporally valid, appropriately calibrated, and useful for differentiating applicants according to their underlying credit risk.

## 9. Fundamental Modeling Constraint

The central constraint of the problem is:

> **The model may only use information that would have been available at the time the credit decision was made.**

Consequently, feature construction must respect the temporal boundary at \(T_0\).

Any variable whose value depends on events occurring after \(T_0\), directly or indirectly, must not be available to the model at prediction time.

This constraint defines the difference between a valid credit-risk model and a model that merely achieves high predictive performance through information leakage.

## 10. Problem Definition Summary

This project addresses the problem of predicting an applicant's future adverse credit outcome using only information available at or before the time of credit application.

Formally:

\[
\boxed{
\text{Historical applicant information}
\rightarrow
\text{Probability of future credit risk}
}
\]

The resulting probability estimate can then serve as the quantitative foundation for a credit scorecard that ranks applicants according to their estimated risk.
:::
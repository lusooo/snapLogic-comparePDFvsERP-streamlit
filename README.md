# Overview
This use-case is about doing Contract reconciliation between:
* Digital version of a contract (PDF)
* Contract data provisioned in the ERP/Billing System

The specific pain that this use-case is solving is because the PDF contract contains pricing revision formula that are not always provisioned the right way in the ERP/Billing System. 

The issues that can happen are the following:
* the pricing revision formula is not applied at all => It means the initial price (P0) will never be increased
* the pricing revision formula is wrong in the ERP

**Consequences**: the customers are underbilled

**Business Value**: several millions of euros per  year 

# Streamlit App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)] (https://snaplogic-genaibuilder-pdf-erp-reconciliation.streamlit.app/)

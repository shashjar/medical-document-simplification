# CS4120 Final Project - Medical Document Summarization

## Overview

Our final project for this course was the evaluation of various LLM models for the purpose of simplifying and summarizing medical documents. Throughout our service learning, we noticed that several older adults, especially the ones we volunteered with, often struggled to meaningfully interpret their medical summaries from recent doctor’s appointments and bloodwork tests. Given that many of these older adults often struggle with chronic health issues and frequent medical visits, we found it beneficial for our project to investigate how older adults can get actionable results from their health data as quickly and easily as possible. 
As such, our project evaluates performance of the BART, T5, and GPT-2 language model architectures in the context of fine-tuning for medical document summarization. Using our datasets, we evaluate these models across a variety of metrics, including ROUGE and Flesch-Kincaird scores, to determine which model is best at making medical information shorter and more digestible for older adults. 

## Setup

All relevant datasets and dependencies can be found in the ``medical_summarization.ipynb`` Jupyter notebook. The entire notebook can be ran top-to-bottom, and is currently configured to load pre-configured weights from our prior training.


### Metrics

We primarily use ROUGE, Flesch Kincaid, and Linsear Write as our metrics for evaluting our model performance after fine-tuning. The relevant code for loading in and using these metrics, as well as our sample text for generating summaries, can be found in the ``/metrics`` directory.

### Datasets

Our datasets used for fine-tuning, Wikismall and MIMIC, can both be found in the ``/datasets`` directory. We're using ``git-lfs`` to store our datasets, so that will likely need to be configured on your system before fetching our data. 

### Archive

Files previously used to generate metrics of T5 and BART performance for our presentation can be found in the ``/archive`` directory. The majority of the code found in these Jupyter notebooks has now been consolidated into ``medical_summarization.ipynb``.

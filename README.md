# CS4120 Final Project - Medical Document Summarization

## Overview

Our final project for this course was the evaluation of various LLM models for the purpose of simplifying and summarizing medical documents. Throughout our service learning, we noticed that several older adults, especially the ones we volunteered with, often struggled to meaningfully interpret their medical summaries from recent doctor’s appointments and bloodwork tests. Given that many of these older adults often struggle with chronic health issues and frequent medical visits, we found it beneficial for our project to investigate how older adults can get actionable results from their health data as quickly and easily as possible. 
As such, our project evaluates performance of the BART, T5, and GPT-2 language model architectures in the context of fine-tuning for medical document summarization. Using our datasets, we evaluate these models across a variety of metrics, including ROUGE and Flesch-Kincaird scores, to determine which model is best at making medical information shorter and more digestible for older adults. 

## Setup

All relevant datasets and dependencies can be found in the ``medical_summarization.ipynb`` Jupyter notebook. The entire notebook can be ran top-to-bottom, and is currently configured to:
- load pre-configured weights from prior training 
- evaluate a sample document.

## Model Weights

Throughout our codebase are several references to the `models`, `t5-wikismall-mimic-dir`, and `bart-mimic-dir` directories, which we used for storing and loading our model weights. Due to size limits on Canvas, we're unable to submit these folders directly. As such, we'll be attaching a Google Drive link at the bottom of our overview. 


### Metrics

We primarily use ROUG and Flesch Kincaid as our metrics for evaluting our model performance after fine-tuning. Our sample text for generating summaries can be found in the ``/metrics`` directory, while the relevant code for evaluating our models can be found in ``evaluation.ipynb``. An implemention of functions for evaluating our models can be found in ``eval_metrics.py``.

### Datasets

Our datasets used for fine-tuning, Wikismall and MIMIC, can both be found in the ``/datasets`` directory. We're using ``git-lfs`` to store our datasets, so that will likely need to be configured on your system before fetching our data. 

### Archive

Files previously used to generate metrics of T5 and BART performance for our presentation can be found in the ``/archive`` directory. The majority of the code found in these Jupyter notebooks has now been consolidated into ``medical_summarization.ipynb``.

### Additional Large Files

Model files and a MIMIC CSV can be found here: https://drive.google.com/drive/folders/1qBbqvLzr3qYfc-asrZsK7v74LXq3X0Vr?usp=sharing

To run evaluation.ipynb without changes, add checkpoint-1000 (BART) and checkpoint-11500 (T5) to a ``models/`` directory, and add ``mimic-iv-bhc.csv`` to the existing ``datasets/mimic-iv-bhc.csv/`` directory.

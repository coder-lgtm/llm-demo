# Demystifying Generative AI And Machine Learning Models
### Women In Tech Boston; Oct 2-3, 2023

## Hands-On workshop to build a custom application using a pre-trained and fine-tuned Large Language Model (Llama2)
This repository conrains instructions and code for building custom applications using LLM, dataset builder utility code for generaiting a custom mini training dataset for cost effective model tuning.

Overall, the goal of this workshop is to familiarize you with
* Generative AI models ecosystem
* Core concepts of the LLMs
* Prompt Engineering

Repository contains
* Installation instructions for some Open Source technologies
* Setup instructions to use Open Sourced Meta Llama2 models
* Code to build simple chatbot application using Llama2 and Streamlit
* Custom mini dataset creator for fine tuning Llama2
* Sample dataset
* Replicate model training scripts
  
## Pre-workshop setup steps
### We will be using following tools and resources
* Our choice of programming language -  [Python 3.8](https://www.python.org/downloads/release/python-380/)
* Quick and elegant app builder - [Streamlit](https://streamlit.io/)
* Place to host and run Machine Learning models in Cloud - [Replicate](https://replicate.com/explore)
* Open source Large Language Model - [Llama2 by Meta](https://ai.meta.com/llama/)
* Fine tuned custom Model - <TBD>
* I use [Visual Studio Code](https://code.visualstudio.com/download) for coding but you could use any text editor as well

### Setup instructions
(These are for MacOS, if you are using Windows system, just google for similar instructions on Windows)
- [ ] Install Homebrew if you don't have it.
      Go to a terminal and run ```$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```
- [ ] Install python 3.8 using homebrew
      ```brew install python@3.8```
- [ ] Checkout this repository
      ```git checkout git@github.com:coder-lgtm/llm-demo.git```
      OR
      Just download the repository from https://github.com/coder-lgtm/llm-demo/archive/refs/heads/main.zip and unzip
- [ ] cd into the llmdemo directory and run the following to install dependencies using the requirements.txt
      ```pip3 install -r ./requirements.txt```
      This will install streamlit and replicate packages for you to use
- [ ] Create an account on [Replicate](https://replicate.com/explore). You should receive an API key that starts with r8_<>. You will need this for this workshop. I used my github account to login, this helps with the integration greatly.

### Workshop action items
- [ ] Familiarize yourself with the Replicate interface
      <Screenshots>
- [ ] Checkout Streamlit interface quickly
- [ ] Go over the Demo Chat App code
- [ ] Execute the code and launch the Streamlit app - show how tweaking the different controls helps
- [ ] Discuss the custom fine tuned model. Discuss the tuning process.
      <Screenshots>
- [ ] Build a new app with the new fine tuned model.
- [ ] Compare the performace of a custom model against the Foundational model

### References and useful links
* https://www.kaggle.com/datasets
* https://huggingface.co/models?dataset=dataset:databricks/databricks-dolly-15k
* https://github.com/a16z-infra/llama2-chatbot/blob/main/llama2_chatbot.py


# Demystifying Generative AI And Machine Learning Models
### Women In Tech Boston; Oct 2-3, 2023
<table><tr>
<td><img
  src="https://registration.women-in-tech-boston.com/cdn/shop/files/preview_images/1638049754-7c3db904ac8414de3d73c860f5cac86fe898899406f25ade9b66ab9659ea9c10-d_295x166_d721bd70-ae81-4662-9526-65fb13e1d595.jpg?v=1687277637"
  alt="Alt text"
  title="Header"
  style="display: inline-block; margin: 0 auto; max-width: 50px; max-height: 50px"> </td>
  <td><img
  src="https://png.pngtree.com/thumb_back/fh260/back_our/20190621/ourmid/pngtree-blue-artificial-intelligence-technology-ai-robot-banner-image_196890.jpg"
  alt="Alt text"
  title="Header"
  style="display: inline-block; margin: 0 auto; max-width: 300px; max-height: 50px"></td>
</tr></table>


## Hands-On workshop to build custom application using Large Language Models (Llama2)
This repository contains instructions and code for building custom applications using LLM, dataset builder utility code for generating a custom mini training dataset for cost effective model tuning.

### Goal of this workshop is to get familiarized with
* Generative AI models ecosystem
* Core concepts of the LLMs
* Prompt Engineering
* Fine-tune a custom model for a specific use case
* Build an app using a pre-trained base LLM and domain specific fine-tuned LLM
<img
  src="./images/chatapp.png"
  alt="Alt text"
  title="Dashboard"
  style="display: inline-block; margin: 0 auto; max-width: 200px">
  
### Repository contains
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
* Place to host and run Machine Learning models in the Cloud - [Replicate](https://replicate.com/explore)
* Open source Large Language Model - [Llama2 by Meta](https://ai.meta.com/llama/)
* Fine tuned custom Model - (In progress, will update the path to this soon)
* I use [Visual Studio Code](https://code.visualstudio.com/download) for coding but you could use any text editor as well

### Setup instructions
- [ ] If you are using Windows, just [download Python](https://www.python.org/downloads/) and run the installer
- [ ] For Mac, Install Homebrew if you don't have it.
      Go to a terminal and run ```$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```
- [ ] Install python 3.8 using homebrew
      ```brew install python@3.8```
      
- [ ] Checkout this repository
      ```git checkout git@github.com:coder-lgtm/llm-demo.git```
      OR
      Just download the repository from https://github.com/coder-lgtm/llm-demo/archive/refs/heads/main.zip and unzip
- [ ] cd into the llm-demo directory and run the following to install dependencies using the requirements.txt
      ```pip3 install -r ./requirements.txt```
      This will install streamlit and replicate packages for you to use
- [ ] Create an account on [Replicate](https://replicate.com/explore). You should receive an API key that starts with r8_<>. You will need this for this workshop. I used my github account to login, this helps with the integration greatly.

## Workshop Agenda

- [ ] Familiarize yourself with Replicate interface
    <img
  src="./images/ReplicateDashboard.png"
  alt="Alt text"
  title="Dashboard"
  style="display: inline-block; margin: 0 auto; max-width: 200px">
  
- [ ] Overview of Streamlit 
- [ ] Go over the Demo Chat App code
- [ ] Execute the code and launch the Streamlit app - tweak the different controls to see the variations in the app behavior
- [ ] Discuss the process of Fine Tuning LLM base model
    
     <img
  src="./images/TrainingCustomModel1.png"
  alt="Alt text"
  title="Train your model"
  style="display: inline-block; margin: 0 auto; max-width: 200px">

  <img
  src="./images/TrainingCustomModel2.png"
  alt="Alt text"
  title="Summary of trainings"
  style="display: inline-block; margin: 0 auto; max-width: 200px">
  
- [ ] Build a new app with the domain-specitic fine tuned model
- [ ] Compare the performance of the custom model against the base Llama2 model

### References and useful links
* https://www.kaggle.com/datasets
* https://huggingface.co/models?dataset=dataset:databricks/databricks-dolly-15k
* https://github.com/a16z-infra/llama2-chatbot/blob/main/llama2_chatbot.py

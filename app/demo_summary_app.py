import streamlit as st
import replicate
import os

# This is a skeletal code. We will fill in the details during our workshop.

#Title
st.title ("Summarization Application")
st.caption ("This application summarizes any text by leveraging the power of Generative AI. Try our app now! ")
is_custom = False
llm = "replicate/llama-2-7b:acdbe5a4987a29261ba7d7d4195ad4fa6b62ce27b034f989fcb9ab0421408a7c"

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    output = replicate.run(
		llm,
		input={} #Workshop time
		)
    return output

# Function for generating Custom Model response
def generate_llama2_response_custom(prompt_input):
	output = replicate.run(
		llm,
		input={} #Workshop time
	)
	return output

# Clear chat history for better demo / testing
def clear_chat_history():
	st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Our simple UI - thanks to Streamlit
with st.sidebar:
    st.title('Your chat with Llama!')
    replicate_api = st.text_input('Enter Replicate API token:', type='password')
    if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
        st.warning('Please enter your credentials!', icon='⚠️')
        replicate_api = ''
    else:
        st.success('Proceed to the chat!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Custom'], key='selected_model')
    if selected_model == 'Llama2-7B':
        is_custom = False
    else:
        is_custom = True
        llm = "" #workshop time
	


with st.container():
	# Display or clear chat messages
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.write(message["content"])

	if prompt := st.chat_input(disabled = not replicate_api):
		#cache it
		st.session_state.messages.append({"role": "user", "content": prompt})
		with st.chat_message("user"):
			st.write(prompt)
       	  
	# Generate a new response if last message is not from assistant
	if st.session_state.messages[-1]["role"] != "assistant":
		with st.chat_message("assistant"):
			# Thinking icon while we get the response back from our model
			with st.spinner("Thinking..."):
				if is_custom:
					response = generate_llama2_response_custom(prompt)
				else:
					response = generate_llama2_response(prompt)
				placeholder = st.empty()
				full_response = ''
				for item in response:
					if item == '.</s>':
						break
					full_response += item
				placeholder.markdown(full_response)
	    
		#cache it 
		message = {"role": "assistant", "content": full_response}
		st.session_state.messages.append(message)
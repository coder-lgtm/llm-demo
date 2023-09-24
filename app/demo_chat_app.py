import streamlit as st
import replicate
import os

# Refactored from <https://github.com/a16z-infra/llama2-chatbot>

#Title
st.title ("Demo Chat Application")
st.caption ("This is a chat aapplication that leverages the power of Generative AI. Chat with our agent now! ")
llm = 'replicate/llama-2-7b:acdbe5a4987a29261ba7d7d4195ad4fa6b62ce27b034f989fcb9ab0421408a7c'

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Function for generating LLaMA2 response with chat history
def generate_llama2_response_with_history(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "system_prompt": "You are a helpful assistant. You learn from your chat context and you add something extra but relevant",
                                  "max_new_tokens": 1000})
    return output

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    output = replicate.run(
    	llm,
    	input={"prompt": prompt_input,
    	       "system_prompt": "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.", 
    	       "max_new_tokens": 1000}
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

    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-70B-Chat'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'replicate/llama-2-7b:acdbe5a4987a29261ba7d7d4195ad4fa6b62ce27b034f989fcb9ab0421408a7c'
    elif selected_model == 'Llama2-70B-Chat':
        llm = 'replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf'
   
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
	            response = generate_llama2_response(prompt)
	            placeholder = st.empty()
	            full_response = ''
	            for item in response:
	             	full_response += item
	             	#print("got a response >> " + item + " <<")
	             	#print("\n")
	            # print("Processed the response")    
	            placeholder.markdown(full_response)
	    
	    #cache it 
	    message = {"role": "assistant", "content": full_response}
	    st.session_state.messages.append(message)
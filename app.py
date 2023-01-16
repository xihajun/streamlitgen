import streamlit as st

st.title("CmdGenForm")

task = st.selectbox("Task", [("image-classification", "Image Classification"),
                             ("object-detection", "Object Detection"),
                             ("packed-bert", "NLP")])

model = st.selectbox("Model", [])

mode = st.selectbox("Mode", [("performance", "Performance"),
                             ("accuracy", "Accuracy"),
                             ("compliance", "Compliance")])

category = st.selectbox("Category", [("datacenter", "Datacenter"),
                                    ("edge-server", "Edge Server"),
                                    ("edge-appliance", "Edge Appliance")])

sut = st.selectbox("System", [])

scenario = st.selectbox("Scenario", [("offline", "Offline"),
                                     ("server", "Server")])

offline_qps = st.number_input("Offline QPS", min_value=0, max_value=None, value=0, step=1)
server_qps = st.number_input("Server QPS", min_value=0, max_value=None, value=0, step=1)

singlestream_latency = st.number_input("SingleStream Latency", min_value=0, max_value=None, value=0, step=1)
multistream_latency = st.number_input("MultiStream Latency", min_value=0, max_value=None, value=0, step=1)

sdk = st.text_input("SDK",value="1.8.3.7")

verbose = st.checkbox("Verbose")
timestamp = st.checkbox("Timestamp")
replace_existing = st.checkbox("Replace Existing")
dataset_size = st.checkbox("Dataset size")

if dataset_size:
    dataset_size_value = st.number_input("Dataset Size", min_value=0, max_value=None, value=0, step=1)
else:
    dataset_size_value = None

buffer_size = st.checkbox("Buffer size")

if buffer_size:
    buffer_size_value = st.number_input("Buffer Size", min_value=0, max_value=None, value=0, step=1)
else:
    buffer_size_value = None

power = st.checkbox("Power")
ip = st.text_input("IP")
port = st.text_input("Port")
experiment_dir = st.checkbox("Record Experiment")
docker = st.checkbox("Docker")
cmd = st.text_area("Command")

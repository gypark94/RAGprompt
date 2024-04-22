
# using requests library to check the response
import requests

# GPU_server Test
#from fastapi import FastAPI
#import asyncio
#from fastapi.responses import StreamingResponse
#from streamer import CustomStreamer
#from threading import Thread
#from queue import Queue
#app = FastAPI()


# Warning: tokenizer recognize tab as spaces. Be careful when entering a query
# Prompt format:
#     "<s>[INST] <<SYS>> + instruction + <</SYS>>" + input + " [/INST]"
# Example:
#     "<s>[INST] <<SYS>> From now on, you are a fraud detector.
#      Inputs are financial log data and your role is to detect anomalies.
#      For example, ~ <</SYS>>
#
#      {input} [/INST]"

# Sending the query in the get request parameter
# use_server_inst: Whether to use the instruction set up inside the server
# use_gpu: Whether or not to use GPU ('True' is using a GPU)
# query: User input
use_server_inst = True
use_gpu = True
query = "Here are examples of normal and abnormal vectors are as follows.\n\
Normal:\n\
-0.370617051,0.576894241,-0.424293699,-1.463609352,2.999617246,3.621052828,0.408295343,0.923764155,-0.450935706,-0.866774475,\
-0.082521397,0.019026907,-0.384993971,0.467685263,0.645416843,-0.596680256,-0.213927062,-0.569622006,0.490851072,0.037121297,\
-0.273540923,-0.893992966,-0.228892108,0.667747503,0.748534112,-0.352541627,-0.045398091,-0.067073826\n\
Abnormal:\n\
-1.512515758,1.133138588,-1.60105248,2.813400968,-2.664503406,-0.310371094,-1.520895164,0.852995775,-1.496494506,-4.056292616,\
1.553755868,-2.743551359,1.504540671,-5.428788499,-0.016017123,-3.727187613,-3.946299589,-1.680286443,2.30361261,1.249585563,\
0.729827756,0.485285915,0.567005413,0.323585692,0.040870854,0.825813553,0.414482272,0.267265082\n\
\n\
Now, Analyze whether below vector is normal or not. And explain why.\n\
Input:\n\
2.299315604,-1.326226145,-1.767031005,-1.872642359,-0.614115829,-0.547589943,-0.7799703,-0.12315579,-1.733601357,1.873707008,\
0.245835082,-1.236927997,-1.248471608,0.505324368,-0.352339425,-0.217650645,0.120565494,0.457671727,0.380764359,-0.457384874,\
-0.302032173,-0.653665551,0.266819067,0.188648356,-0.193382218,-0.335411805,-0.046581611,-0.064933721\n\
\n\
Is this input log normal or abnormal?"

# Streaming Test
'''
url = f""

# sending a request and fetching a response which is stored in r
with requests.get(url) as r:
    # printing response of each stream
    for chunk in r.iter_content(128):
        print(chunk.decode('ascii'))
'''

# Non-streaming Test
url = f""
response = requests.get(url)
print(response.text)

# GPU_server Test
"""
@app.get('/query/')
async def llm_outputs(query: str):
    print(f'Query receieved:\n{query}')
    url = f"http://LAN"
    response = requests.get(url)
    output = response.text
    print(f'Output receieved:\n{output}')
    return output
"""

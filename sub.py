import os
token = "ここにdiscordトークンを入力"#@param {type:"string"}
os.environ['TOKEN'] = token

openai_apikey = "ここにOpenAIのAPI Keyを入力"#@param {type:"string"}
os.environ['OPENAI_API'] = openai_apikey

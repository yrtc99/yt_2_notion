from llama_cpp import Llama

# 设置模型路径
MODEL_PATH = "/your/path/to/your/model/STTnotion/mistral-7b-instruct-v0.1.Q4_K_S.gguf" #download your ideal model, I use mistral-7b-instruct-v0.1.Q4_K_S.gguf

# 初始化 LLaMA 模型
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_batch=512)


def generate_summary(text):
    prompt = f"""你是一個會議摘要專家，請用中文為以下文本生成一個簡潔的摘要。摘要應包含3-5個主要要點，每個要點用簡短的句子表達：

{text}

摘要（3-5個要點）：
1. """

    # 生成摘要
    output = llm(prompt, max_tokens=2000, stop=None, echo=False)
    
    # 提取生成的摘要
    summary = output['choices'][0]['text'].strip()

    print("模型输出：")
    print(output)
    print("\n生成的摘要：")
    print(summary)
    
    return summary

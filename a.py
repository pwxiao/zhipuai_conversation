# pip install zhipuai 请先在终端进行安装

from zhipuai import ZhipuAI

client = ZhipuAI(api_key="xxxx")
print("欢迎使用智谱ai")
a=""
while True:
    a = input("root：")
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {
                "role": "user",
                "content": a
            }
        ],
        top_p=0.7,
        temperature=0.95,
        max_tokens=1024,
        stream=True,
    )
    print("智谱ai：",end="")
    for trunk in response:
        print(trunk.choices[0].delta.content,end="")
    print()

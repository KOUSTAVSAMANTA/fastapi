from aitextgen import aitextgen
ai = aitextgen(model_folder="./models/pytorch2/", config="./models/pytorch2/config.json", to_gpu=True)

print("generating")
def gener(text):
    z = ai.generate(n=3,
                prompt='[YOU] : '+text+' \n[BOT] :',
                batch_size=1,
                max_length=50,
                temperature=0.1,
                top_p=0.9,
                return_as_list=True)[0]
    ans = z.split("\n")
    pre=ans[1].split("[BOT] : ")
    return pre[1]
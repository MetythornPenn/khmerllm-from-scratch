# Khmer LLMs from Scratch----


## Instruction
```bash
# install torch & cuda
$ pip install torch --index-url https://download.pytorch.org/whl/cu118

# install dependencies
$ pip install -r requirements.txt

# data preprocessing 
$ python main.py --mode data-prep

# training
$ python main.py --mode train

# inference
$ python main.py --mode infer
```

## Reference code 
- [Andrej Karpathy](https://github.com/karpathy/ng-video-lecture)
- [Infatoshi](https://github.com/Infatoshi/fcc-intro-to-llms)
- [Infatoshi google colab](https://colab.research.google.com/drive/1_7TNpEEl8xjHlr9JzKbK5AuDKXwAkHqj?usp=sharing)

##  Dataset

- [OpenWebText](https://skylion007.github.io/OpenWebTextCorpus/)

## Research Papers:

- [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf)
- [A survery of llms](https://arxiv.org/pdf/2303.18223.pdf)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/pdf/2305.14314.pdf)
- [Zero to GPT](https://github.com/VikParuchuri/zero_to_gpt)


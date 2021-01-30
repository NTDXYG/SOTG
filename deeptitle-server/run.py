from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import pandas as pd
from simpletransformers.classification import ClassificationModel, ClassificationArgs
from simpletransformers.seq2seq import Seq2SeqModel, Seq2SeqArgs
from nltk import word_tokenize
from utils import get_score

deep_scc_model_args = ClassificationArgs(num_train_epochs=10,max_seq_length=300,use_multiprocessing=False)
deep_scc_model = ClassificationModel("roberta", "NTUYG/DeepSCC-RoBERTa", num_labels=19, args=deep_scc_model_args,use_cuda=True)

model_args = Seq2SeqArgs(n_gpu=1)

# 加载本地训练好的模型
java_model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="NTUYG/SOTitle-java-BART",
    args=model_args,
)
csharp_model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="NTUYG/SOTitle-csharp-BART",
    args=model_args,
)
python_model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="NTUYG/SOTitle-python-BART",
    args=model_args,
)
js_model = Seq2SeqModel(
    encoder_decoder_type="bart",
    encoder_decoder_name="NTUYG/SOTitle-js-BART",
    args=model_args,
)

java_title_list = pd.read_csv('data/java_title.csv')['title'].tolist()
csharp_title_list = pd.read_csv('data/c#_title.csv')['title'].tolist()
js_title_list = pd.read_csv('data/js_title.csv')['title'].tolist()
py_title_list = pd.read_csv('data/python_title.csv')['title'].tolist()

app=Flask(__name__) #变量app是Flask的一个实例并且必须传入一个参数，__name__对应的值是__main，即当前的py文件的文件名作为Flask的程序名称，这个也可以自定义，比如，取，'MY_ZHH_APP'                          #__name__是固定写法，主要是方便flask框架去寻找资源 ，也方便flask插件出现错误时，去定位问题
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)
name_file = ['bash', 'c', 'c#', 'c++','css', 'haskell', 'java', 'javascript', 'lua', 'objective-c', 'perl', 'php', 'python','r','ruby', 'scala', 'sql', 'swift', 'vb.net']

from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):

            return float(o)

        super(JSONEncoder, self).default(o)
app.json_encoder = JSONEncoder

@app.route('/hello')      #相当于一个装饰器，视图映射，路由系统生成 视图对应url，这边没有指定method .默认使用get
def first_flask():    #视图函数
    return 'Hello World'  #response，最终给浏览器返回的内容

@app.route('/get_title',methods=['POST'])
def get_title():
    get_data = json.loads(request.get_data(as_text=True))
    code = get_data['code']
    code = code.replace('\n', ' ')
    predictions, raw_outputs = deep_scc_model.predict([code])
    predict = name_file[predictions[0]]
    similarity = []
    if(predict == 'java'):
        describe = get_data['describe']
        describe = describe.replace('\n', ' ')
        code = ' '.join(word_tokenize(code))
        describe = ' '.join(word_tokenize(describe))
        body = describe + ' <code> ' + code + ' </code>'
        title = java_model.predict([body])[0]
        sims = get_score(title, java_title_list)
        for i in sims:
            similarity.append({'title':i[1],'score':"%.2f%%" % (i[0] * 100)})
    elif(predict == 'c#'):
        describe = get_data['describe']
        describe = describe.replace('\n', ' ')
        code = ' '.join(word_tokenize(code))
        describe = ' '.join(word_tokenize(describe))
        body = describe + ' <code> ' + code + ' </code>'
        title = csharp_model.predict([body])[0]
        sims = get_score(title, csharp_title_list)
        for i in sims:
            similarity.append({'title': i[1], 'score': "%.2f%%" % (i[0] * 100)})
    elif(predict == 'javascript'):
        describe = get_data['describe']
        describe = describe.replace('\n', ' ')
        code = ' '.join(word_tokenize(code))
        describe = ' '.join(word_tokenize(describe))
        body = describe + ' <code> ' + code + ' </code>'
        title = js_model.predict([body])[0]
        sims = get_score(title, js_title_list)
        for i in sims:
            similarity.append({'title': i[1], 'score': "%.2f%%" % (i[0] * 100)})
    elif (predict == 'python'):
        describe = get_data['describe']
        describe = describe.replace('\n', ' ')
        code = ' '.join(word_tokenize(code))
        describe = ' '.join(word_tokenize(describe))
        body = describe + ' <code> ' + code + ' </code>'
        title = python_model.predict([body])[0]
        sims = get_score(title, py_title_list)
        for i in sims:
            similarity.append({'title': i[1], 'score': "%.2f%%" % (i[0] * 100)})
    else:
        title = "Sorry, we do not currently support this language."
    result = {'title': title, 'language': predict, 'similarity': similarity}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
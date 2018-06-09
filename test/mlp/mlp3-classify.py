from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import numpy as np #numpy의 array라고 알려주면서 value error를 방지한다.
import json
max_words = 56681 # 입력 단어 수: word-dic.json 파일 참고
nb_classes = 6 # 6개의 카테고리
batch_size = 64
nb_epoch = 20
# MLP 모델 생성하기 --- (※1)
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    return model
# 데이터 읽어 들이기--- (※2)
data = json.load(open("./newstext/data-mini.json")) #데이터 파일은 용량이 커서 올리지 않음...
#data = json.load(open("./newstext/data.json"))
X = data["X"] # 텍스트를 나타내는 데이터
Y = data["Y"] # 카테고리 데이터
# 학습하기 --- (※3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train),len(Y_train))
model = KerasClassifier(
    build_fn=build_model,
    nb_epoch=nb_epoch,
    batch_size=batch_size)
model.fit(np.array(X_train), np.array(Y_train))
# 예측하기 --- (※4)
y = model.predict(np.array(X_test))
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)

#출처 윤인성님의 머신러닝 딥러닝 실전개발입문 (에러가 나서 수정을 좀 했다...)

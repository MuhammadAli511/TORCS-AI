import math
import pandas as pd
from sklearn.model_selection import train_test_split
import statistics
import numpy as np

from sklearn.tree import DecisionTreeClassifier
import sklearn

class carPredict:

    def __init__(self, filename):
        # name=['angle','curLapTime','damage','distFromStart','distRaced','fuel','gear','lastLapTime','opponents','racePos','rpm','speedX','speedY','speedZ','track','trackPos','wheelSpinVel','z','focus','keyPress']
        data = pd.read_csv(filename)
        # data.drop('opponents', inplace=True, axis=1)
        # data.drop('track', inplace=True, axis=1)
        # data.drop('wheelSpinVel', inplace=True, axis=1)
        # data.drop('focus', inplace=True, axis=1)
        # data.drop('fuel', inplace=True, axis=1)
        # data.drop('damage', inplace=True, axis=1)
        # data.drop('gear', inplace=True, axis=1)
        # data.drop('curLapTime', inplace=True, axis=1)
        # data.drop('distFromStart', inplace=True, axis=1)
        # data.drop('distRaced', inplace=True, axis=1)


        data.dropna(axis=0, inplace=True)

        data.drop('curLapTime', inplace=True, axis=1)
        data.drop('damage', inplace=True, axis=1)
        data.drop('distFromStart', inplace=True, axis=1)
        data.drop('distRaced', inplace=True, axis=1)
        data.drop('fuel', inplace=True, axis=1)
        data.drop('gear', inplace=True, axis=1)
        data.drop('lastLapTime', inplace=True, axis=1)
        data.drop('opponents', inplace=True, axis=1)
        data.drop('racePos', inplace=True, axis=1)
        data.drop('z', inplace=True, axis=1)
        data.drop('focus', inplace=True, axis=1)

        # data.drop('speedX', inplace=True, axis=1)
        # data.drop('speedY', inplace=True, axis=1)
        # data.drop('speedZ', inplace=True, axis=1)
        #
        # data.drop('angle', inplace=True, axis=1)
        # data.drop('rpm', inplace=True, axis=1)

        newtrack = []

        for record in data['track']:

            str1 = record[1:-1]
            li = list(str1.split(" "))
            newlist = []
            # print(li)
            for val in li:
                if (val[len(val) - 1] == '\n'):
                    if (val[len(val) - 2] == '\r'):
                        vv = float(val[1:-3])
                    else:
                        vv = float(val[1:-2])
                else:
                    vv = float(val[1:-1])
                newlist.append(vv)

            newtrack.append(newlist)

        newwheel = []

        for record in data['wheelSpinVel']:

            str1 = record[1:-1]
            li = list(str1.split(" "))

            newlist = []
            for val in li:
                if (val[len(val) - 1] == '\n'):
                    if (val[len(val) - 2] == '\r'):
                        vv = float(val[1:-3])
                    else:
                        vv = float(val[1:-2])
                else:
                    vv = float(val[1:-1])
                newlist.append(vv)

            newwheel.append(newlist)

        track1 = []
        track2 = []
        track3 = []
        track4 = []
        track5 = []
        track6 = []
        track7 = []
        track8 = []
        track9 = []
        track10 = []
        track11 = []
        track12 = []
        track13 = []
        track14 = []
        track15 = []
        track16 = []
        track17 = []
        track18 = []
        track19 = []

        for t in newtrack:
            track1.append(t[0])
            track2.append(t[1])
            track3.append(t[2])
            track4.append(t[3])
            track5.append(t[4])
            track6.append(t[5])
            track7.append(t[6])
            track8.append(t[7])
            track9.append(t[8])
            track10.append(t[9])
            track11.append(t[10])
            track12.append(t[11])
            track13.append(t[12])
            track14.append(t[13])
            track15.append(t[14])
            track16.append(t[15])
            track17.append(t[16])
            track18.append(t[17])
            track19.append(t[18])

        wheelSpinvel1 = []
        wheelSpinvel2 = []
        wheelSpinvel3 = []
        wheelSpinvel4 = []

        for w in newwheel:
            wheelSpinvel1.append(w[0])
            wheelSpinvel2.append(w[1])
            wheelSpinvel3.append(w[2])
            wheelSpinvel4.append(w[3])
        #
        data['track1'] = track1
        data['track2'] = track2
        data['track3'] = track3
        data['track4'] = track4
        data['track5'] = track5
        data['track6'] = track6
        data['track7'] = track7
        data['track8'] = track8
        data['track9'] = track9
        data['track10'] = track10
        data['track11'] = track11
        data['track12'] = track12
        data['track13'] = track13
        data['track14'] = track14
        data['track15'] = track15
        data['track16'] = track16
        data['track17'] = track17
        data['track18'] = track18
        data['track19'] = track19

        data['wheelSpinVel1'] = wheelSpinvel1
        data['wheelSpinVel2'] = wheelSpinvel2
        data['wheelSpinVel3'] = wheelSpinvel3
        data['wheelSpinVel4'] = wheelSpinvel4
        # #
        data.drop('track', inplace=True, axis=1)
        data.drop('wheelSpinVel', inplace=True, axis=1)

        keyP = data.pop('keyPress')
        data['keyPress'] = keyP



        #print(data)



        self.traindata = data
        


        train_features = self.traindata.iloc[:52060, :-1]
        train_targets = self.traindata.iloc[:52060, -1]

        self.tree = DecisionTreeClassifier(criterion='entropy').fit(train_features, train_targets)

      
        self.k=3

    def newPrediction(self, test):

        # test.drop('opponents', inplace=True, axis=1)
        # test.drop('track', inplace=True, axis=1)
        # test.drop('wheelSpinVel', inplace=True, axis=1)
        # test.drop('focus', inplace=True, axis=1)
        # test.drop('fuel', inplace=True, axis=1)
        # test.drop('damage', inplace=True, axis=1)
        # test.drop('gear', inplace=True, axis=1)
        # test.drop('curLapTime', inplace=True, axis=1)
        # test.drop('distFromStart', inplace=True, axis=1)
        # test.drop('distRaced', inplace=True, axis=1)

        test.drop('curLapTime', inplace=True, axis=1)
        test.drop('damage', inplace=True, axis=1)
        test.drop('distFromStart', inplace=True, axis=1)
        test.drop('distRaced', inplace=True, axis=1)
        test.drop('fuel', inplace=True, axis=1)
        test.drop('gear', inplace=True, axis=1)
        test.drop('lastLapTime', inplace=True, axis=1)
        test.drop('opponents', inplace=True, axis=1)
        test.drop('racePos', inplace=True, axis=1)
        test.drop('z', inplace=True, axis=1)
        test.drop('focus', inplace=True, axis=1)

        # test.drop('speedX', inplace=True, axis=1)
        # test.drop('speedY', inplace=True, axis=1)
        # test.drop('speedZ', inplace=True, axis=1)
        #
        # test.drop('angle', inplace=True, axis=1)
        # test.drop('rpm', inplace=True, axis=1)

        for record in test['track']:
            test['track1'] = record[0]
            test['track2'] = record[1]
            test['track3'] = record[2]
            test['track4'] = record[3]
            test['track5'] = record[4]
            test['track6'] = record[5]
            test['track7'] = record[6]
            test['track8'] = record[7]
            test['track9'] = record[8]
            test['track10'] = record[9]
            test['track11'] = record[10]
            test['track12'] = record[11]
            test['track13'] = record[12]
            test['track14'] = record[13]
            test['track15'] = record[14]
            test['track16'] = record[15]
            test['track17'] = record[16]
            test['track18'] = record[17]
            test['track19'] = record[18]

        for record in test['wheelSpinVel']:
            test['wheelSpinVel1'] = record[0]
            test['wheelSpinVel2'] = record[1]
            test['wheelSpinVel3'] = record[2]
            test['wheelSpinVel4'] = record[3]

        test.drop('track', inplace=True, axis=1)
        test.drop('wheelSpinVel', inplace=True, axis=1)

       # print(test)



        prediction = self.tree.predict(test)

        return prediction[0]







from .DBConnection import DBConnection
from .CountWords import CountWords

class tf:

    def calc(topic):
        res=dict({})
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select * from app_questions")
        row = cursor.fetchall()
        topic=topic.lower()
        topic=topic.split()
        for r in row:
            id = r[1]
            q_n = r[2]
            matched=0
            for word in topic:
                matched=matched+CountWords.countOccurences(q_n,word)
            tf=matched/len(topic)

            if tf>0.5:
                res[id]=tf



        sorted_dict = dict( sorted(res.items(),
                           key=lambda item: item[1],
                           reverse=True))
        print(sorted_dict)
        if(len(sorted_dict)>0):
            val = [elem[0] for elem in sorted_dict.items()]
            return val[0]
        else:
            return -1





            

if __name__ == '__main__':
    print(tf.calc('hi'))
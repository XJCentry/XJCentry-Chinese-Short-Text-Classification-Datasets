# with open('toutiao_cat_data.txt','r',encoding='utf-8') as f:
#     all=f.readlines()
#     for each in all:
#         details=each.replace('\n','').split('_!_')
#         with open('all.txt','a',encoding='utf-8') as ff:
#             ff.write(details[3].replace('\t','')+'\t'+details[2]+'\n')


'''
                    content
class                      
news_agriculture      19322
news_car              35785
news_culture          28031
news_edu              27058
news_entertainment    39396
news_finance          27085
news_game             29300
news_house            17672
news_military         24984
news_sports           37568
news_story             6273
news_tech             41543
news_travel           21422
news_world            26909
stock                   340

'''
dict={

'news_agriculture' :0,
'news_car'          :1,
'news_culture'      :2,
'news_edu'          :3,
'news_entertainment' :4,
'news_finance'       :5,
'news_game'          :6,
'news_house'         :7,
'news_military'      :8,
'news_sports'        :9,
'news_tech'         :10,
'news_travel'         :11,
'news_world'         :12

}
import pandas as pd

df=pd.read_csv('all.txt', sep='\t', names=['content', 'class'])
# print(df.groupby(by='class').count())
traincount=15000
testcount=1000
valcount=1000
for each in dict:
    # print(each,dict[each])
    each_df=df[df['class']==each]
    # print(type(each_df))
    for i in range(len(each_df)):
        if i<traincount:
            # print(each_df.iloc[i][0])
            content=each_df.iloc[i][0]
            label_id=dict[each]
            with open('train.txt', 'a', encoding='utf-8') as train_f:
                train_f.write(content+'\t'+str(label_id)+'\n')
        elif i<traincount+testcount:
            # print(each_df.iloc[i][0])
            content=each_df.iloc[i][0]
            label_id=dict[each]
            with open('test.txt', 'a', encoding='utf-8') as train_f:
                train_f.write(content+'\t'+str(label_id)+'\n')
        elif i<traincount+testcount+valcount:
            # print(each_df.iloc[i][0])
            content=each_df.iloc[i][0]
            label_id=dict[each]
            with open('dev.txt', 'a', encoding='utf-8') as train_f:
                train_f.write(content+'\t'+str(label_id)+'\n')




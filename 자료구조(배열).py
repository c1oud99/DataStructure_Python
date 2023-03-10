#!/usr/bin/env python
# coding: utf-8

# ## 꼭 알아둬야 할 자료 구조: 배열 (Array)
# * 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# * 파이썬에서는 리스트 타입이 배열 기능을 제공함

# ### 1. 배열은 왜 필요할까?
# - 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
# - 같은 종류의 데이터를 순차적으로 저장
# - 장점: 
#   - 빠른 접근 가능
#     - 첫 데이터의 위치에서 상대적인 위치로 데이터 접근(인덱스 번호로 접근)
# - 단점: 
#   - 데이터 추가/삭제의 어려움
#     - 미리 최대 길이를 지정해야 함
#   
# > 엑셀로 이해해보기

# #### C 언어 예: 영어 단어 저장
#include <stdio.h>

int main(int argc, char * argv[])
{
    char country[3] = "US";
    printf ("%c%c\n", country[0], country[1]);
    printf ("%s\n", country);    
    return 0;
}
# #### 파이썬 언어 예: 영어 단어 저장

# In[2]:


country = 'US'
print (country)


# ### 2. 파이썬과 배열
# - 파이썬에서는 리스트로 배열 구현 가능

# In[2]:


# 1차원 배열: 리스트로 구현시
data = [1, 2, 3, 4, 5]
data


# In[4]:


# 2차원 배열: 리스트로 구현시
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data


# In[5]:


print (data[0])

print (data[0][0])
print (data[0][1])
print (data[0][2])
print (data[1][0])
print (data[1][1])


# ### 3. 프로그래밍 연습 

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습1: 위의 2차원 배열에서 9, 8, 7 을 순서대로 출력해보기</font></strong><br>
# </div>

# In[6]:


print(data[2][2], data[2][1], data[2][0])


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="3em">연습2: 아래의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기</font></div>

# In[ ]:


dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',A
'Moran, Mr. James',
'McCarthy, Mr. Timothy JA
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. FatimaA
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg DaniraA',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']


# In[40]:


m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print (m_count)


# ### 참고
# * range(stop): range(10)은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# * range(start, stop): range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# * range(start, stop, step): range(0, 20, 2)은 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
#   - start, stop, step은 음수로 지정 가능

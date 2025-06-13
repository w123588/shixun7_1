import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='南宁必吃榜')

df = pd.DataFrame({
    "latitude":[22.833023,22.849208,22.814160,22.818192,22.830622],
    "longitude":[108.403855,108.320469,108.321510,108.292848,108.371383]})
# 设置索引列的名称
df.index.name='序号'

st.subheader('南宁地图')

st.map(df)

st.title('⭐餐厅评分')
# 定义数据,以便创建数据框
data = {
    '门店':['中国兰州拉面', '隆江猪脚饭', '海底捞火锅','肯德基','必胜客'],
    '评分':[4.8, 4.5, 4.7,4.3,4.4],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为条形图的x轴
df_indexed = df.set_index('门店')
st.bar_chart(df_indexed)

st.title('💰不同类型餐厅价格')
# 定义数据,以便创建数据框
data = {
    '月份': ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
    '中国兰州拉面(在水一方店)': [20, 15, 18, 46, 56, 43, 59, 55, 44, 77, 88, 95],
    '王记隆江猪脚饭(万秀村店)': [12, 16, 12, 46, 64, 42, 49, 95, 34, 67, 48, 15],
    '海底捞火锅(百盛步行街店)': [110, 100, 120, 46, 54, 43, 49, 55, 124, 77, 86, 75],
    '肯德基(新阳店)': [11, 16, 10, 69, 54, 62, 49, 95, 94, 67, 80, 45],
    '必胜客(WOW青秀万达店)': [10, 19, 60, 66, 54, 32, 49, 46, 64, 70, 81, 75]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 通过y参数筛选只显示2、3号门店的数据
st.line_chart(df, y=['中国兰州拉面(在水一方店)','王记隆江猪脚饭(万秀村店)','海底捞火锅(百盛步行街店)','肯德基(新阳店)','必胜客(WOW青秀万达店)'])

st.title('🍲用餐高峰时段')
# 定义数据,以便创建数据框
data = {
    '时间':['9','10','11', '12', '13','14','15'],
    '中国兰州拉面':[97,121,134, 189, 180,177,114],
    '隆江猪脚饭':[76,97,120, 174, 156,144,113],
    '海底捞火锅':[71,81,110, 211, 198,149,97],
    '肯德基':[104,95,140, 178, 190,113,94],
    '必胜客':[111,86,160, 170, 184,99,104],
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5,6,7], name='序号')
# 将新索引应用到数据框上
df.index = index

# 通过x指定月份所在这一列为面积图的x轴
df_indexed = df.set_index('时间')
st.area_chart(df_indexed)

st.title('🍽餐厅详情')
with st.expander("海底捞火锅(百盛步行街店)"):
        c1, c2= st.columns(2)
        c1.markdown('## 海底捞火锅(百盛步行街店)')
        c1.markdown('##### 评分')
        c1.markdown('# 4.9/5.0')
        c1.markdown('#### 人均消费')
        c1.markdown('# 35000元')

        c2.markdown('**推荐菜品：**')
        c2.markdown(' • &#8194;蟹棒虾滑肥牛卷')
        c2.markdown(' • &#8194;芝麻白糖年糕')
        c2.markdown(' • &#8194;牛肉豆花')


st.subheader('当前拥挤程度')
st.progress(99,text="99%拥挤")


st.title('😍今日推荐')
st.markdown("<span style='color:red; border:2px solid red; border-radius:8px; padding:4px;'>干饭首选👍</span>", unsafe_allow_html=True)

# 初始化会话状态
if 'count' not in st.session_state:
    st.session_state.count = 0

count = 0;
if st.button(' :red[今天吃什么 --点我点我！！！]'):
	st.session_state.count += 1
	if st.session_state.count % 6 == 1:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：中国兰州拉面</span>", unsafe_allow_html=True)
		st.markdown("![中国兰州拉面](https://x0.ifengimg.com/ucms/2021_34/15C767BF261DF9EFA084B2374F55E18199D0FD57_size137_w1080_h1623.jpg)")
	if st.session_state.count % 6 == 2:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：王记隆江猪脚饭</span>", unsafe_allow_html=True)
		st.markdown("![王记隆江猪脚饭](https://tse4-mm.cn.bing.net/th/id/OIP-C.-k_asvs8q7pV6L0SErCCDwHaE8?rs=1&pid=ImgDetMain)")
	if st.session_state.count % 6 == 3:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：海底捞火锅(百盛步行街店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://zhongces3.sina.com.cn/product/20221028/0d0599ab2717311cb7d955ac428c42e1.jpeg)")
	if st.session_state.count % 6 == 4:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：肯德基(新阳店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://ts1.tc.mm.bing.net/th/id/R-C.7f7abab1305b51bd7d4a4aed9929c27f?rik=QF7KU3Lt0HyAng&riu=http%3a%2f%2fsu.bcebos.com%2fb2b-jiameng%2fonline%2f8be0d455-22f2-4cfd-be79-065fb5ae462a&ehk=vavYn4edBcz1n6BoGMnr2GuqWgkTSpKLMBikBB5J8Fo%3d&risl=&pid=ImgRaw&r=0)")
	if st.session_state.count % 6 == 5:
		st.markdown("<span style='border-radius: 8px; display: inline-block;width: 800px; padding: 8px 16px;background-color:green;'>今日推荐：必胜客(WOW青秀万达店)</span>", unsafe_allow_html=True)
		st.markdown("![图片](https://tse4-mm.cn.bing.net/th/id/OIP-C.OvojXjmhI5Ll4vaFZaXsPgHaLG?rs=1&pid=ImgDetMain)")

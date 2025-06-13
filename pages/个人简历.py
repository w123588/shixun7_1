import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title='💼个人简历生成器',layout='wide')
st.title("🎨个人简历生成器")
st.caption('使用Streamlit创建您的个性化简历')

# 判断内存中（session_state中）有没有a
if 'sex' not in st.session_state:
	st.session_state.sex = ''
if 'languages' not in st.session_state:
	st.session_state.languages = ''
if 'degree' not in st.session_state:
	st.session_state.degree = ''
if 'skills' not in st.session_state:
	st.session_state.skills = ''
	
def str1(l):
    s = ""
    for i in l:
        s += str(i) + ' '
    return s

data = [{
    'sex':('男','女'),
    'degree':('','小学', '初中', '高中', '职校', '本科', '高职', '中专', '中本'),
    'languages':('中文', '英语', '日语', '法语', '韩语', '德语'),
    'skills':('C', 'C++', 'Pythono', 'Java', 'R语言', 'WPS')
    }]

c1,c2=st.columns([1,1])

with c1:
    st.header('个人信息表单')
    st.markdown("""<hr style="height:2px;border-width:0;color:blue;background-color:blue">""", unsafe_allow_html=True)
    name = st.text_input('姓名', autocomplete='name')

    loction = st.text_input('职位', autocomplete='loction')

    telephone = st.text_input('电话', autocomplete='telephone')
    yx= st.text_input('邮箱', autocomplete='yx')
     
    date1 = st.date_input("出生日期", value=None)

    st.session_state.sex = st.radio('性别',data[0]['sex'],horizontal=True,)
    degree = st.selectbox('学历：', data[0]['degree'], index=0)
    st.session_state.languages = st.multiselect('语言能力',data[0]['languages'],)
    st.session_state.skills = st.multiselect('技能',data[0]['skills'],)
    year = st.slider('工作经验/年', 0, 10000, 1)
    st.write(year)
    salary = st.slider('选择薪资待遇/元',0.0, 1000000.0, (25.0, 7500.0))
    st.write('你选择的范围是：', salary)
    st.subheader("示例2")
    if 'init_text' not in st.session_state:
        st.session_state['init_text'] ="" 
      
    jj=st.text_area(label='个人简历', placeholder='请简要介绍您的专业背景,职业目标和个人特点...', value='',height=200, max_chars=200)
    w1 = st.time_input("每日最佳联系时间段")


# 文件上传功能
    uploaded_file = st.file_uploader("选择一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 显示上传的图片
    st.image(uploaded_file, caption="上传的照片", use_column_width=True)
    
    # 保存上传的文件到本地
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("文件保存成功！")

with c2:
    st.header('简历实时预览')
    st.markdown("""<hr style="height:2px;border-width:0;color:blue;background-color:blue">""", unsafe_allow_html=True)
    
    c11,c22=st.columns([1,1])
    with c11:
        st.write(f'职位：{st.session_state.sex}')
        st.write(f'电话：{telephone}')
        st.write(f'邮箱：{yx}')
        st.write(f'出生日期:{date1}')
        st.write(f'最佳联系时间：{w1}')
    with c22:
        st.write(f'性别：{st.session_state.sex}')
        st.write(f'学历：{st.session_state.degree}')
        st.write(f'工作经验：{year}年')
        st.write(f'期望薪资：{salary}元')
        st.write(f'语言能力：{str1(st.session_state.languages)}')
        st.write(f'技能：{str1(st.session_state.skills)}')
    st.markdown('***')
    st.header('个人简介')

    st.text(f'{jj}')
    st.markdown('***')



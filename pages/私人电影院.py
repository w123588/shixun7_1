import streamlit as st

st.set_page_config(page_title='MY视频播放', page_icon='🔞')

st.title('📽MY视频分享库')
st.text('Please点击任意视频播放')

# 判断内存中（session_state中）有没有a
if 'count1' not in st.session_state:
	st.session_state.count1 = 0

# 读取视频数据
video_file = 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'
video_1 = [{'url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
	'title':'班尼特',
	'time':'0.10s',
	'describe':'班尼特看蝴蝶被苹果砸死',
	'class': '动漫',
	'author':'《守护者联盟》',
	'introduction':'斑驳树影里，班尼特仰头追逐一只翩跹的菜粉蝶。高枝熟透的苹果悄然松动，裹着风直坠——蝶翅银鳞正巧拂过果核，“啵”地轻响，金黄果肉爆裂处，斑斓的翅尖抽搐着嵌进果核褶皱，蜜汁混着磷粉淌过班尼特僵直的手指。那蝶至死都不曾知晓，一次寻常的越顶飞行，竟撞碎了牛顿与厄运的共谋。'},
	{'url': 'https://www.w3schools.com/html/movie.mp4',
	'title':'熊和鸽子',
	'time':'0.12s',
	'describe':'熊和鸽子自然相处',
	'class': '自然',
	'author':'《动物世界》',
	'introduction':'河水清浅处，棕熊踏着碎波踱步，水花漫过它的厚毛。几只白鸽在近旁石上梳理湿羽，或展翅轻掠水面，翅尖几乎点破倒影。熊影与鸽影在涟漪中晃动交错，笨重与灵巧在流水声里达成奇异的安宁。'},
	{'url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
	'title':'Sintel',
	'time':'0.52s',
	'describe':'sintel的女龙寻找她失散的龙宝宝的故事',
	'class': '动漫',
	'author':'由blender基金会',
	'introduction':'Sintel中，女孩捡到受伤小龙，养大后小龙被大龙抓走，她跋山涉水寻找，却误杀大龙，发现真相后掩面痛哭。'}]

def my_format_func(option):
	return f'{option}'

video_class = st.selectbox('选择类别:',['全部', '分类1', '分类2', '分类3'],format_func=my_format_func,index=0)

if video_class == '全部':
	st.subheader(video_1[0]['title'])
	st.video(video_1[0]['url'], )
	with st.expander("视频详情"):
		st.header(video_1[0]['title'])
		st.text(video_1[0]['describe'])
		st.text(video_1[0]['class']+' '+'|'+' '+video_1[0]['time']+' '+'|'+' '+video_1[0]['author']) 
		st.text(video_1[0]['introduction'])
	st.subheader(video_1[1]['title'])
	st.video(video_1[1]['url'], )
	with st.expander("视频详情"):
		st.header(video_1[1]['title'])
		st.text(video_1[1]['describe'])
		st.text(video_1[1]['class']+' '+'|'+' '+video_1[1]['time']+' '+'|'+' '+video_1[1]['author'])
		st.text(video_1[1]['introduction'])
	st.subheader(video_1[2]['title'])
	st.video(video_1[2]['url'],) 
	with st.expander("视频详情"):
		st.header(video_1[2]['title'])
		st.text(video_1[2]['describe'])
		st.text(video_1[2]['class']+' '+'|'+' '+video_1[2]['time']+' '+'|'+' '+video_1[2]['author'])
		st.text(video_1[2]['introduction'])
elif video_class == '分类1':
	st.subheader(video_1[0]['title'])
	st.video(video_1[0]['url'], ) 
	with st.expander("视频详情"):
		st.header(video_1[0]['title'])
		st.text(video_1[0]['describe'])
		st.text(video_1[0]['class']+' '+'|'+' '+video_1[0]['time']+' '+'|'+' '+video_1[0]['author'])
		st.text(video_1[0]['introduction'])
elif video_class == '分类2':
	st.subheader(video_1[1]['title'])
	st.video(video_1[1]['url'], )
	with st.expander("视频详情"):
		st.header(video_1[1]['title'])
		st.text(video_1[1]['describe'])
		st.text(video_1[1]['class']+' '+'|'+' '+video_1[1]['time']+' '+'|'+' '+video_1[1]['author'])
		st.text(video_1[1]['introduction'])
elif video_class == '分类3':
	st.subheader(video_1[2]['title'])
	st.video(video_1[2]['url'], ) 
	with st.expander("视频详情"):
		st.header(video_1[2]['title'])
		st.text(video_1[2]['describe'])
		st.text(video_1[2]['class']+' '+'|'+' '+video_1[2]['time']+' '+'|'+' '+video_1[2]['author'])
		st.text(video_1[2]['introduction'])



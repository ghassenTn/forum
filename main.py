import streamlit as st


def get_like_nb(nb=1):
    nb = nb + 1
    return nb
st.markdown("## Debian Community .")
st.caption("By @DebianCommunity :material/forum:")
### news about new release
for x in range(7):
    cnt_news = st.container(border=True)
    with cnt_news:
        st.markdown("**News about new release**")
        st.markdown("""
        - [Debian 11 Bullseye](https://www.debian.org/News/2021/20210814)
                - [Debian 10 Buster](https://www.debian.org/News/2019/20190706)
                - [Debian 9 Stretch](https://www.debian.org/News/2017/20170617)
                - [Debian 8 Jessie](https://www.debian.org/News/2015/20150426)
                - [Debian 7 Wheezy](https://www.debian.org/News/2013/20130504)
                - [Debian 6 Squeeze](https://www.debian.org/News/2011/20110205)
                - [Debian 5 Lenny](https://www.debian.org/News/2009/20090214)  
                    """)
        cols = st.columns([1,1,15],gap='small')
        dislike_count = 0
        if 'dislike_count' not in st.session_state:
            st.session_state['dislike_count'] = dislike_count
        if cols[0].button(f'{st.session_state["dislike_count"]} :material/thumb_down:', key=f'dislike{x}',type='tertiary'):
            st.session_state['dislike_count'] = get_like_nb(st.session_state['dislike_count'])
        like_count = 0
        if 'like_count' not in st.session_state:
            st.session_state['like_count'] = like_count
        if cols[1].button(f'{st.session_state["like_count"]} :material/thumb_up:', key=f'like{x}',type='tertiary'):
            st.session_state['like_count'] = get_like_nb(st.session_state['like_count'])
        comment_count = 0
        if 'comment_count' not in st.session_state:
            st.session_state['comment_count'] = comment_count
        with cols[2]:
            btn = st.button(f'{st.session_state["comment_count"]} :material/comment:', key=f'comment{x}',type='tertiary')
        if btn:    
            comentaire = st.text_area("Commentaire")
            st.session_state['comment_count'] = get_like_nb(st.session_state['comment_count'])
            
    


    
            
    
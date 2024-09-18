import streamlit as st
import requests
import io
from docx import Document
from PIL import Image

st.set_page_config(page_title="佛法修行", layout="wide")

cc = OpenCC('s2t')  # Simplified to Traditional

# Custom CSS for the golden yellow text, responsive video, and larger content text
st.markdown("""
    <style>
    .golden-text {
        font-size: 24px;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
    }
    .video-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
        height: 0;
        overflow: hidden;
    }
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .large-content {
        font-size: 20px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("佛法修行")

# Adding the text in large, bold, golden yellow font
st.markdown("""
    <p class="golden-text">
    願以此功德，莊嚴佛淨土，<br>
    上報四重恩，下濟三途苦。<br>
    若有見聞者，悉發菩提心，<br>
    盡此一報身，同生極樂國。
    </p>
    """, unsafe_allow_html=True)

def main():
    # Sidebar
    st.sidebar.title("修行內容")
    # 迴向 section
    st.sidebar.header("迴向")
    if st.sidebar.button("迴向偈"):
        display_hui_xiang_ji()
    
    # 持咒 section
    st.sidebar.header("持咒")
    if st.sidebar.button("藥師咒"):
        display_medicine_buddha_mantra()
    if st.sidebar.button("大悲咒"):
        display_great_compassion_mantra()
    
    # 三想破瓦法 section
    st.sidebar.header("三想破瓦法")
    if st.sidebar.button("破瓦法"):
        display_phowa_practice()

def fetch_docx_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        doc = Document(io.BytesIO(response.content))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except requests.exceptions.RequestException as e:
        return f"無法獲取文件內容。錯誤：{str(e)}"
    except Exception as e:
        return f"處理文件時出錯。錯誤：{str(e)}"

def display_hui_xiang_ji():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%9B%9E%E5%90%91%E5%81%88.docx"
    content = fetch_docx_content(url)
    
    st.header("迴向偈")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("更多資訊：")
    st.markdown("[迴向偈 - 星雲大師著作全集](https://books.masterhsingyun.org/ArticleDetail/artcle9851)")

def display_medicine_buddha_mantra():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E8%97%A5%E5%B8%AB%E5%92%92.docx"
    content = fetch_docx_content(url)
    
    st.header("藥師咒")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("藥師咒影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/5UnbgjkbgUI?start=1218&end=1242" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("影片來源：")
    st.markdown("[藥師咒 - YouTube](https://www.youtube.com/watch?v=5UnbgjkbgUI&t=1218s)")

def display_great_compassion_mantra():
    url = "https://github.com/jasonckb/Buddha/raw/main/%E5%A4%A7%E6%82%B2%E5%92%92.docx"
    content = fetch_docx_content(url)
    
    st.header("大悲咒")
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    st.write("大悲咒影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/Hr9zmoDWppA?start=0&end=162" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("影片來源：")
    st.markdown("[大悲咒 - YouTube](https://www.youtube.com/watch?v=Hr9zmoDWppA)")

def display_phowa_practice():
    st.header("三想破瓦法")
    
    # Display image
    image_url = "https://github.com/jasonckb/Buddha/raw/main/%E4%B8%89%E6%83%B3%E7%A0%B4%E7%93%A6%E6%B3%95.jpg"
    response = requests.get(image_url)
    img = Image.open(io.BytesIO(response.content))
    st.image(img, use_column_width=True)
    
    # Display content from docx file
    url = "https://github.com/jasonckb/Buddha/raw/main/%E4%B8%89%E6%83%B3%E7%A0%B4%E7%93%A6%E6%B3%95.docx"
    content = fetch_docx_content(url)
    st.markdown(f'<div class="large-content">{content}</div>', unsafe_allow_html=True)
    
    # Display source
    st.write("文字來源：")
    st.markdown("[三想破瓦法 - 佛教在线](http://read.goodweb.net.cn/news/news_view.asp?newsid=74024)")
    
    # Display video
    st.write("破瓦法影片：")
    st.markdown("""
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/wDVoBVC5s2c?start=536&end=2375" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    # Display video source
    st.write("影片來源：")
    st.markdown("[破瓦法 - YouTube](https://www.youtube.com/watch?v=wDVoBVC5s2c&t=1072s)")

if __name__ == "__main__":
    main()

import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st
from io import StringIO
from dotenv import load_dotenv

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def fetch_firms_csv():
    map_key = "USA"
    sensor = "VIIRS_SNPP_NRT"
    day_range = 1

    api_key = "DEMO_KEY"  # 测试用公开key

    url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{map_key}/{sensor}/{day_range}?key={api_key}"
    st.write("Request URL:", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.error(f"Failed to fetch data from NASA: {e}")
        return None


def main():
    st.title("AidSense: Multimodal Disaster Response AI System")
    st.sidebar.title("AidSense Configuration")

    # 显示API状态
    if NASA_API_KEY:
        st.sidebar.success("NASA API Key loaded")
    else:
        st.sidebar.error("NASA API Key missing!")

    csv_data = fetch_firms_csv()

    if csv_data:
        try:
            df = pd.read_csv(StringIO(csv_data))

            # 确保至少有经纬度字段
            if 'latitude' not in df.columns or 'longitude' not in df.columns:
                st.error("NASA returned unexpected data format.")
                st.code(csv_data[:1000])  # 打印错误返回内容
                return

            st.success(f"✅ Latest fire detections: {len(df)} points")

            # 准备绘图参数
            plot_args = {
                "lat": "latitude",
                "lon": "longitude",
                "zoom": 3,
                "mapbox_style": "open-street-map",
                "title": "NASA FIRMS Fire Hotspots (USA)"
            }

            # 动态添加颜色、大小字段
            if "confidence" in df.columns:
                plot_args["color"] = "confidence"
            if "brightness" in df.columns:
                plot_args["size"] = "brightness"
                plot_args["size_max"] = 15

            fig = px.scatter_mapbox(df, **plot_args)
            st.plotly_chart(fig, use_container_width=True)

            # 可选：显示部分表格
            with st.expander("Show raw data"):
                st.dataframe(df.head(20))

        except Exception as e:
            st.error(f"Failed to parse or plot data: {e}")
            st.code(csv_data[:1000])
    else:
        st.warning("No data received from NASA.")

if __name__ == "__main__":
    main()


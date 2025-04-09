import requests
from bs4 import BeautifulSoup
import json

def get_zhihu_hot():
    """获取知乎热榜"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 获取知乎热榜
        url = 'https://www.zhihu.com/hot'
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        hot_items = soup.select('.HotList-item')
        
        results = []
        for item in hot_items:
            try:
                title_element = item.select_one('.HotItem-title')
                if title_element:
                    title = title_element.text.strip()
                    link = title_element.parent.get('href')
                    
                    # 获取热度
                    metrics = item.select_one('.HotItem-metrics')
                    hot_value = metrics.text.strip() if metrics else ""
                    
                    results.append({
                        "title": title,
                        "link": link,
                        "hot_value": hot_value
                    })
            except Exception as e:
                print(f"解析单个热点出错: {e}")
        
        return results
    except Exception as e:
        print(f"获取知乎热榜失败: {e}")
        return []

if __name__ == "__main__":
    hot_topics = get_zhihu_hot()
    print(json.dumps(hot_topics, ensure_ascii=False, indent=2)) 
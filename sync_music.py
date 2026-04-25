#!/usr/bin/env python3
"""GitHub Music Sync Script - 自动扫描音乐目录，更新 music.js"""
import os, json, datetime

# 使用脚本所在目录作为基准，保证在任何环境（本地/CI）都能正确运行
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(SCRIPT_DIR, "音乐")
JS_PATH = os.path.join(SCRIPT_DIR, "music.js")
BASE_URL = "https://cdn.jsdelivr.net/gh/ERX399/ker@main/音乐/"
EXTS = ('.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac', '.wma', '.webm')

def scan_music():
    """扫描目录，返回歌曲文件名列表"""
    if not os.path.isdir(MUSIC_DIR):
        print(f"[ERROR] 目录不存在: {MUSIC_DIR}")
        return []
    files = []
    for f in sorted(os.listdir(MUSIC_DIR)):
        if f.lower().endswith(EXTS) and not f.startswith('.'):
            files.append(f)
    return files

def generate_js(files):
    """生成 music.js 内容"""
    items = []
    for f in files:
        name = os.path.splitext(f)[0].replace('"', '\\"')
        items.append('        { name: "%s", url: "%s" }' % (name, f.replace('"', '\\"')))
    
    return """// ker/music.js
// 通用型列表配置 - 可供任何项目接入使用
// 使用方式：<script src="https://cdn.jsdelivr.net/gh/ERX399/ker@main/music.js"></script>

(function () {
  const CONFIG = {
    baseUrl: '%s',
    items: [
%s
    ]
  };

  const fullList = CONFIG.items.map(item => ({
    name: item.name,
    url: CONFIG.baseUrl + item.url,
    n: item.name,
    u: CONFIG.baseUrl + item.url
  }));

  window.KER_MUSIC = {
    base: CONFIG.baseUrl,
    baseUrl: CONFIG.baseUrl,
    songs: fullList,
    items: fullList,
    list: fullList,
    getByName: function(name) { return fullList.find(item => item.name === name); },
    getByIndex: function(index) { return fullList[index]; },
    count: fullList.length
  };

  window.MUSIC = window.KER_MUSIC;
  window.MUSIC_CONFIG_SOURCE = window.KER_MUSIC;

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = window.KER_MUSIC;
  }

  console.log('[KER Music] 已加载 ' + fullList.length + ' 首歌曲');
})();""" % (BASE_URL, ",\n".join(items))

def main():
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始同步...")
    files = scan_music()
    if not files:
        print("[WARN] 未找到任何音乐文件，跳过更新")
        return
    
    # 读旧内容
    old_content = ""
    if os.path.exists(JS_PATH):
        with open(JS_PATH, 'r', encoding='utf-8') as f:
            old_content = f.read()
    
    new_content = generate_js(files)
    
    if old_content == new_content:
        print(f"[OK] 无变化 ({len(files)} 首歌曲)")
        return
    
    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[OK] 已更新 music.js ({len(files)} 首歌曲)")

if __name__ == '__main__':
    main()

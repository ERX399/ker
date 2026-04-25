// ker/music.js
// 通用型列表配置 - 可供任何项目接入使用
// 使用方式：<script src="https://cdn.jsdelivr.net/gh/ERX399/ker@main/music.js"></script>

(function () {
  const CONFIG = {
    baseUrl: 'https://cdn.jsdelivr.net/gh/ERX399/ker@main/音乐/',
    items: [
        { name: "I Can't Wait", url: "I Can't Wait.mp3" },
        { name: "リテラチュア", url: "リテラチュア.mp3" },
        { name: "你最近还好吗", url: "你最近还好吗.mp3" },
        { name: "嘘月", url: "嘘月.mp3" },
        { name: "带我走", url: "带我走.mp3" },
        { name: "我们", url: "我们.mp3" },
        { name: "我愛你", url: "我愛你.mp3" },
        { name: "星茶会", url: "星茶会.mp3" },
        { name: "爱你", url: "爱你.mp3" },
        { name: "知我", url: "知我.mp3" },
        { name: "还是会想你", url: "还是会想你.mp3" },
        { name: "雨爱", url: "雨爱.mp3" },
        { name: "鸟之诗-八音盒", url: "鸟之诗-八音盒.mp3" }
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
})();
# 图片 API 接入教程

## 引入脚本

在页面中引入本站的 `random.js`：

```html
<script src="https://img.399520.xyz/random.js"></script>
```

## 用法

### img 标签

```html
<!-- 横屏图片 -->
<img alt="random:h" />

<!-- 竖屏图片 -->
<img alt="random:v" />
```

脚本会自动把 `alt="random:h"` 或 `alt="random:v"` 的 img 标签替换为随机图片。

### 背景图

```html
<div data-random-bg="h"></div>
<div data-random-bg="v"></div>
```

引入脚本后元素会自动设置背景图。

### JavaScript API

脚本暴露两个全局函数，直接调用即可拿到图片 URL：

```javascript
getRandomPicH()  // 横屏 URL
getRandomPicV()  // 竖屏 URL
```

同一会话内多次调用返回相同 URL，保证一致性。

---

## AI 一键接入

把以下提示词发给任意 AI（ChatGPT、Claude、Copilot 等），AI 会自动帮你接入：

```
在你的 HTML 页面中接入随机图片 API：
1. 在 </body> 前引入脚本：<script src="https://img.399520.xyz/random.js"></script>
2. 需要横屏图的地方用 <img alt="random:h" />
3. 需要竖屏图的地方用 <img alt="random:v" />
4. 需要背景图用 <div data-random-bg="h"> 或 <div data-random-bg="v">
5. JS 中可直接调用 getRandomPicH() / getRandomPicV() 获取 URL
```

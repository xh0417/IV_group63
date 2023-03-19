import altair as alt
import pandas as pd
import json

# 生成Altair图表规范
data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
chart = alt.Chart(data).mark_point().encode(x='x', y='y')
spec = chart.to_dict()

# 将规范转换为JSON格式，并将其发送到前端
json_spec = json.dumps(spec)

# 在前端，使用Vega-Lite API解析规范并呈现图表
# 在HTML页面中添加一个元素，用于呈现图表
<div id="vis"></div>

// 使用Vega-Lite API创建可视化对象
var vis = new vega.View(vega.parse(json_spec), {
  renderer: 'canvas',
  container: '#vis'
});

// 在可视化对象上注册选择器交互
var selector = new vega.Selector('selector')
  .encodings('x')
  .marks('points')
  .on('select', function(event, item) {
    // 根据选择的数据点更新其他元素
    console.log('Selected data points:', event.items);
  });

vis.addSelector('selector', selector);
vis.run();

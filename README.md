# DNFCalculating
  主要框架由纸飞机实现，西瓜协助修改，SCUDRT优化排序，python编写，pyqt5图形GUI库<br>
  <b>如果有兴趣添加职业整合,可加群：1019815121,记得备注下职业</b><br>

## 各职业实现
  女大枪(纸飞机提供)、男大枪(幕城提供)、剑魔(爱敏777提供)由纸飞机完成<br>
  剑豪(东总提供)、狂战(东总提供)、光枪(东总提供)、毒王(东总提供)由纸飞机完成<br>
  女机械由荔枝贝壳完成<br>
  女弹药由西瓜完成<br>
  将军由RBQ小一完成<br>
  
## 程序目录结构说明
### Part目录
  职业相关文件目录,由职业名.py及sum.py组成,职业名.py负责各个职业的个性化数据,sum.py负责引用所有职业<br>
  
### PublicReference目录
  公共实现部分,由base.py 装备.py 装备函数.py组成
  
#### PublicReference/base.py
  核心算法及主体界面绘制部分<br>
  常规无需修改该部分,如需要优化程序的效率及部分算法，可尝试修改<br>
  主体核心可优化空间比较大,但由于接触PY才几个礼拜,对PY多核心运算的不熟悉,暂不打算修改,欢迎尝试优化

#### PublicReference/装备.py
  装备及套装数据部分<br>
  如需要添加修改装备.可在此处修改,注意装备的后缀数字,需要与img/装备下的文件名一致(新增需要同步添加图标)

#### PublicReference/装备函数.py
  一些计算公式部分,除非公式出现偏差,否则无需修改<br>

### ResourceFiles目录
  资源文件目录,由公用资源文件及职业资源文件组成<br>
  
  
### main.py
  程序入口页面,职业相关部分已经抽出,无需修改<br>
  

## 添加一个职业的步骤
  1 在Part目录下,创建职业.py文件,实现参考其他职业,<br>
  2 在ResourceFiles目录下创建对应的职业素材文件夹,结构参考其他职业
  3 在技能文件夹中添加技能图标,图片后缀为png,buff图标命名为BUFF.png<br>
  4 参考其他职业,在.py文件中完善技能数据及部分特殊的算法(如果有比较奇怪的算法需要时间,可以参考芙蕾雅.py修改技能类结构,或者修改伤害算法)<br>
  5 在Part/sum.py中引入并添加对应职业<br>
  6 由于技能及被动等已经做过抽象化同时进行过扩展,因此大部分职业只需要录入基础数据等就可以,小部分采用/CD无法计算的续航类技能等,可参考芙蕾雅.py进行计算函数个性化实现<br>
  7  技能及被动等只扩展了技能的三条属性,第一条技能hit默认1,2|3条hit默认为0,需要手动赋值;如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数;固伤在填写基础及成长的时候需要注意,技能面板/独立得到的成长及数值需要*100<br>
  8 如果需要添加武器,在PublicReference/装备.py添加装备属性,同时在ResourceFiles/img/装备装备下添加对应图标
  


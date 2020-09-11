from PublicReference.base_buff import *


class BUFF·神启·圣骑士技能0(被动技能) :
    名称 = '守护恩赐'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    额外体精 = 0
    站街生效 = 1
    体力 = [0, 20, 24, 28, 32, 36, 41, 46, 51, 57, 63, 69, 75, 81, 88, 95, 103, 111, 119, 127, 135, 144, 153, 163, 172, 182, 192, 203, 213, 224, 235, 247, 259, 271, 283, 295, 309, 322, 335, 349, 363, 377, 391, 407, 421, 437, 453, 469, 485, 501, 518, 532, 548, 564, 580, 596, 611, 627, 643, 659, 675]
    精神 = [0, 54, 58, 62, 66, 70, 75, 80, 85, 91, 97, 103, 109, 115, 122, 129, 137, 145, 153, 161, 169, 178, 187, 197, 206, 216, 226, 237, 247, 258, 269, 281, 293, 305, 317, 329, 343, 356, 369, 383, 397, 411, 425, 441, 455, 471, 487, 503, 519, 535, 552, 566, 582, 598, 614, 630, 645, 661, 677, 693, 709]
    def 体力加成(self):
        return self.体力[self.等级] + self.额外体精

    def 精神加成(self):
        return self.精神[self.等级] + self.额外体精

    def 结算统计(self): 
        return [0, self.体力加成(), self.精神加成(), 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class BUFF·神启·圣骑士技能1(主动技能):
    名称 = '守护徽章'
    所在等级 = 25
    等级上限 = 40
    基础等级 = 30
    守护徽章per = 0.15
    数值 = [0, 24, 26, 28, 31, 33, 35, 38, 40, 43, 46, 49, 51, 55, 58, 61, 64, 67, 71, 75, 78, 82, 85, 89, 93, 97, 101, 106, 110, 114, 119, 123, 128, 133, 137, 142, 147, 152, 157, 163, 167]
    def 体力加成(self):
        return int(self.数值[self.等级] * (1 + self.守护徽章per))

    def 精神加成(self):
        return int(self.数值[self.等级] * (1 + self.守护徽章per))

    def 结算统计(self): 
        return [0, self.体力加成(), self.精神加成(), 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class BUFF·神启·圣骑士技能2(主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数值 = [0, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    
    def 结算统计(self): 
        return [0, 0, 0, 0, 0, self.数值[self.等级], self.数值[self.等级], self.数值[self.等级]]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class BUFF·神启·圣骑士技能3(主动技能):
    名称 = '荣誉祝福'
    所在等级 = 30
    等级上限 = 40
    基础等级 = 10
    BUFF力量per = 0
    BUFF智力per = 0
    BUFF物攻per = 0
    BUFF魔攻per = 0
    BUFF独立per = 0
    BUFF力量 = 0
    BUFF智力 = 0
    BUFF物攻 = 0
    BUFF魔攻 = 0
    BUFF独立 = 0
    三攻 = [0, 43, 44, 46, 48, 49, 51, 53, 54, 56, 58, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 86, 88, 90, 91, 93, 95, 96, 98, 100, 101, 103, 105, 106, 109]
    力智 = [0, 164, 175, 186, 198, 209, 219, 230, 241, 253, 264, 275, 286, 298, 309, 320, 330, 341, 353, 364, 375, 386, 398, 409, 420, 431, 441, 453, 464, 475, 486, 498, 509, 520, 531, 543, 553, 564, 575, 586, 598]
    
    def 结算统计(self):
        倍率 = self.适用数值 / 620 + 1
        temp = []
        temp.append(0) #智力
        temp.append(0) #体力
        temp.append(0) #精神
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 3) * 倍率)) #力量
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 3) * 倍率)) #智力
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 3) * 倍率)) #物攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 3) * 倍率)) #魔攻
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 3) * 倍率)) #独立
        return temp

    def BUFF面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.BUFF力量) * self.BUFF力量per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.BUFF智力) * self.BUFF智力per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF物攻) * self.BUFF物攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF魔攻) * self.BUFF魔攻per, 0)))
        temp.append(int(round((self.三攻[self.等级] + self.BUFF独立) * self.BUFF独立per, 0)))
        return temp

class BUFF·神启·圣骑士技能4(被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    额外体精 = 0
    力智 = [0, 40, 48, 58, 67, 77, 87, 98, 109, 120, 133, 144, 157, 171, 184, 198, 212, 226, 242, 258, 273, 290, 306, 323, 341, 359, 378, 397, 416, 436, 456, 476, 498, 518, 541, 562, 586, 609, 632, 654, 678]
    体精 = [0, 31, 38, 45, 53, 60, 68, 76, 85, 94, 104, 113, 123, 134, 144, 154, 166, 177, 189, 202, 213, 226, 239, 253, 266, 281, 296, 310, 325, 341, 356, 372, 389, 405, 423, 439, 458, 476, 494, 511, 530]
    
    def 体力加成(self):
        return self.体精[self.等级] + self.额外体精

    def 精神加成(self):
        return self.体精[self.等级] + self.额外体精

    def 结算统计(self): 
        return [0, self.体力加成(), self.精神加成(), self.力智[self.等级], self.力智[self.等级], 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class BUFF·神启·圣骑士技能5(主动技能):
    名称 = '天启之珠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    一觉力智 = 0
    一觉力智per = 0
    #28 原力智 941  测试修改为 939
    力智 = [0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668]
    
    def 结算统计(self):
        倍率 = self.适用数值 / 750 + 1
        x = (self.力智[self.等级] + self.一觉力智) * 倍率
        return [0, 0, 0, int(x * self.一觉力智per), int(x * self.一觉力智per), 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

    def 一觉面板(self):
        temp = []
        temp.append(self.名称)
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        temp.append(int(round((self.力智[self.等级] + self.一觉力智) * self.一觉力智per, 0)))
        return temp

class BUFF·神启·圣骑士技能6(主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    体精 = [0, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 47, 50, 52, 55, 57, 60, 62, 65, 67, 70, 72, 75, 77, 80, 82, 85, 87, 90, 92, 95, 97, 100, 102, 105, 107, 110]
    def 体力加成(self):
        return self.体精[self.等级] * 24

    def 精神加成(self):
        return self.体精[self.等级] * 24

    def 结算统计(self): 
        return [0, self.体力加成(), self.精神加成(), 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立

class BUFF·神启·圣骑士技能7(被动技能):
    名称 = '神之代行者'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    站街生效 = 1
    体精 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]
    def 体力加成(self):
        return self.体精[self.等级]

    def 精神加成(self):
        return self.体精[self.等级]

    def 结算统计(self): 
        return [0, self.体力加成(), self.精神加成(), 0, 0, 0, 0, 0]
        #智力 体力 精神  力量  智力  物攻  魔攻 独立


class BUFF·神启·圣骑士技能8(主动技能):
    名称 = '最后的审判'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23

    def 结算统计(self):
        return [0, 0, 0, 0, 0, 0, 0, 0]

    def 加成倍率(self):
        if self.关联技能 == ['天启之珠']:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(1.23 + self.等级 * 0.01, 2)



BUFF·神启·圣骑士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('BUFF·神启·圣骑士技能列表.append(BUFF·神启·圣骑士技能'+str(i)+'())')
        i += 1
    except:
        i = -1

BUFF·神启·圣骑士技能序号 = dict()
for i in range(len(BUFF·神启·圣骑士技能列表)):
    BUFF·神启·圣骑士技能序号[BUFF·神启·圣骑士技能列表[i].名称] = i
BUFF·神启·圣骑士一觉序号 = 0
BUFF·神启·圣骑士二觉序号 = 0
BUFF·神启·圣骑士三觉序号 = 0
for i in BUFF·神启·圣骑士技能列表:
    if i.所在等级 == 50:
        BUFF·神启·圣骑士一觉序号 = BUFF·神启·圣骑士技能序号[i.名称]
    if i.所在等级 == 85:
        BUFF·神启·圣骑士二觉序号 = BUFF·神启·圣骑士技能序号[i.名称]
    if i.所在等级 == 100:
        BUFF·神启·圣骑士三觉序号 = BUFF·神启·圣骑士技能序号[i.名称]

class BUFF·神启·圣骑士角色属性(角色属性):
    实际名称 = 'BUFF·神启·圣骑士'
    角色 = '圣职者(男)'
    职业 = '圣骑士'

    系数类型选择 = ['体力','精神']

    武器选项 = ['十字架']

    一觉序号 = 5
    三觉序号 = 8

    防具类型 = '板甲'
    防具精通属性 = ['体力','精神']

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(BUFF·神启·圣骑士技能列表)
        self.技能序号 = deepcopy(BUFF·神启·圣骑士技能序号)

    def 专属词条计算(self):
        self.技能栏[self.技能序号['守护恩赐']].额外体精 = self.守护恩赐体精
        self.技能栏[self.技能序号['信念光环']].额外体精 = self.信念光环体精
        self.技能栏[self.技能序号['守护恩赐']].等级加成(self.转职被动Lv)
        # self.技能栏[self.技能序号['守护徽章']].守护徽章per = self.守护徽章per
        self.技能栏[self.技能序号['荣誉祝福']].等级加成(self.BUFFLv)
        self.技能栏[self.技能序号['荣誉祝福']].BUFF力量per = self.BUFF力量per
        self.技能栏[self.技能序号['荣誉祝福']].BUFF智力per = self.BUFF智力per
        self.技能栏[self.技能序号['荣誉祝福']].BUFF物攻per = self.BUFF物攻per
        self.技能栏[self.技能序号['荣誉祝福']].BUFF魔攻per = self.BUFF魔攻per
        self.技能栏[self.技能序号['荣誉祝福']].BUFF独立per = self.BUFF独立per
        self.技能栏[self.技能序号['荣誉祝福']].BUFF力量 = self.BUFF力量
        self.技能栏[self.技能序号['荣誉祝福']].BUFF智力 = self.BUFF智力
        self.技能栏[self.技能序号['荣誉祝福']].BUFF物攻 = self.BUFF物攻
        self.技能栏[self.技能序号['荣誉祝福']].BUFF魔攻 = self.BUFF魔攻
        self.技能栏[self.技能序号['荣誉祝福']].BUFF独立 = self.BUFF独立
        self.技能栏[self.技能序号['天启之珠']].等级加成(self.一觉Lv)
        self.技能栏[self.技能序号['天启之珠']].一觉力智 = self.一觉力智
        self.技能栏[self.技能序号['天启之珠']].一觉力智per = self.一觉力智per
        self.技能栏[self.技能序号['信念光环']].等级加成(self.一觉被动Lv)

    def BUFF计算(self, x = 0):
        总数据 = self.数据计算()
        关联技能 = self.技能栏[self.技能序号['最后的审判']].关联技能

        if '天启之珠' in 关联技能:
            for j in range(8):
                总数据[self.技能序号['最后的审判']][j] = int(总数据[self.技能序号['天启之珠']][j] * (self.技能栏[self.技能序号['最后的审判']].绑定一觉力智per + self.技能栏[self.技能序号['最后的审判']].等级 * 0.01))
                总数据[self.技能序号['天启之珠']][j] = 0
        elif '神圣洗礼：信仰之翼' in 关联技能:
            for j in range(8):
                总数据[self.技能序号['最后的审判']][j] = int(总数据[self.技能序号['天启之珠']][j] * (self.技能栏[self.技能序号['最后的审判']].绑定二觉力智per + self.技能栏[self.技能序号['最后的审判']].等级 * 0.01))
        return self.结果返回(x, 总数据)

class BUFF·神启·圣骑士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = BUFF·神启·圣骑士角色属性()
        self.角色属性A = BUFF·神启·圣骑士角色属性()
        self.角色属性B = BUFF·神启·圣骑士角色属性()
        self.一觉序号 = BUFF·神启·圣骑士一觉序号
        self.二觉序号 = BUFF·神启·圣骑士二觉序号
        self.三觉序号 = BUFF·神启·圣骑士三觉序号
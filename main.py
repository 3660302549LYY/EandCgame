import random
from wordbase import siji_chinese,siji_data,siba_data_chinese,siba_data_all
import os
import datetime as t


all_chinese=[]   #存储中文列数据
all_data=[]   #存储所有数据
score=0   #初始化分数
time_count=0   #初始化总用时
count=0   #计数器
def get_random_chinese():
    global count   #声明全局变量
    global time_count   #声明全局变量
    global score   #声明全局变量
    answer=all_data[random.randint(0,len(all_data)-1)]    #获取随机行数据
    part_new_data_english=answer[0]   #获取英文部分数据
    part_new_data_chinese=answer[1]   #获取中文部分数据
    choice_list2=[]
    order=["A","B","C","D","."]
    for i in range(4):
        temp_chinese=all_chinese[random.randint(0, len(all_data) - 1)]
        choice_list2.append(order[i] +order[4]+temp_chinese)   #生成四个随机中文词汇列表

    new_index=random.randint(0,3)
    if new_index == 0:
        choice_list2[new_index]="A."+part_new_data_chinese   #将新数据英文替换为随机中文词汇
        choice="A"
        choice2="a"
        choice3="1"
    elif new_index==1:
        choice_list2[new_index]="B."+part_new_data_chinese   #将新数据英文替换为随机中文词汇
        choice="B"
        choice2="b"
        choice3="2"
    elif new_index==2:
        choice_list2[new_index]="C."+part_new_data_chinese   #将新数据英文替换为随机中文词汇
        choice="C"
        choice2="c"
        choice3="3"
    else:
        choice_list2[new_index]="D."+part_new_data_chinese   #将新数据英文替换为随机中文词汇
        choice="D"
        choice2="d"
        choice3="4"
    count += 1  # 计数器加1
    print("第"+str(count)+"题：")   #输出英文部分数据
    print(part_new_data_english+"的中文释义是：\n")   #用户输入选项

    for i in range(4):
        print(choice_list2[i])   #输出四个随机中文词汇列表
    print("\n")   #输出正确答案
    t1 = t.datetime.now()
    user_choice = input("你的选择是：")  # 输出用户选择
    t2 = t.datetime.now()
    dt = int((t2 - t1).total_seconds())  # 计算用时
    time_count += dt

    if user_choice==choice or user_choice==choice2 or user_choice==choice3:   #判断用户选择是否正确
        print("回答正确！")
        score+=10   #每回答正确加10分
        os.system('cls')   #清空控制台
        print("上一题用时："+str(dt)+"秒\n")  # 输出用时
        if dt>=4:   #每分钟加10分
            score-=6
        get_random_chinese()  #递归调用函数，继续游戏
    else:
        print("回答错误！正确答案是："+answer[1])   #输出正确答案
        print("共答对"+str(count-1)+"题，得分"+str(score)+"分，\n总用时："+str(time_count)+"秒\n"+"游戏结束！")   #输出总用时
        if_exit=input("是否退出游戏？(1 or y/n or Enter):\n")   #用户输入是否退出游戏
        if if_exit=="y" or if_exit=="1":
            exit()   #退出游戏
        else:
            count = 0  # 计数器清零
            score = 0  # 分数清零
            time_count = 0  # 总用时清零
            os.system('cls')   #清空控制台
            clist()   #递归调用函数，继续游戏

def clist():
    global all_chinese   #声明全局变量
    global all_data   #声明全局变量
    choice_list1=input("请选择词库：\na.四级词库（4616个词汇）(默认按Enter键)\nb.四八级词库（12815个词汇）\n请输入：（参数包含：a、A、b、B、Enter）")
    print(choice_list1) 
    if choice_list1=="a":
                all_chinese=siji_chinese   #存储中文列数据
                all_data=siji_data   #存储所有数据
                print("您选择了四级词库")   #输出中文列数据
                print("\n")
                get_random_chinese()   #递归调用函数，开始游戏
    elif choice_list1=="A":
                all_chinese=siji_chinese   #存储中文列数据
                all_data=siji_data   #存储所有数据
                print("您选择了四级词库")   #输出中文列数据
                print("\n")
                get_random_chinese()   #递归调用函数，开始游戏
    elif choice_list1=="":
                all_chinese=siji_chinese   #存储中文列数据
                all_data=siji_data   #存储所有数据
                print("您选择了四级词库")   #输出中文列数据
                print("\n")
                get_random_chinese()   #递归调用函数，开始游戏


    elif choice_list1=="b":
                all_chinese=siba_data_chinese   #存储中文列数据
                all_data=siba_data_all   #存储所有数据
                print("您选择了四八级词库")   #输出中文列数据
                print("\n")
                get_random_chinese()   #递归调用函数，开始游戏
    elif choice_list1=="B":
                all_chinese=siba_data_chinese   #存储中文列数据
                all_data=siba_data_all   #存储所有数据
                print("您选择了四八级词库")   #输出中文列数据
                print("\n")
                get_random_chinese()   #递归调用函数，开始游戏

    else:
            print("输入错误！请重新输入！")
            clist()   #递归调用函数，继续游戏
#原创作者：郭航
print("欢迎来到英语词汇游戏！")
print("程序设计：郭航\nQQ：3600673534 \n个人博客：https://3660302549lyy.github.io（获取更多资源或最新版本）\n（手机访问时请关闭流量使用WiFi，或使用加速器，谢谢）\n版本：v1.0\n语言：Python 3.7.4\n操作系统：Windows")
print("游戏目标：测试玩家的词汇量。\n")
print("游戏规则：每一轮游戏，系统会随机选择一行数据，并给出四个随机中文词汇，其中有一个是正确的中文释义。\n玩家需要根据英文部分的中文释义，选择正确的中文释义。\n如果玩家回答错误，则游戏结束，并给出正确答案。如果玩家回答正确，则系统加10分，并继续游戏。(但答题时间超过4秒，系统扣6分)\n\n玩家可以选择退出游戏。")
print("答出正确的中文释义前的字母可以是A、B、C、D或a、b、c、d或1、2、3、4分别表示选择的中文释义。\n")
input("按Enter键开始游戏！")   #用户输入任意键开始游戏
os.system('cls')   #清空控制台
clist()   #调用函数，开始游戏
def calculate_bmi(height:int, weight:int)->float:
    if height < 120 or height > 220:
            raise Exception(f'輸入的身高: {height} 公分 不在 120 ~ 220 範圍內')
    height /= 100

    if weight < 30.0 or weight > 200.0:
            raise Exception(f'輸入的體重: {weight:.2f} 公斤 不在 30 ~ 200 範圍內')
    
    bmicalculate = weight / height ** 2
    return bmicalculate

def main():
    # BMI計算
    try:
        height: int = float(input('請輸入你的身高(公分 cm):'))      
        weight = float(input('請輸入你的體重(公斤 kg):'))
        bmicalculate = calculate_bmi(height, weight)
    except ValueError:
        print('輸入發生錯誤')
    except Exception as e :
        print(e)
    else:
        print(f'你的身高:{height*100} 公分')
        print(f'你的體重:{weight:.2f} 公斤')
        print(f'你的 BMI值為:{bmicalculate:.2f}')
        if bmicalculate < 18.5:
            print('你的體重過輕')
        elif calculate_bmi < 24:
            print('你的體重正常')
        elif calculate_bmi < 27:
            print('你的體重稍微過重')
        elif calculate_bmi < 30:
            print('你已經輕度肥胖')
        elif calculate_bmi < 35:
            print('你已經中度肥胖')
        else:
            print('你已經重度肥胖')

if __name__ == "__main__":
    main()
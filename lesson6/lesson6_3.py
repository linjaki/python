def calculate_bmi(height: int, weight: float) -> float:
    # 驗證身高範圍
    if height < 120 or height > 220:
        raise Exception(f'輸入的身高: {height} 公分 不在 120 ~ 220 範圍內')
    height /= 100  # 身高轉換成公尺

    # 驗證體重範圍
    if weight < 30.0 or weight > 200.0:
        raise Exception(f'輸入的體重: {weight:.2f} 公斤 不在 30 ~ 200 範圍內')
    
    # 計算 BMI
    bmicalculate = weight / height ** 2
    return bmicalculate

def get_state(bmi: float) -> str:
    # 根據 BMI 值返回體重狀態
    if bmi < 18.5:
        return '你的體重過輕'
    elif bmi < 24:
        return '你的體重正常'
    elif bmi < 27:
        return '你的體重稍微過重'
    elif bmi < 30:
        return '你已經輕度肥胖'
    elif bmi < 35:
        return '你已經中度肥胖'
    else:
        return '你已經重度肥胖'

def main():
    try:
        height = int(input('請輸入你的身高(公分 cm):'))        
        weight = float(input('請輸入你的體重(公斤 kg):'))  # 使用 float() 來接收體重輸入        
        bmi = calculate_bmi(height, weight)  # 計算 BMI
    except ValueError:
        print('輸入發生錯誤，請確認輸入的是數字。')
    except Exception as e:
        print(e)  # 處理範圍錯誤
    else:
        print(f'你的身高: {height} 公分')
        print(f'你的體重: {weight:.2f} 公斤')
        print(f'你的 BMI 值為: {bmi:.2f}')
        print(get_state(bmi))  # 顯示 BMI 判斷結果

if __name__ == "__main__":
    main()
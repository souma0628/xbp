"""
天気予報プログラム（OpenWeatherMap API版）
------------------------------------------
都市名を入力すると、
・現在の気温と天気
・今日の（朝・昼・夜）の天気予報
を表示します。

使用API: OpenWeatherMap（https://openweathermap.org/api）
※ APIキーは個人で取得し、外部に公開しないよう注意。
"""

import requests
from datetime import datetime, timedelta, timezone

# ==== 🔑 APIキー ====
API_KEY = "c363761924da8e3c24e32ddf4f8d5e8b"  # ★絶対にWeb上に公開しないこと！

# ==== 🌍 都市名の入力 ====
city = input("都市名を英語で入力してください（例: Tokyo, Osaka, New York）: ")

# ==== 現在の天気を取得 ====
current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja"
current_res = requests.get(current_url)

# レスポンスが成功（status_code = 200）のとき
if current_res.status_code == 200:
    current_data = current_res.json()

    city_name = current_data["name"]
    temp = current_data["main"]["temp"]
    weather = current_data["weather"][0]["description"]

    print(f"\n🌤 {city_name} の現在の天気")
    print(f"気温: {temp} ℃")
    print(f"天気: {weather}")

    # ==== 今日の天気（3時間ごとの予報）を取得 ====
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=ja"
    forecast_res = requests.get(forecast_url)

    if forecast_res.status_code == 200:
        forecast_data = forecast_res.json()

        # 現地時間の設定
        tz = timezone(timedelta(seconds=forecast_data["city"]["timezone"]))  
        now = datetime.now(tz)
        today = now.date()

        # 朝(6時前後), 昼(12時前後), 夜(18時前後)の天気を取得
        times = {"朝": 6, "昼": 12, "夜": 18}
        print("\n📅 今日の天気予報:")

        for label, hour in times.items():
            # 最も近い時間帯のデータを選択
            target = min(
                forecast_data["list"],
                key=lambda x: abs(datetime.fromtimestamp(x["dt"], tz).hour - hour)
            )
            t = datetime.fromtimestamp(target["dt"], tz)
            temp2 = target["main"]["temp"]
            w2 = target["weather"][0]["description"]
            print(f"{label}（{t.strftime('%H:%M')}） → {w2}（{temp2}℃）")

    else:
        print("⚠️ 予報データを取得できませんでした。")

else:
    print("⚠️ 都市名が間違っているか、データを取得できませんでした。")

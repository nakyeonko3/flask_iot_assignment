from flask import Flask, render_template
import spidev
import time

# SPI 인스턴스 spi 생성
spi = spidev.SpiDev()
app = Flask(__name__)

# 0 ~ 7 까지 8개의 채널에서 SPI 데이터를 읽어옵니다.
# def readadc(adcnum):
#   if adcnum > 7 or adcnum < 0:
#     return -1
#   r = spi.xfer2([1, 8 + adcnum << 4, 0])
#   data = ((r[1] & 3) << 8) + r[2]
#   return data

data = 12
@app.route('/')
def get_data():
    return render_template("get_data.html", potentialData=data)

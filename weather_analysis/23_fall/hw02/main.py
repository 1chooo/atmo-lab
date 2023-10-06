# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any
import numpy as np  
import cartopy.crs as ccrs  
import matplotlib.pyplot as plt 
import cartopy.feature as cfeature
import os

def load_data(
        file_name: str,
        var, 
        nlev,
        nlat,
        mlon,
    ) -> np.ndarray[Any]:
    data = np.fromfile(
        file_name, 
        dtype='<f4',
    )
    data = data.reshape(
        var, 
        nlev,
        nlat,
        mlon,
    )

    return data

def configure_parameters(
        mlon, 
        nlat, 
        data
    ) -> tuple[
        np.linspace,
        np.linspace,
        Any,    
        Any,    
        Any,    
        Any,
    ]:
    lon = np.linspace(90, 180, mlon)
    lat = np.linspace(15, 60, nlat)
    h = data[0, :, :, :]
    u = data[1, :, :, :]
    v = data[2, :, :, :]
    t = data[3, :, :, :]

    return (
        lon,
        lat,
        h,
        u,
        v,
        t,
    )


def count_divergence(
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ) -> np.ndarray[np.float64]:
    divergence = np.zeros(
        [nlev, nlat, mlon]
    )
    
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度
                dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:
                    # 計算x方向上的差分
                    x_value = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)
                    # 計算y方向上的差分
                    y_value = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)
                    
                    divergence[i, j, k] = x_value + y_value
                else:
                    # 單邊插植
                    # 計算 x 方向上的差分
                    if k == 0:
                        x_value = (u[i, j, k + 1] - u[i, j, k]) / dx
                    elif k == mlon - 1:
                        x_value = (u[i, j, k] - u[i, j, k - 1]) / dx
                    else:
                        x_value = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)

                    # 計算 y 方向上的差分
                    if j == 0:
                        y_value = (v[i, j + 1, k] - v[i, j, k]) / dy 
                    elif j == nlat - 1:
                        y_value = (v[i, j, k] - v[i, j - 1, k]) / dy 
                    else:
                        y_value = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)  

                    divergence[i, j, k] = x_value + y_value

    return divergence

def count_vertical_speed(
        divergence,
        nlev,
        nlat,
        mlon,
        pressure_values,
    ) -> np.ndarray[np.float64]:

    vertical_speed = np.zeros(
        [nlev, nlat,mlon]
    )
    #initial vertical speed
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度
                if i == 0:
                    vertical_speed[i, j, k] = divergence[i, j, k]*pressure_values[i]  # 初始化垂直風速
                elif i > 0:
                    vertical_speed[i, j, k] = vertical_speed[i-1, j, k]+divergence[i, j, k]*pressure_values[i]  # 計算垂直風速

    # #correction error
    # # 創建一個形狀為 [5, 25, 49] 的全零的 3D 數組
    expanded_error = np.zeros([5, 25, 49])
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度
                expanded_error[i,j,k] = vertical_speed[4,j,k]/910  # 計算擴展錯誤

    div_new = divergence - expanded_error  # 修正相對渦度
    # # correction div
    vertical_speed_new =  np.zeros([nlev,  nlat,mlon], dtype=float)  # 創建一個全零數組來存儲新的垂直風速
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度                   
                if i == 0:
                    vertical_speed_new [i, j, k] = div_new[i, j, k]*pressure_values[i]  # 初始化新的垂直風速
                elif i > 0:
                    vertical_speed_new [i, j, k] = vertical_speed_new[i-1, j, k]+div_new[i, j, k]*pressure_values[i]  # 計算新的垂直風速

    return vertical_speed_new

def check_output_dir() -> None:
    os.makedirs("imgs", exist_ok=True)

def plot_data(
        factor, 
        lat,
    ):
    # 繪製資料
    level = [1010, 925, 775, 600, 400,100]  # 高度層壓力值的列表
    # os.makedirs(title[5:], exist_ok=True)
    plt.figure(figsize=(6, 3), dpi=400)  # 創建一個畫布，設置圖形大小和DPI
    var = np.zeros((6,25))
    var[1:,:] = factor[:, :, 16]  # 提取指定經度上的數據
    contour = plt.contour(
        lat, 
        level, 
        var, 
        cmap='coolwarm',
        # cmap='jet',
        levels = np.linspace(-0.002,0.002,9)
    )
    plt.title("120E vetical velocity")  # 設置圖形標題
    plt.xticks(np.linspace(15,60,10))  # 設置x軸刻度
    plt.yscale('log')  # 設置 y 軸為對數尺度
    plt.yticks(np.linspace(1000,100,10))  # 設置y軸刻度
    # 設置 y 軸刻度標籤格式為指數形式
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
    plt.colorbar(
        contour, 
        orientation='vertical', 
        shrink=0.7, 
        label="(m/s)",
    )
    plt.gca().invert_yaxis()  # 倒轉 y 軸，使得壓力降低時y軸上升
    plt.ylim(1010, 100)  # 設置 y 軸範圍
    plt.grid(
        True, 
        linestyle='--', 
        alpha=0.5,
    )
    plt.savefig("120E_vetical_velocity.png")

    # plt.show()  # 顯示圖形

def main() -> None:
    file_name = "./output.bin"
    dy = 6378000 * 1.875 * np.pi / 180
    pressure_values = [85, 150, 175, 200, 300]

    data = load_data(
        file_name=file_name,
        var=4,
        nlev=5,
        nlat=25,
        mlon=49, 
    )

    (
        lon,
        lat,
        h,
        u,
        v,
        t,
    ) = configure_parameters(
        mlon=49,
        nlat=25,
        data=data,
    )

    divergence = count_divergence(
        u=u,
        v=v,
        dy=dy,
        nlev=5,
        nlat=25,
        mlon=49,
        lat=lat,
    )
    vertical_speed = count_vertical_speed(
        divergence=divergence,
        nlev=5,
        nlat=25,
        mlon=49,
        pressure_values=pressure_values,
    )

    plot_data(
        factor=vertical_speed,
        lat=lat,
    )

if __name__ == '__main__':
    main()
import csv
import math
import statistics


def get_mode(arr):
    arr_appear = dict((a, arr.count(a)) for a in arr)
    max_appear = max(arr_appear.values())
    if max_appear == 1:
        return None
    mode = [k for k, v in arr_appear.items() if v == max_appear]
    return mode


def diversify_wind_direction(x):
    if x == 0:
        return "Calm"
    angle_mapping = {
        11.25: 77.5,
        33.75: 45,
        56.25: 22.5,
        78.75: 0,
        101.25: 337.5,
        123.75: 315,
        146.25: 292.5,
        168.75: 270,
        191.25: 247.5,
        213.75: 225,
        236.25: 202.5,
        258.75: 180,
        281.25: 157.5,
        303.75: 135,
        326.25: 112.5,
        348.75: 90
    }
    for angle, direction in angle_mapping.items():
        if angle < x < angle + 22.5:
            return direction


def diversify_beaufort_scale(x):
    beaufort_mapping = {
        0.2001: '0',
        1.5001: '1',
        3.3001: '2',
        5.4001: '3',
        7.9001: '4',
        10.7001: '5',
        13.8001: '6',
        17.1001: '7',
        20.7001: '8',
        24.4001: '9',
        28.4001: '10',
        32.6001: '11',
        36.9001: '12',
        41.1001: '13',
        46.1001: '14',
        50.9001: '15',
        56.0001: '16',
        61.2001: '17'
    }
    for speed, scale in beaufort_mapping.items():
        if speed < x < speed + 0.1:
            return scale


def process_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        ws_24 = []
        ws = []
        wd = []
        for line in reader:
            if line[1] == '9' and line[2] == '8':
                ws_24.append(float(line[7]))
                if int(line[4]) >= 50:
                    ws.append(float(line[7]))
                    wd.append(float(line[8]))
        return ws_24, ws, wd


def calculate_wind_direction_average(ws, wd):
    wd_avg = []
    for i in range(0, len(wd), 10):
        wd_per_10_min = wd[i: i + 10]
        ws_per_10_min = ws[i: i + 10]
        wd_16 = [diversify_wind_direction(x) for x in wd_per_10_min]
        mode = get_mode(wd_16)
        count = [wd_16.index(direction) for direction in mode]
        ws_max = max([ws_per_10_min[index] for index in count])
        wd_avg.append(wd_16[ws_per_10_min.index(ws_max)])
    return wd_avg


def calculate_wind_speed_average(ws):
    ws_avg = []
    for i in range(0, len(ws), 10):
        ws_per_10_min = ws[i:i + 10]
        ws_avg.append(round(sum(ws_per_10_min) / 10, 1))
    return ws_avg


def process_hourly_data(ws_avg, wd_avg):
    u_wind = []
    v_wind = []
    for i in range(len(ws_avg)):
        angle = math.radians(wd_avg[i])
        u = abs(round(ws_avg[i] * math.cos(angle), 1))
        v = abs(round(ws_avg[i] * math.sin(angle), 1))
        u_wind.append(u)
        v_wind.append(v)
    return u_wind, v_wind


def calculate_gust(ws_24):
    gust_ws = []
    for i in range(0, len(ws_24), 10):
        ws_24_per_10_min = ws_24[i:i + 10]
        ws_p10_max = max(ws_24_per_10_min)
        ws_p10_avg = sum(ws_24_per_10_min) / 10
        gap = ws_p10_max - ws_p10_avg
        if gap > 5:
            gust_ws.append(ws_p10_max)
        else:
            gust_ws.append("NaN")
    return gust_ws


def analyze_atmospheric_data(file_path):
    ws_24, ws, wd = process_data(file_path)
    wd_avg = calculate_wind_direction_average(ws, wd)
    ws_avg = calculate_wind_speed_average(ws)
    u_wind, v_wind = process_hourly_data(ws_avg, wd_avg)
    gust_ws = calculate_gust(ws_24)
    return wd_avg, ws_avg, u_wind, v_wind, gust_ws


def main():
    file_path = "10M_tower_data1.csv"
    wd_avg, ws_avg, u_wind, v_wind, gust_ws = analyze_atmospheric_data(file_path)

    hour = 0
    for wd in wd_avg:
        hour += 1
        print("Hour:", hour, "\tWind Direction average:", wd)

    print("")

    hour = 0
    for ws in ws_avg:
        hour += 1
        print("Hour:", hour, "\tWind Speed Average:", ws)

    print("")

    hour = 0
    for u, v in zip(u_wind, v_wind):
        hour += 1
        print("Hour:", hour, "\tu_wind:", u, "\t,", "v_wind:", v)

    print("")

    hour = 0
    for gust in gust_ws:
        hour += 1
        print("Hour:", hour, "\tgust_ws:", gust)


if __name__ == "__main__":
    main()

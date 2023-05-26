import csv
import math
import matplotlib.pyplot as plt

Rd = 287.0  # J/(kg*K)
Rv = 461.5  # J/(kg*K)

def calculate_variables(line, count):
    temp = round(float(line[5]), 1)
    rh = round(float(line[6]), 1)
    p = round(float(line[9]), 1)

    if temp == -999 or rh == -999 or p == -999:
        count += 1
        return None, count

    eS = round((6.112 * math.exp((17.67 * temp) / (temp + 243.5))), 2)
    ePrime = round(((rh / 100.0) * eS), 2)
    Td = round(((243.5 * math.log(ePrime / 6.11)) / (17.76 - math.log(ePrime / 6.11))), 2)
    q = round((1000 * (((ePrime) / (Rv * (temp + 273.15))) /
        (((p - ePrime) / (Rd * (temp + 273.15))) +
        ((ePrime) / (Rv * (temp + 273.15)))))), 2)
    r = round((1000 * (((ePrime) / (Rv * (temp + 273.15))) /
        ((p - ePrime) / (Rd * (temp + 273.15))))), 2)

    return [eS, ePrime, Td, q, r], count


def process_data(filename):
    list_time, variables = [], [[], [], [], [], []]  # [eS, ePrime, Td, q, r]
    with open(filename, 'r') as inputFile:
        dataReader = csv.reader(inputFile)
        for line in dataReader:
            if line[1] == '9' and line[2] == '8':
                count = 0
                time = float(line[3]) + (float(line[4]) / 60.0)
                list_time.append(time)

                results, count = calculate_variables(line, count)
                if results is not None:
                    for i in range(len(variables)):
                        variables[i].append(results[i])

    return list_time, variables


def plot_chart(x, y1, y2, label1, label2, ylabel, title, save_filename):
    plt.figure(title)
    plt.plot(x, y1, linewidth=1.0)
    plt.plot(x, y2, linewidth=1.0)
    plt.xlabel("Time (hr)")
    plt.ylabel(ylabel)
    plt.legend([label1, label2])
    plt.title(title, fontweight="bold")
    plt.xticks(range(0, 25, 1))
    plt.xlim(0, 24.0001)
    plt.grid()
    plt.savefig(save_filename, dpi=300)


def main():
    file1 = "10M_tower_data1.csv"
    file2 = "10M_tower_data2.csv"

    list_time, variables1 = process_data(file1)
    _, variables2 = process_data(file2)

    labels = [
        "Saturated water vapor pressure (hPa)", 
        "Water vapor pressure (hPa)",
        "Dew point temperature (°C)", 
        "Specific humidity (g/kg)", 
        "Mixing ratio (g/kg)"
    ]
    filenames = [
        "Saturated_Water_Vapor_Pressure.png", 
        "Water_Vapor_Pressure.png",
        "Dew_Point_Temperature.png", 
        "Specific_Humidity.png", 
        "Mixing_Ratio.png"
    ]

    for i, label in enumerate(labels):
        plot_chart(list_time, variables1[i], variables2[i], "Tower1", "Tower2", label, f"9/8 {label}", f"./image/{filenames[i]}")

    # Find the maximum and minimum values for each tower
    variable_names = [
        "Saturated water vapor pressure", 
        "Water vapor pressure",
        "Dew point temperature", 
        "Specific humidity", 
        "Mixing ratio"
    ]
    variables = [variables1, variables2]

    for i, variable in enumerate(variables):
        print(f"{variable_names[i]}: maximum: {max(variable[i])}; minimum: {min(variable[i])}")

    plt.show()


if __name__ == "__main__":
    main()


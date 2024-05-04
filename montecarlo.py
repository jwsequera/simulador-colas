import numpy as np

def simulacion(num_servers, arrival_rate, service_rate, sim_time, num_simulaciones):
    metricas = {'tiempo_espera_promedio': [], 'tiempo_sistema': [], 'utlizizacion_servidores': []}

    for _ in range(num_simulaciones):
        time = 0
        service_times = [0] * num_servers
        wait_times = []
        service_start_times = []
        service_end_times = []

        while time < sim_time: #cuando el tiempo de simulacion 
            inter_arrival_time = np.random.exponential(1 / arrival_rate) #se genera un tiempo de llegada entre clientes
            time += inter_arrival_time #se suma el tiempo de llegada al tiempo actual

            next_server = np.argmin(service_times) #se elige el servidor que esta disponible

            if time < sim_time:
                if service_times[next_server] <= time: #Se verifica si el servidor seleccionado está disponible
                    service_start = time
                else:
                    service_start = service_times[next_server]

                service_time = np.random.exponential(1 / service_rate) 
                service_end = service_start + service_time

                wait_times.append(service_start - time)
                service_start_times.append(service_start)
                service_end_times.append(service_end)

                service_times[next_server] = service_end

        total_wait_time = sum(wait_times)
        tiempo_espera_promedio = total_wait_time / len(wait_times) if wait_times else 0
        tiempo_sistema = max(service_end_times) - min(service_start_times)
        utlizizacion_servidores = sum([end_time - start_time for start_time, end_time in zip(service_start_times, service_end_times)]) / (num_servers * time)

        metricas['tiempo_espera_promedio'].append(tiempo_espera_promedio)
        metricas['tiempo_sistema'].append(tiempo_sistema)
        metricas['utlizizacion_servidores'].append(utlizizacion_servidores)

    # Calcula el promedio de las metricas
    for metric in metricas:
        metricas[metric] = np.mean(metricas[metric])

    return metricas

# Parameters
num_servers = 3
arrival_rate = 4 
service_rate = 3
sim_time = 100
num_simulaciones = 1000

# Simulate queue and calculate metricas
# metricas = simulacion(num_servers, arrival_rate, service_rate, sim_time, num_simulaciones)

# print("Average Wait Time:", metricas['tiempo_espera_promedio'])
# print("System Time:", metricas['tiempo_sistema'])
# print("Server Utilization:", metricas['utlizizacion_servidores'])

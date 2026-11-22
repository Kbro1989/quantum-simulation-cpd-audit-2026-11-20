#!/usr/bin/env python3
"""
Quick NVML diagnostic probe
"""

import sys
sys.path.insert(0, r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
import cupy

def test_nvml():
    try:
        import pynvml
        print(f"pynvml loaded successfully")
        pynvml.nvmlInit()
        print("nvmlInit: OK")
        
        for i in range(2):
            try:
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                print(f"Device {i}: handle = {handle}")
                dev_name = pynvml.nvmlDeviceGetName(handle)
                print(f"  Name: {dev_name}")
                total_mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
                print(f"  Total VRAM: {total_mem.total / 1024**3:.2f} GB")
                
                power = pynvml.nvmlDeviceGetPowerUsage(handle)
                print(f"  Power: {power} mW")
                
                temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
                print(f"  Temp: {temp} C")
                
                utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
                print(f"  GPU Util: {utilization.gpu}%, Mem Util: {utilization.memory}%")
                
                sm_clock = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM)
                mem_clock = pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM)
                print(f"  SM Clock: {sm_clock} MHz, Mem Clock: {mem_clock} MHz")
                
                energy = pynvml.nvmlDeviceGetTotalEnergyConsumption(handle)
                print(f"  Total Energy: {energy} mJ")
                
            except Exception as e:
                print(f"Device {i}: ERROR - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_nvml()
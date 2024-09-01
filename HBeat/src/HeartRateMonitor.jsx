import React, { useEffect, useState } from 'react';
async function getHeartRateDevice() {
  try {
    const device = await navigator.bluetooth.requestDevice({
      filters: [{ services: ['heart_rate'] }]
    });
    return device;
  } catch (error) {
    console.error('Bluetooth Device Error:', error);
    return null;
  }
}

async function getHeartRate() {
  const device = await getHeartRateDevice();
  if (!device) return null;

  try {
    const server = await device.gatt.connect();
    const service = await server.getPrimaryService('heart_rate');
    const characteristic = await service.getCharacteristic('heart_rate_measurement');
    
    characteristic.startNotifications();
    
    return new Promise((resolve) => {
      characteristic.addEventListener('characteristicvaluechanged', (event) => {
        const value = event.target.value;
        const heartRate = value.getUint8(1);
        resolve(heartRate);
      });
    });
  } catch (error) {
    console.error('Bluetooth GATT Error:', error);
  }
}

function HeartRateMonitor() {
  const [heartRate, setHeartRate] = useState(null);

  useEffect(() => {
    async function fetchHeartRate() {
      const rate = await getHeartRate();
      setHeartRate(rate);
    }

    fetchHeartRate();
  }, []);

  return (
    <div>
      <h1>HBeat</h1>
      <p>{heartRate ? `${heartRate} bpm` : '0'}  bpm</p>
    </div>
  );
}

export default HeartRateMonitor;

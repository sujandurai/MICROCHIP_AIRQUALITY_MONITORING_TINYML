// ============================================================
// ESP-01S WiFi Bridge for AQMS PIC32CM System
// Target: ESP8266 (ESP-01S)
// Flow: PIC32 sends AT commands → ESP-01S connects to 'sujandurai'
//       hotspot → publishes sensor JSON to broker.hivemq.com →
//       Dashboard at sujandurai.github.io/AQMS_dashboard subscribes
//       via MQTT over WebSocket
//
// MQTT Topic: aqms/pic32/data
// Broker:     broker.hivemq.com:1883
// Client ID:  aqms-pic32
//
// NOTE: This sketch runs on the ESP-01S itself (flashed via
//       Arduino IDE with ESP8266 board package). The PIC32 controls
//       it via AT commands over SERCOM5 (PB02/PB03 at 115200 baud).
//       Flash this only if you need the ESP to self-manage WiFi.
//       For AT-command mode, just use the default AT firmware.
// ============================================================

// This file is INFO ONLY for AT-command mode.
// The real working flow uses the AT firmware already on the ESP-01S.
// The PIC32 main.c handles all AT commands via wifi_manager.c.
//
// To test ESP-01S connectivity manually via serial terminal:
//   1. AT                    => OK
//   2. AT+CWMODE=1           => OK
//   3. AT+CWJAP="sujandurai","12345678"  => WIFI GOT IP
//   4. AT+CIPSTART="TCP","broker.hivemq.com",1883  => CONNECT
//   5. AT+CIPSEND=24         => > (send MQTT CONNECT packet)

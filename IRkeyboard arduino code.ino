#include <IRremote.h>

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(2, ENABLE_LED_FEEDBACK);  // 使用 D2 引脚
  Serial.println("IR Receiver ready!");
}

void loop() {
  if (IrReceiver.decode()) {
    // 打印红外编码（十六进制）
    Serial.print("Received IR code: 0x");
    Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);

    IrReceiver.resume(); // 等待下一个信号
  }
}


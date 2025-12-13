void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == 'A') { // analogRead A0
      int val = analogRead(A0);
      Serial.println(val);
    }

    if (c == 'D') { // digitalRead pin 7
      int val = digitalRead(7);
      Serial.println(val);
    }

    if (c == 'P') { // PWM write (pin 11)
      int value = Serial.parseInt();
      analogWrite(11, value);
    }

    if (c == 'W') { // digitalWrite
      int val = Serial.parseInt();
      digitalWrite(13, val);
    }

    if (c == 'L') {  // blink LED13
      digitalWrite(13, HIGH);
      delay(200);
      digitalWrite(13, LOW);
      delay(200);
      Serial.println("BLINK DONE");
    }
  }
}
